import json
import csv
from datetime import datetime, timedelta

def generate_daily_message_counts(json_path, csv_path, start_date="2022-11-01"):
    with open(json_path, 'r') as file:
        data = json.load(file)

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.today()

    daily_counts = {}

    for conversation in data:
        for message in conversation.get("messages", []):
            timestamp = message.get("timestamp")
            if timestamp:
                message_date = datetime.fromisoformat(timestamp).date()
                daily_counts[message_date] = daily_counts.get(message_date, 0) + 1

    rows = []
    current_date = start_date.date()
    while current_date <= end_date.date():
        count = daily_counts.get(current_date, 0)
        rows.append({"date": current_date.strftime("%Y-%m-%d"), "number_of_messages": count})
        current_date += timedelta(days=1)

    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ["date", "number_of_messages"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

