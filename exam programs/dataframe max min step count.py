import pandas as pd

data = {
    "Day 1": [1020, 2500, 450, 3000, 5000],
    "Day 2": [2400, 1000, 900, 2890, 3500],
    "Day 3": [2800, 1500, 500, 1890, 4955],
    "Day 4": [1056, 2300, 1089, 3500, 4256],
    "Day 5": [1089, 3500, 2000, 4500, 5000],
    "Day 6": [2800, 1500, 500, 1890, 4955],
    "Day 7": [1080, 2800, 1080, 2890, 3855]
}

df = pd.DataFrame(data, index=["Jack", "Lawrence", "Susen", "Kiran", "George"])


df["Average Step Count"] = df.mean(axis=1).round(1)

df["Total Step Count"] = df.drop(columns="Average Step Count").sum(axis=1)
df["Minimum Step Count"] = df.min(axis=1).astype(int)

df["Maximum Step Count"] = df[["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]].max(axis=1)


df = df[["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Total Step Count", "Average Step Count", "Minimum Step Count", "Maximum Step Count"]]

print(df)
