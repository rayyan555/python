cricketer = {
    "VinayKumar": [102, 5],
    "Yuzvendra Chahal": [89, 10],
    "Sandeep Sharma": [95, 8],
    "Umesh Yadav": [85, 6],
    "BhuvaneswarKumar": [106, 10],
    "Basil Thampi": [70, 5]
}

# Calculate bowling average and update dictionary values
cricketer = {player: [runs / wickets] for player, (runs, wickets) in cricketer.items()}

# Sort the dictionary based on bowling average
sorted_cricketer = {k: v for k, v in sorted(cricketer.items(), key=lambda x: x[1])}

print(sorted_cricketer)
