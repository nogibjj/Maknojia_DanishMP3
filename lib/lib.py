import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np


# Read CSV
def csv_open(file_path):
    data = pd.read_csv(file_path)
    return data


def grouping(Dataframe, GroupName, SumName):
    # Group data by team and points
    grouped = pd.DataFrame(Dataframe.groupby(GroupName)[SumName].sum()).reset_index(
        drop=False
    )

    # Sort the new dataframe in ascending order
    grouped = grouped.sort_values(by=SumName, ascending=True)
    return grouped


def summary_stat(dataframe):
    # Get summary statistics
    description = dataframe.describe()
    return description


# Creating bar chart
def bar_chart(dataframe):
    # Setting x to nfl team column and y to fantasy points column
    x = dataframe["Team"]
    y = dataframe["Points"]

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
    # Setting x to nfl team column and y to fantasy points column
    x = dataframe["Team"]
    y = dataframe["Points"]

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


# Create mapplot
def mapplot(dataframe):
    url = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
    world = gpd.read_file(url)

    # Merge data (country_df) with the world geometry based on the "Country" column
    merged = world.merge(dataframe, left_on="NAME", right_on="Country", how="left")

    # Plot the merged GeoDataFrame
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    # Draw country boundaries
    merged.boundary.plot(ax=ax)
    merged.plot(
        column="Points",
        ax=ax,
        legend=True,
        cmap="OrRd",
        missing_kwds={"color": "lightgrey", "label": "No data"},
    )

    # Title plot and show
    plt.title("F1 2023 Season Career Driver Points by Country")
    plt.show()
