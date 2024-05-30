# lib/cli.py

from helpers import (
    exit_program,
    list_patients,
    find_patient_by_user_input,
    find_patient_by_id,
    create_patient,
    update_patient,
    delete_patient,
    list_doctors,
    find_doctor_by_name,
    find_doctor_by_id,
    create_doctor,
    update_doctor,
    delete_doctor,
    list_patient_doctors
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            patients()
        elif choice == "2":
            doctors()
        elif choice == "3":
            patient_doctors()
        else:
            print("Invalid choice")


def menu():
    print("Patient and Doctor Management System")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Patients")
    print("2. Doctors")
    print("3. Patient-Doctor Associations")

def patients():
    while True:
        patient_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_patients()
        elif choice == "2":
            find_patient_by_user_input()
        elif choice == "3":
            find_patient_by_id()
        elif choice == "4":
            create_patient()
        elif choice == "5":
            update_patient()
        elif choice == "6":
            delete_patient()
        else:
            print("Invalid choice")

def patient_options():
    print("Patient Options:")
    print("0. Back to main menu")
    print("1. List all patients")
    print("2. Find patient by name")
    print("3. Find patient by ID")
    print("4. Create new patient")
    print("5. Update patient")
    print("6. Delete patient")
    print("Please select an option:")

def doctors():
    while True:
        doctor_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_doctors()
        elif choice == "2":
            find_doctor_by_name()
        elif choice == "3":
            find_doctor_by_id()
        elif choice == "4":
            create_doctor()
        elif choice == "5":
            update_doctor()
        elif choice == "6":
            delete_doctor()
        else:
            print("Invalid choice")

def doctor_options():
    print("Doctor Options:")
    print("0. Back to main menu")
    print("1. List all doctors")
    print("2. Find doctor by name")
    print("3. Find doctor by ID")
    print("4. Create new doctor")
    print("5. Update doctor")
    print("6. Delete doctor")
    print("Please select an option:")

def patient_doctors():
    while True:
        patient_doctor_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_patient_doctors()
        else:
            print("Invalid choice")

def patient_doctor_options():
    print("Patient and Doctor Options:")
    print("0. Back to main menu")
    print("1. List patient doctors")
    print("Please select an option:")

if __name__ == "__main__":
    main()
