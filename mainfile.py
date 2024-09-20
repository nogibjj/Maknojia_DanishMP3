from lib import csv_open, grouping, summary_stat, bar_chart, scatterplot


file_name = "Formula1_2023season_drivers.csv"

# Csv open
f1_dataframe = csv_open(file_name)


grouped1 = grouping(f1_dataframe, "Team", "Points")
grouped2 = grouping(f1_dataframe, "Country", "Points")

# Print stats summary
descriptioncsv = summary_stat(grouped1)
print(descriptioncsv)

# Bar chart
bar_chart(grouped1)

# Scatterplot
scatterplot(grouped1)
