import pandas as pd
import os
csv_path = os.path.join(os.path.dirname(__file__), 'student_marks.csv')
df = pd.read_csv(csv_path)
# print(df.isnull().sum())
median_score=df["Score"].median()
# print(df["Score"].mean())
df["Score"]=df["Score"].fillna(median_score)
# print(df.isnull().sum())
# print(df["Score"].mean())

# Attendance_dropna=df.dropna(subset=["Attendance_Percentage"])
#duplicates
# df_no_duplicates=df.drop_duplicates()
# print("Data without duplicates:",df_no_duplicates)


#filtering - example
# df_filtered=df[df["Name"]=="Diana Prince"]
# print("Students who scored >=50:",df_filtered)
# df_filtered=df[df["Score"]<50]
# print("Students who scored <50:",df_filtered)
# top_math = df[~(df['Subject'] == 'Math') & ~(df['Score'] > 90)]
# print(top_math)

# Group by
subject_avg = df.groupby('Subject')['Score'].mean()
print(subject_avg)

class_subject_avg = df.groupby(['Class', 'Subject'])['Score'].mean()
print(class_subject_avg)

#Aggregations
# stats = df.groupby('Subject')['Score'].agg(['mean', 'max', 'min', 'count'])
# print("Stats:",stats)

# # pivot_table
# pivot_table = df.pivot_table(index='Subject', columns='Class', values='Score', aggfunc='mean')
# print(pivot_table)

# df['Honors'] = df['Score'].apply(lambda x: True if x >= 90 else False)
# print(df[['Name', 'Score', 'Honors']].head())


january_sales = pd.DataFrame({"Item": ["Apple", "Banana"], "Sales": [100, 150]})
february_sales = pd.DataFrame({"Item": ["Cherry", "Dates"], "Sales": [200, 50]})
# print(january_sales)

master_sales = pd.concat([january_sales, february_sales], ignore_index=True)
print("Master Sales Table (Concatenated):\n", master_sales)

employees = pd.DataFrame({
    "Emp_ID": [1, 2, 3],
    "Name": ["John", "Sarah", "Mike"]
})

salaries = pd.DataFrame({
    "Emp_ID": [1, 2, 3],
    "Salary": [60000, 80000, 75000]
})

full_employee_data = pd.merge(employees, salaries, on="Emp_ID")
print("Merged Employee Table:\n", full_employee_data)