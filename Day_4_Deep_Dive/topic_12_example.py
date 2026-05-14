import pandas as pd

df = pd.read_csv('student_marks.csv')
df['Score'] = df['Score'].fillna(df['Score'].mean())

print("--- Single Grouping ---")
subject_avg = df.groupby('Subject')['Score'].mean()
print(subject_avg)

print("\n--- Multi-Index Grouping ---")
class_subject_avg = df.groupby(['Class', 'Subject'])['Score'].mean()
print(class_subject_avg)

print("\n--- Multiple Aggregations ---")
stats = df.groupby('Subject')['Score'].agg(['mean', 'max', 'min', 'count'])
print(stats)

print("\n--- Custom Apply Function ---")
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

df['Letter_Grade'] = df['Score'].apply(assign_grade)
print(df[['Name', 'Score', 'Letter_Grade']].head())

print("\n--- Lambda Function ---")
df['Honors'] = df['Score'].apply(lambda x: True if x >= 90 else False)
print(df[['Name', 'Score', 'Honors']].head())
