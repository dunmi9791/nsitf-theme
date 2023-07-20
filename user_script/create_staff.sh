#!/bin/bash

csv_file="users.csv"

while IFS=',' read -r username password email
do
    tutor local do createuser --staff -p "$password" "$username" "$email"
done < "$csv_file"