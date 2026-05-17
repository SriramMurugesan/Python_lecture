import pandas as pd
import os
csv_path = os.path.join(os.path.dirname(__file__), 'student_marks.csv')
df = pd.read_csv(csv_path)
# print(df)

# print(df.head())
# print(df.tail(3))
# print(df.shape)
# print(df.info())
print(df.describe())
# print(df.columns)
# names_series=df['Name']
# print(names_series)
# print(type(names_series))
# print(type(df))
# print(df.iloc[0]) # By index value
# print(df.loc[0, 'Name']) # By index label
# print(df.iloc[0:3, 1:3])