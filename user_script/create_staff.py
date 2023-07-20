import csv
import subprocess

csv_file = "users.csv"

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header line
    for row in reader:
        password, username, email = row
        subprocess.run(["tutor", "local", "do", "createuser", "--staff", "-p", password, username, email])
