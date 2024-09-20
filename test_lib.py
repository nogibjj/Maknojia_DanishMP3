"""
Test File
"""

from lib.lib import (
    csv_open,
    grouping,
    summary_stat,
    bar_chart,
    scatterplot,
    mapplot,
)
import pandas as pd
from io import StringIO


def test_csv_open():
    csv_data = """Team,Points,Country
                  RedBull,200,Austria
                  Mercedes,180,Germany
                  Ferrari,150,Italy
                  McLaren,100,United Kingdom"""
    csv_file = StringIO(csv_data)

    result_df = csv_open(csv_file)

    assert result_df.shape == (4, 3), "DataFrame should have 4 rows and 3 columns"
    assert list(result_df.columns) == [
        "Team",
        "Points",
        "Country",
    ], "Columns do not match expected names"


def test_grouping():
    csv_data = """Team,Points,Country
                  RedBull,200,Austria
                  Mercedes,180,Germany
                  Ferrari,150,Italy
                  McLaren,100,United Kingdom"""
    df = pd.read_csv(StringIO(csv_data))

    grouped = grouping(df, "Country", "Points")

    assert grouped.shape[0] == 4, "Grouped DataFrame should have 4 rows"

    # Check if the grouped DataFrame is sorted by summed Points
    expected_countries = ["United Kingdom", "Italy", "Germany", "Austria"]
    assert (
        list(grouped["Country"]) == expected_countries
    ), "Countries should be sorted by summed Points"

    # Check the summed points for each country
    assert (
        grouped.loc[grouped["Country"] == "United Kingdom", "Points"].values[0] == 100
    )
    assert grouped.loc[grouped["Country"] == "Italy", "Points"].values[0] == 150
    assert grouped.loc[grouped["Country"] == "Germany", "Points"].values[0] == 180
    assert grouped.loc[grouped["Country"] == "Austria", "Points"].values[0] == 200


def test_summary_stat():
    csv_data = """Team,Points,Country
                  RedBull,200,Austria
                  Mercedes,180,Germany
                  Ferrari,150,Italy
                  McLaren,100,United Kingdom"""
    df = pd.read_csv(StringIO(csv_data))

    stats = summary_stat(df)

    assert "Points" in stats.columns, "'Points' should be in the summary statistics"
    assert stats.loc["mean", "Points"] == 157.5, "Expected mean of Points to be 157.5"


def test_bar_chart():
    csv_data = """Team,Points,Country
                  RedBull,200,Austria
                  Mercedes,180,Germany
                  Ferrari,150,Italy
                  McLaren,100,United Kingdom"""
    df = pd.read_csv(StringIO(csv_data))

    try:
        # plt.figure()
        bar_chart(df)
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Bar chart plot failed: {e}")

    assert plot_success, "Bar chart function should not raise exceptions."


def test_scatterplot():
    csv_data = """Team,Points,Country
                  RedBull,200,Austria
                  Mercedes,180,Germany
                  Ferrari,150,Italy
                  McLaren,100,United Kingdom"""
    df = pd.read_csv(StringIO(csv_data))

    try:
        # plt.figure()
        scatterplot(df)
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Scatterplot failed: {e}")

    assert plot_success, "Scatterplot function should not raise exceptions."


def test_mapplot():
    csv_data = """Team,Points,Country
                  RedBull,200,Austria
                  Mercedes,180,Germany
                  Ferrari,150,Italy
                  McLaren,100,United Kingdom"""
    df = pd.read_csv(StringIO(csv_data))

    try:
        # plt.figure()
        mapplot(df)
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Map plot failed: {e}")

    assert plot_success, "Map plot function should not raise exceptions."
