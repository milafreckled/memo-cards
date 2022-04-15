# List with duplicates
dupl = [3, 3, 10, 12, 4, 5, 8, 9, 9, 10]
no_dupl = list(dict.fromkeys(dupl))
print(no_dupl)