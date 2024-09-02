import pandas as pd
df=pd.read_json("Employee.json")
# print(df)

# Add a new column 'Bonus' which is 10% of salary
df['Bonus']=df['Salary']*0.10

#Save the updated Dataframe to a new JSON file
df.to_json('employees_with_bonus_json',orient='records',lines=True)