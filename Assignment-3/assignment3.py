# Assignment-3, Cognitive Computing UCS420
# Pandas Q1-Q5
# Nilabh Kishore Gupta

import pandas as pd

# Q1. Create a dataset as given in the table (Tid, Refund, Marital_Status, Taxable_Income, Cheat)
data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital_Status": ["Single", "Married", "Single", "Married", "Divorced",
                        "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable_Income": ["125K", "100K", "70K", "120K", "95K",
                        "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}
df = pd.DataFrame(data)
print(df)

# Q2. locate row 0, 4, 7 and 8 using DataFrame
print("\n", df.loc[[0, 4, 7, 8]])

# Q3. navigate the DataFrame
# 1. rows index 3 to 7
# 2. rows 4 to 8, columns 2 to 4
# 3. all rows, columns index 1 to 3 (include 3)
print("\n", df.loc[3:7])
print("\n", df.iloc[4:9, 2:5])
print("\n", df.iloc[:, 1:4])

# Q4. read a csv file (iris dataset) and display its first five rows
iris = pd.read_csv("iris.csv")
print("\n", iris.head())

# Q5. delete row 4 and column 3 from the csv file, display the result
iris2 = iris.drop(index=4)
iris2 = iris2.drop(columns=iris.columns[3])
print("\n", iris2.head(10))
