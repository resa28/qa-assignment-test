import requests
import csv

URL = "https://reqres.in/api/users?page=2"
CSV_FILE = "users.csv"


def fetch_users():
    response = requests.get(URL)
    response.raise_for_status()  # error kalau gagal
    return response.json()["data"]


def save_to_csv(users):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["email", "first_name", "last_name"])  # header

        for user in users:
            writer.writerow([user["email"], user["first_name"], user["last_name"]])


def main():
    users = fetch_users()
    save_to_csv(users)
    print(f"CSV berhasil dibuat: {CSV_FILE}")


if __name__ == "__main__":
    main()
