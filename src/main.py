import json
from datetime import datetime

from src.change_json_structure import extract_user_conversations
from src.create_time_data import generate_daily_message_counts
from src.generate_diagrams import plot_message_counts

if __name__ == '__main__':
    input_file = "../data/conversations.json"
    simple_json_file = "../output/user_conversations.json"
    extract_user_conversations(input_file, simple_json_file)

    csv_file = "../output/message_counts.csv"
    generate_daily_message_counts(simple_json_file, csv_file)

    png_file = "../output/message_counts.png"
    html_file = "../output/message_counts.html"
    plot_message_counts(csv_file, png_file, html_file)
