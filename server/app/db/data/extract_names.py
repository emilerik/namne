from uuid import uuid4
from bs4 import BeautifulSoup
import csv

# type: ignore


# Load the HTML file
with open("names.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")


# Helper to extract names from a table by id
def extract_names(table_id):  # type: ignore
    table = soup.find("table", id=table_id)  # type: ignore
    return [a.text.strip() for a in table.find_all("a")]  # type: ignore


# Extract names
girl_names = extract_names("girls")  # type: ignore
boy_names = extract_names("boys")  # type: ignore

# Write to CSV files
with open("girls_name_1000_w_gender.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "gender"])
    for name in girl_names:  # type: ignore
        id = uuid4()
        writer.writerow([id, name, "girl"])

with open("boys_name_1000_w_gender.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "gender"])
    for name in boy_names:  # type: ignore
        id = uuid4()
        writer.writerow([id, name, "boy"])
