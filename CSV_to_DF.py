import pandas as pd

df=pd.read_csv('Employee.csv')
print(df)

# Display the first 3 rows
print(df.head(3))

# show summary information about the Dataframes
print(df.info())

# Display summary statistics of numeric columns
print(df.describe())

#  Filter rows where salary is greater than 80000
high_salary_df=df[df['Salary']>80000]
print(high_salary_df)

# Sort by Age in descending order
sorted_df=df.sort_values(by='Age',ascending=False)
print(sorted_df)