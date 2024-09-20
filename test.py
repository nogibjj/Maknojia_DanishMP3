from test_lib import (
    test_csv_open,
    test_grouping,
    test_summary_stat,
    test_bar_chart,
    test_scatterplot,
)


def run_tests():

    print("Testing csv_open()")
    test_csv_open()

    print("Testing grouping()")
    test_grouping()

    print("Testing summary_stat()")
    test_summary_stat()

    print("Testing bar_chart()")
    test_bar_chart()

    print("Testing scatterplot()")
    test_scatterplot()

    print("Tests ran successfully!")


if __name__ == "__main__":
    run_tests()
