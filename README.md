# ChatGPT Usage Analysis and Visualization Tool

**Analyze ChatGPT Usage Data** | **Python-Based Data Insights** | **Visualize Message Counts, Moving Averages, and More**

This Python project enables users to analyze ChatGPT usage data and generate powerful insights through visualizations like **message counts**, **moving averages**, and **box plots**. By exporting ChatGPT usage data, users can transform raw data into actionable insights with
daily counts, trends, and distribution analyses. This tool outputs data in various formats, including **CSV**, **PNG**, and interactive **HTML** files,
ideal for further exploration and reporting.

## Example Output

![ChatGPT Usage Scatter Plot with Moving Average](./output/scatter_moving_avg.png)

## Project Structure

```
├── .gitignore
├── data/
├── output/
│   ├── box_plot.html
│   ├── box_plot.png
│   ├── message_counts.csv
│   ├── message_counts.html
│   ├── message_counts.png
│   ├── scatter_moving_avg.html
│   ├── scatter_moving_avg.png
├── src/
│   ├── change_json_structure.py
│   ├── create_time_data.py
│   ├── generate_diagrams.py
│   ├── main.py
├── requirements.txt
└── README.md
```

## Prerequisites

- **Python 3.10+**: Required to run the analysis and visualization scripts.
- **Python Libraries**: Install necessary libraries using `pip install -r requirements.txt`.

## Setup

1. **Export and Prepare ChatGPT Usage Data**:
    - Export your ChatGPT usage data as instructed by OpenAI and unzip the data into the `./data` folder for processing.

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To execute the analysis, run:

```bash
python src/main.py
```

The script will process the ChatGPT usage data, generate statistical analyses of message counts, and produce visualizations saved to the
`output/` folder.

## Outputs and Visualizations

Each analysis output provides valuable insights into ChatGPT usage trends:

- **Daily Message Counts**:
    - `message_counts.csv`: A CSV file containing daily message counts.
    - `message_counts.png`: A static line plot showing daily message counts.
    - `message_counts.html`: An interactive HTML line plot for further exploration.

- **Scatter Plot with Moving Average**:
    - `scatter_moving_avg.png`: Scatter plot of daily message counts with a 7-day moving average.
    - `scatter_moving_avg.html`: Interactive HTML version of the scatter plot with moving average, ideal for identifying trends over time.

- **Box Plot of Message Counts**:
    - `box_plot.png`: Static box plot showing the distribution of daily message counts.
    - `box_plot.html`: Interactive HTML version of the box plot, useful for understanding variations and outliers in message volume.

## File Descriptions

- **Project Files**:
    - `.gitignore`: Lists files and folders ignored by Git.
    - `data/README.md`: Placeholder for usage data documentation.
    - `output/`: Directory containing CSV, PNG, and HTML outputs.
    - **Scripts for Data Processing**:
        - `src/change_json_structure.py`: Reformats JSON structure for easier analysis.
        - `src/create_time_data.py`: Converts raw data into time-based message counts.
        - `src/generate_diagrams.py`: Generates the visualizations from processed CSV data.
        - `src/main.py`: Main script that orchestrates data transformation and visualization generation.

## Summary

With this ChatGPT Usage Analysis tool, users can gain a deeper understanding of their ChatGPT interactions, visualize trends, and leverage
the data for better decision-making. Whether you’re analyzing daily usage patterns, visualizing trends, or creating reports, this tool makes
it easy to transform raw usage data into actionable insights.
