# This is a sample Python script.
import pathlib
import os
import shutil
from itertools import chain

homeDir = pathlib.Path.home()
downloads = homeDir / 'Downloads'
print(downloads.exists())
try:
    os.mkdir(downloads / "Excel files")
except FileExistsError:
    print("skipping")
# os.mkdir(downloads / "Text files")
# os.mkdir(downloads / "Install files")
# os.mkdir(downloads / "Photo files")
# os.mkdir(downloads / "Other")
for element in downloads.glob("*.xlsx"):
    shutil.move(downloads / element, downloads / "Excel files", copy_function=shutil.copytree)
for element in chain(downloads.glob("*.doc"), downloads.glob("*.docx"), downloads.glob("*.txt"), downloads.glob("*.pdf")):
    shutil.move(downloads / element, downloads / "Text files", copy_function=shutil.copytree)
for element in chain(downloads.glob("*.jpg"), downloads.glob("*.JPG"), downloads.glob("*.png"), downloads.glob("*.jpeg")):
    shutil.move(downloads / element, downloads / "Photo files")
for element in downloads.glob("*.dmg"):
    shutil.move(downloads / element, downloads / "Install files", copy_function=shutil.copytree)

print(downloads.stat())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
