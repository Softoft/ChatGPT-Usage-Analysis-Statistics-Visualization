import json
from datetime import datetime

def extract_user_conversations(input_path, output_path):
    with open(input_path) as file:
        data = json.load(file)

    conversations = []

    for conv in data:
        title = conv.get("title")
        messages = []

        for msg_id, msg_data in conv.get("mapping", {}).items():
            message = msg_data.get("message")
            if message and message.get("author", {}).get("role", "") == "user":
                msg_id = message.get("id")
                timestamp = message.get("create_time")
                if timestamp:
                    timestamp = datetime.fromtimestamp(timestamp).isoformat()

                messages.append({
                    "id": msg_id,
                    "timestamp": timestamp
                })

        if messages:
            conversations.append({
                "title": title,
                "messages": messages
            })

    with open(output_path, 'w') as outfile:
        json.dump(conversations, outfile, indent=2)