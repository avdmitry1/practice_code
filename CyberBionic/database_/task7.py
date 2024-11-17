import csv
import json


def input_data():
    first_name = input("Input name: ")
    last_name = input("Input last name: ")
    birth_date = input("Input birthday (yyyy-mm-dd): ")
    city = input("Input city: ")
    return {
        "first_name": first_name,
        "last_name": last_name,
        "birth_date": birth_date,
        "city": city,
    }


def save_to_csv(data, filename="users.csv", mode="w"):
    header = ["first_name", "last_name", "birth_date", "city"]

    with open(filename, mode, newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        if mode == "w":
            writer.writeheader()
        writer.writerow(data)


def read_csv(filename="users.csv"):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def csv_to_json(filename="users.csv", json_filename="users.json"):
    data = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"Data saves to {json_filename}")


def main():
    while True:
        print("\n1: Input new data")
        print("2: Input new data to file")
        print("3: Read CSV-file")
        print("4: Convert CSV to JSON")
        print("5: Exit")

        choice = input("Choose option: ")

        if choice == "1":  # Rewrite
            data = input_data()
            save_to_csv(data, mode="w")
        elif choice == "2":  # Add data to file
            data = input_data()
            save_to_csv(data, mode="a")  # Mode 'a' to add new lines
        elif choice == "3":  # Read CSV-file
            read_csv()
        elif choice == "4":  # Convert CSV to JSON
            csv_to_json()
        elif choice == "5":  # Exit
            print("Exit.")
            break
        else:
            print("Error.")


if __name__ == "__main__":
    main()
