import polars as pl
import matplotlib.pyplot as plt


# Read CSV
def csv_open(file_path):
    data = pl.read_csv(file_path)
    return data


def grouping(dataframe, group_name, sum_name):
    # Group data by team and sum points
    grouped = dataframe.group_by(group_name).agg(pl.sum(sum_name).alias(sum_name))

    # Sort the new DataFrame in ascending order
    grouped = grouped.sort(sum_name)
    return grouped


def summary_stat(dataframe, Points):
    # Get summary statistics
    description = dataframe.select(Points).describe()
    meanpoints = dataframe.select(pl.col(Points).mean())
    # description = dataframe.describe()
    # meanpoints = dataframe.mean()
    return description, meanpoints


# Creating bar chart
def bar_chart(dataframe):

    x = dataframe["Team"].to_list()
    y = dataframe["Points"].to_list()

    # Plotting the bar chart
    plt.bar(x, y, width=0.8, color="red")

    # Rotating all x-axis labels vertically to fit on the chart
    plt.xticks(range(len(x)), x, rotation="vertical")

    # Labeling the chart
    plt.title("F1 2023 Season Career Driver Points")
    plt.xlabel("Team")
    plt.ylabel("Total Career Team Driver Points")

    # Show the chart
    plt.show()


# Create Scatterplot
def scatterplot(dataframe):
    # Extracting Team and Points for plotting
    x = dataframe["Team"].to_list()
    y = dataframe["Points"].to_list()

    # Plotting the scatter chart
    plt.scatter(x, y, color="red")

    # Rotating all x-axis labels vertically to fit on the chart
    plt.xticks(range(len(x)), x, rotation="vertical")

    # Labeling the chart
    plt.title("F1 2023 Season Career Driver Points")
    plt.xlabel("Team")
    plt.ylabel("Total Career Team Driver Points")

    # Show the chart
    plt.show()
