# import numpy as np
import pandas as pd


# arr=np.array([1,2,3,4,5])
# print(arr)
#
# # Reshape to a 2x3 array
# reshaped_arr=np.arrange(6).reshape(2,3)
# print("Reshaped array: ",reshaped_arr)
#
# # Element-wise addition
# arr_add=arr+10
# print("Add 10 to each element:",arr_add)
#
# # Element-wise multiplication
# arr_mul=arr*2
# print("Multiplied each element by 2: ",arr_mul)
#
# # Slicing arrays
# sliced_array=arr[1:4]
# print("Sliced array: ",sliced_array)
# df=pd.read_csv("sample_data.csv")
# print(df)
#
# # Replace empty strings and strings with only spaces with NaN
# df.replace(r'^\s*$',np.nan,regex=True,inplace=True)
#
# # check for missing values
# print(df.isnull().sum())
#
# # Display rows with missing data
# print(df[df.isnull().any(axis=1)])

# Drop rows with any missing values
# df_cleaned=df.dropna()
# print(df_cleaned)
# # Modify the existing dataframe
# df.loc[2,'City']='California'
# df.loc[3,'Age']=27
# df.loc[4,'Salary']=65000
# print(df)

# df1=pd.DataFrame({
#     'employee_id':[1,2,3,4],
#     'employee_name':['John Doe','Jane smith','Sam Brown','Emily Davis']
# })
# df2=pd.DataFrame({
#     'employee_id':[3,4,5,6],
#     'department':['Finance','HR','IT','Marketing']
# })
#
# merged_df=pd.merge(df1,df2,on='employee_id',how='inner')
# print(merged_df)

df=pd.DataFrame({
    'employee_id':[1,2,2,3,3,3],
    'department':['HR','IT','IT','Finance','Finance','Finance'],
    'Salary':[50000,60000,62000,55000,58000,60000]
})
grouped_df=df.groupby('department')['Salary'].mean().reset_index()
print(grouped_df)