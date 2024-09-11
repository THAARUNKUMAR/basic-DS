import pandas as pd
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
s3 = pd.Series({"a": 100, "b": 200, "c": 300})

print("-----without index from list------")
print(s1)
print("-----with index from list------")
print(s2)
print("-----from dict------")
print(s3)
s1 = pd.Series([1,2,3,4,5,6,7,8,9])
s2 = pd.Series([10,20,30,40,50,60,70,80,90])

print("-----adding value 5 to all the elements in the series-------")
print(s1 + 5)

print("-----adding two pandas series----")
print(s1+s2)

print("-----subtracting two pandas series----")
print(s1-s2)
df1 = pd.DataFrame({"names": ["peter", "sharon", "bob"],
                    "marks": [8, 90, 85]})

print(df1)
iris = pd.read_csv("iris.csv")

print("-----head-----")
iris.head()
print("-----tail-----")
iris.tail()
[ ]
iris.iloc[0:3,0:2]
mean_age = details["age"].mean()
details["age"].fillna(mean_age, inplace=True)

details
details.dropna(subset=['age', 'occupation'])

