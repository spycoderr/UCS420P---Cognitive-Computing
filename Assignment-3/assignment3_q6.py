# Assignment-3, Cognitive Computing UCS420
# Q6 - employees.csv dataset
# Nilabh Kishore Gupta

import pandas as pd

# Create a sample dataset (employees.csv) with employee info
emp_data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}
df = pd.DataFrame(emp_data)
df.to_csv("employees.csv", index=False)

# a) shape of the DataFrame
print("a)", df.shape)

# b) summary with dtypes and non-null counts
print("\nb)")
df.info()

# c) descriptive statistics
print("\nc)\n", df.describe())

# d) first 5 rows and last 3 rows
print("\nd)\n", df.head(), "\n", df.tail(3))

# e) average salary, total bonus, youngest age, highest rating
print("\ne) avg salary:", df["Salary"].mean())
print("total bonus:", df["Bonus"].sum())
print("youngest:", df["Age"].min())
print("top rating:", df["Rating"].max())

# f) sort by Salary in descending order
print("\nf)\n", df.sort_values(by="Salary", ascending=False))

# g) add Performance_Category column based on Rating
def get_category(r):
    if r >= 4.5:
        return "Excellent"
    elif r >= 4.0:
        return "Good"
    return "Average"

df["Performance_Category"] = df["Rating"].apply(get_category)
print("\ng)\n", df[["Name", "Rating", "Performance_Category"]])

# h) identify missing values
print("\nh)\n", df.isnull().sum())

# i) rename Employee_ID column to ID
df = df.rename(columns={"Employee_ID": "ID"})
print("\ni)", df.columns.tolist())

# j) employees with more than 5 years experience, and employees in IT
print("\nj)\n", df[df["Years_of_Experience"] > 5])
print("\n", df[df["Department"] == "IT"])

# k) add Tax column, 10% of Salary
df["Tax"] = df["Salary"] * 0.10
print("\nk)\n", df[["Name", "Salary", "Tax"]])

# l) save modified DataFrame to new csv
df.to_csv("employees_modified.csv", index=False)
print("\nl) saved employees_modified.csv")
