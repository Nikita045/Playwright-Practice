import csv
import os

def load_csv_data(file_path):
    """
    Loads test data from CSV file and returns list of tuples
    """

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    data = []

    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Validate required columns
        required_columns = {"username2", "password2", "expected_message2"}
        if not required_columns.issubset(reader.fieldnames):
            raise ValueError(
                f"CSV must contain columns: {required_columns}"
            )

        for row in reader:
            data.append((
                row["username2"],
                row["password2"],
                row["expected_message2"]
            ))

    return data