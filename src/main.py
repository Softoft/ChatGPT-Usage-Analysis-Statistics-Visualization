from src.change_json_structure import extract_user_conversations
from src.create_time_data import generate_daily_message_counts
from src.generate_diagrams import plot_message_counts, plot_scatter_with_moving_avg, plot_box_plot

if __name__ == '__main__':
    input_file = "../data/conversations.json"
    simple_json_file = "../output/user_conversations.json"
    extract_user_conversations(input_file, simple_json_file)

    csv_file = "../output/message_counts.csv"
    generate_daily_message_counts(simple_json_file, csv_file)

    png_file = "../output/message_counts.png"
    html_file = "../output/message_counts.html"
    plot_message_counts(csv_file, png_file, html_file)
    plot_scatter_with_moving_avg(csv_file, "../output/scatter_moving_avg.png", "../output/scatter_moving_avg.html")
    plot_box_plot(csv_file, "../output/box_plot.png", "../output/box_plot.html")
