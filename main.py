
import csv
import os

file_name = "patients.csv"


def setup():
    if not os.path.exists(file_name):
        f = open(file_name, "w", newline="")
        w = csv.writer(f)

        w.writerow(["Patient ID", "Name", "Age", "Gender",
                    "Disease", "Doctor", "Room"])

        f.close()


def add_patient():
    pid = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    disease = input("Enter disease: ")
    doctor = input("Enter doctor name: ")
    room = input("Enter room number: ")

    f = open(file_name, "a", newline="")
    w = csv.writer(f)

    w.writerow([pid, name, age, gender, disease, doctor, room])

    f.close()

    print("Patient added successfully.")


def show_patients():
    f = open(file_name, "r")
    data = csv.reader(f)

    for row in data:
        print(row)

    f.close()


def search_patient():
    pid = input("Enter patient ID: ")
    found = False

    f = open(file_name, "r")
    data = csv.DictReader(f)

    for row in data:
        if row["Patient ID"] == pid:
            print("\nPatient Details")
            print("ID:", row["Patient ID"])
            print("Name:", row["Name"])
            print("Age:", row["Age"])
            print("Gender:", row["Gender"])
            print("Disease:", row["Disease"])
            print("Doctor:", row["Doctor"])
            print("Room:", row["Room"])

            found = True
            break

    f.close()

    if found == False:
        print("Patient not found.")


def delete_patient():
    pid = input("Enter patient ID to delete: ")

    f = open(file_name, "r")
    data = list(csv.DictReader(f))
    f.close()

    new_data = []
    found = False

    for row in data:
        if row["Patient ID"] == pid:
            found = True
        else:
            new_data.append(row)

    if found:
        f = open(file_name, "w", newline="")
        fields = ["Patient ID", "Name", "Age", "Gender",
                  "Disease", "Doctor", "Room"]

        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(new_data)

        f.close()

        print("Patient deleted successfully.")
    else:
        print("Patient not found.")


setup()

while True:
    print("\n-------------------------------")
    print(" Hospital Patient Management")
    print("-------------------------------")
    print("1. Add Patient")
    print("2. Show Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        show_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        delete_patient()

    elif choice == "5":
        print("Program closed.")
        break

    else:
        print("Wrong choice. Please try again.")


