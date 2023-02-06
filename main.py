from apriori import Apriori
import pandas as pd
# Load the CSV file into a pandas dataframe
df = pd.read_csv("data1.csv")
# Copy the contents of the dataframe into a variable
data = df.values

# set min support and min confidence
minsup = 0.3
minconf = 0.6

# load Apriori model without selected_items
ap = Apriori(data, minsup, minconf)

# run algorithm
ap.run()

# print out frequent itemset
ap.print_frequent_itemset()

# print out rules
ap.print_rule()

