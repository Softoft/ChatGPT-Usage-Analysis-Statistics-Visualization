import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def plot_message_counts(csv_path, png_path, html_path):
    df = pd.read_csv(csv_path, parse_dates=["date"])

    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["number_of_messages"], label="Number of Messages", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Number of Messages")
    plt.title("Daily Message Counts")
    plt.grid(True)
    plt.savefig(png_path)
    plt.close()

    fig = px.line(df, x="date", y="number_of_messages", title="Daily Message Counts")
    fig.update_layout(xaxis_title="Date", yaxis_title="Number of Messages")
    fig.write_html(html_path)


def plot_scatter_with_moving_avg(csv_path, png_path, html_path):
    df = pd.read_csv(csv_path, parse_dates=["date"])
    df["moving_avg_7"] = df["number_of_messages"].rolling(window=7).mean()

    # Static scatter plot with Matplotlib
    plt.figure(figsize=(10, 6))
    plt.scatter(df["date"], df["number_of_messages"], color="blue", label="Number of Messages")
    plt.plot(df["date"], df["moving_avg_7"], color="red", label="7-Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Number of Messages")
    plt.title("Scatter Plot with 7-Day Moving Average")
    plt.legend()
    plt.grid(True)
    plt.savefig(png_path)
    plt.close()

    # Interactive scatter plot with Plotly
    fig = px.scatter(df, x="date", y="number_of_messages", title="Scatter Plot with 7-Day Moving Average")
    fig.add_trace(go.Scatter(x=df["date"], y=df["moving_avg_7"], mode="lines", name="7-Day Moving Average", line=dict(color="red")))
    fig.update_layout(xaxis_title="Date", yaxis_title="Number of Messages")
    fig.write_html(html_path)


def plot_box_plot(csv_path, png_path, html_path):
    df = pd.read_csv(csv_path, parse_dates=["date"])

    # Static box plot with Matplotlib
    plt.figure(figsize=(8, 6))
    plt.boxplot(df["number_of_messages"], vert=False)
    plt.xlabel("Number of Messages")
    plt.title("Box Plot of Daily Message Counts")
    plt.savefig(png_path)
    plt.close()

    # Interactive box plot with Plotly
    fig = px.box(df, y="number_of_messages", title="Box Plot of Daily Message Counts")
    fig.update_layout(yaxis_title="Number of Messages")
    fig.write_html(html_path)
