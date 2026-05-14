import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), 'student_marks.csv')
df = pd.read_csv(csv_path)

print("--- Missing Data Check ---")
print(df.isnull().sum())

print("\n--- Strategy 1: Dropna (Attendance) ---")
df_cleaned = df.dropna(subset=['Attendance_Percentage'])
print(f"Original shape: {df.shape}, New shape: {df_cleaned.shape}")

print("\n--- Strategy 2: Fillna (Score) ---")
mean_score = df['Score'].mean()
df['Score'] = df['Score'].fillna(mean_score)
print(df.isnull().sum())

print("\n--- String Manipulation ---")
print("Before:", df.iloc[0]['Name'])
df['Name'] = df['Name'].str.strip()
print("After:", df.iloc[0]['Name'])

print("\n--- Boolean Filtering (Single) ---")
failed_students = df[df['Pass'] == False]
print(failed_students[['Name', 'Score']])

print("\n--- Boolean Filtering (Multiple) ---")
top_math = df[(df['Subject'] == 'Math') & (df['Score'] > 90)]
print(top_math[['Name', 'Class', 'Score']])
