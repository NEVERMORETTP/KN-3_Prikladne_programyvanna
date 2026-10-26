def _is_int(s: str) -> bool:
    if not s:
        return False
    if s[0] in ("+", "-"):
        return s[1:].isdigit() and len(s) > 1
    return s.isdigit()


def _is_float(s: str) -> bool:
    if not s:
        return False
    work = s
    if work[0] in ("+", "-"):
        work = work[1:]
    if not work:
        return False
    if work.count(".") > 1:
        return False
    return work.replace(".", "", 1).isdigit()


def parse_line(line: str) -> tuple:
    parts = [p.strip() for p in line.split(";")]
    if len(parts) != 4:
        return None, "Неправильна кількість полів"

    sensor_id, room, temp_str, hum_str = parts

    if not _is_float(temp_str):
        return None, "Температура має бути числом"

    temp = float(temp_str)
    if temp < -50.0 or temp > 80.0:
        return None, "Температура виходить за межі"

    if not _is_int(hum_str):
        return None, "Некоректна вологість"

    hum = int(hum_str)
    if hum < 0 or hum > 100:
        return None, "Некоректна вологість"

    is_anomaly = temp > 35.0 or temp < 5.0

    record = {
        "sensor_id": sensor_id,
        "room": room,
        "temperature": temp,
        "humidity": hum,
        "is_anomaly": is_anomaly,
    }
    return record, None


def load_records(lines: list) -> tuple:
    records = []
    errors = []
    for line_idx, line in enumerate(lines, start=1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        record, err = parse_line(line)
        if err is not None:
            errors.append(f"Рядок {line_idx}: {err}")
        else:
            records.append(record)
    return records, errors


def summarize(records: list) -> dict:
    summary = {}
    for r in records:
        room = r["room"]
        temp = r["temperature"]
        is_anom = r["is_anomaly"]

        if room not in summary:
            summary[room] = {
                "count": 0,
                "total": 0.0,
                "average": 0.0,
                "max": temp,
                "anomalies_count": 0,
            }

        g = summary[room]
        g["count"] += 1
        g["total"] = round(g["total"] + temp, 2)
        if temp > g["max"]:
            g["max"] = temp
        if is_anom:
            g["anomalies_count"] += 1

    for room, g in summary.items():
        if g["count"] > 0:
            g["average"] = round(g["total"] / g["count"], 2)

    return summary


def top_n(records: list, n: int) -> list:
    if n <= 0:
        return []
    sorted_recs = sorted(
        records, key=lambda r: (-r["temperature"], r["sensor_id"])
    )
    return sorted_recs[:n]


def unique_values(records: list) -> list:
    return sorted(list({r["room"] for r in records}))


def render_report(records: list) -> str:
    summary = summarize(records)
    lines = ["Звіт за кімнатами:"]
    for room, s in summary.items():
        lines.append(
            f"Кімната {room}: записів {s['count']}, "
            f"сер. темп. {s['average']:.2f}, "
            f"макс. темп. {s['max']:.2f}, "
            f"аномалій {s['anomalies_count']}"
        )
    lines.append("Підсумковий рядок:")
    lines.append(f"Всього записів: {len(records)}")
    return "\n".join(lines)


def handle_command(records: list, command: str) -> str:
    cmd = command.strip()
    cmd_lower = cmd.lower()

    if cmd_lower == "report":
        return render_report(records)

    if cmd_lower.startswith("top"):
        parts = cmd.split()
        if len(parts) == 2 and _is_int(parts[1]):
            n = int(parts[1])
            if not records:
                return "Порожньо"
            top_records = top_n(records, n)
            res = []
            for i, r in enumerate(top_records, start=1):
                res.append(f"{i}. {r['sensor_id']}: {r['temperature']:.2f}")
            return "\n".join(res)
        return "Помилка: N має бути цілим числом"

    if cmd_lower == "unique":
        return ", ".join(unique_values(records))

    if cmd_lower == "help":
        return "Команди: report, top N, unique, help, exit"

    return f"Невідома команда: {cmd}"


def main():
    print("Вставте рядки даних (порожній рядок завершує введення):")
    raw_lines = []
    while True:
        line = input()
        if line == "":
            break
        raw_lines.append(line)

    records, errors = load_records(raw_lines)
    for err in errors:
        print(err)

    while True:
        cmd = input()
        if cmd.strip().lower() == "exit":
            break
        print(handle_command(records, cmd))


if __name__ == "__main__":
    main()