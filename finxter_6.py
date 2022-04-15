# DATA
cols = ['name', 'surname', 'gender']

db = [("Charlie", "Bucket", "male"),
      ("Augustus", "Gloop", "male"),
      ("Veruca", "Salt", "female"),
      ("Violet", "Beauregard", "female"),
      ("Mike", "Teavee", "male")]

result = [dict(zip(cols, row)) for row in db]

print(result)