import pandas as pd
# Creating a Dataframe from a dictionary with Indian Names
data={
    "Name":["Amit","Priya","Vikram","Neha","Ravi"],
    "Age": [25,30,35,40,45],
    "City": ["Mumbai","Delhi","Bangalore","Chennai","Pune"]
}
df=pd.DataFrame(data)
print(df)
# Accessing single column
print(df["Name"])

#Accessing multiple columns
print(df[["Name","Age"]])

#Accessing rows using index
print(df.iloc[0:3]) #First Row

# Filter rows where age is greater than 30
filtered_df=df[df["Age"]>30]
print(filtered_df)

# Adding a new column 'Salary'
df['Salary']=[50000,60000,70000,80000,90000]
print(df)

# Sorting by Age
sorted_df=df.sort_values(by="Age",ascending=False)
print(sorted_df)

# Rename the 'Name' column to 'Full Name' and 'Age' to 'Years'
df_renamed=df.rename(columns={"Name":"Full Name","Age":"Years"})
print(df_renamed)

# Drop the 'City' column
df_dropped=df.drop(columns=["City"])
print(df_dropped)

# Drop the row at index 2 (Vikram)
df_dropped_index=df.drop(index=2)
print(df_dropped_index)

# Create a new column 'Seniority' based on the age
df['Seniority']=df['Age'].apply(lambda x: 'Senior' if x>=35 else 'Junior')
print(df)

# Group by 'City' and Calculate the average Salary in each city
df_grouped=df.groupby("City")["Salary"].mean()
print(df_grouped)

# Apply a custom function to the 'Salary' column to add a 10% bonus
def add_bonus(salary):
    return salary*1.10
df["Salary_with_bonus"]=df['Salary'].apply(add_bonus)
print(df)

# Create another dataframe
df_new=pd.DataFrame({
    "Name":["Sonia","Rahul"],
    "Age": [29,31],
    "City": ["Kolkata","Hyderabad"],
    "Salary":[58000,63000]
})

#Merge based on the 'Name' column
df_merged=pd.merge(df, df_new, on="Name",how="left")
print(df_merged)

# Concat two DataFrames
df_concat=pd.concat([df,df_new], ignore_index=True)
print(df_concat)

# Filtering people with salary more than 50,000
high_salary=df_new[df_new['Salary']>50000]
print("People with salary more than 50,000: /n", high_salary)

# Filtering people whose name starts with 'A'
name_starts_with_a = df[df['Name'].str.startswith('A')]
print("\nPeople whose name starts with 'A':\n", name_starts_with_a)