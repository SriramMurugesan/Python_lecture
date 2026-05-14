import pandas as pd

df = pd.read_csv('student_marks.csv')

print("--- Head ---")
print(df.head())

print("\n--- Tail ---")
print(df.tail(3))

print("\n--- Shape ---")
print(df.shape)

print("\n--- Info ---")
df.info()

print("\n--- Describe ---")
print(df.describe())

print("\n--- Series vs DataFrame ---")
print(type(df))
names_series = df['Name']
print(type(names_series))

print("\n--- iloc vs loc ---")
print(df.iloc[0])        # physical position
print(df.loc[0, 'Name']) # label based
print(df.iloc[0:3, 1:3]) # slicing rows 0-2, cols 1-2
