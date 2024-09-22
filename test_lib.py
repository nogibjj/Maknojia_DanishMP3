"""
Test File
"""

from lib import csv_open, grouping, summary_stat, bar_chart, scatterplot
import polars as pl
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
    df = pl.read_csv(StringIO(csv_data))

    grouped = grouping(df, "Country", "Points")

    assert grouped.shape[0] == 4, "Grouped DataFrame should have 4 rows"

    # Check if the grouped DataFrame is sorted by summed Points
    expected_countries = ["United Kingdom", "Italy", "Germany", "Austria"]
    assert (
        list(grouped["Country"]) == expected_countries
    ), "Countries should be sorted by summed Points"

    # Check the  points for each country
    assert (
        grouped.filter(pl.col("Country") == "United Kingdom")
        .select("Points")
        .to_numpy()[0]
        == 100
    )
    assert (
        grouped.filter(pl.col("Country") == "Italy").select("Points").to_numpy()[0]
        == 150
    )
    assert (
        grouped.filter(pl.col("Country") == "Germany").select("Points").to_numpy()[0]
        == 180
    )
    assert (
        grouped.filter(pl.col("Country") == "Austria").select("Points").to_numpy()[0]
        == 200
    )


def test_summary_stat():
    csv_data = """Team,Points,Country
                  RedBull,200,Austria
                  Mercedes,180,Germany
                  Ferrari,150,Italy
                  McLaren,100,United Kingdom"""
    df = pl.read_csv(StringIO(csv_data))
    df = df.with_columns(pl.col("Points").cast(pl.Float64))

    stats, mean_points = summary_stat(df, "Points")

    assert stats.shape[0] == 9, "Description should have 8 rows"


def test_bar_chart():
    csv_data = """Team,Points,Country
                  RedBull,200,Austria
                  Mercedes,180,Germany
                  Ferrari,150,Italy
                  McLaren,100,United Kingdom"""
    df = pl.read_csv(StringIO(csv_data))

    try:
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
    df = pl.read_csv(StringIO(csv_data))

    try:
        scatterplot(df)
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Scatterplot failed: {e}")

    assert plot_success, "Scatterplot function should not raise exceptions."


if __name__ == "__main__":
    test_csv_open()
    test_grouping()
    test_summary_stat()
    test_bar_chart()
    test_scatterplot()
