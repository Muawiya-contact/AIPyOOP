# main.py

from aipyoop.interactive import start_learning
from aipyoop.refactor import refactor_code
from aipyoop.examples import Car

if __name__ == "__main__":
    print("🚀 AIPyOOP - Main Interface 🚀")
    print("Choose a mode:")
    print("1. Interactive Learning")
    print("2. Refactor & Improve Existing Code")
    print("3. Run Pre-Built Example")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        start_learning()
    elif choice == "2":
        path = input("Enter the path to your Python file: ")
        refactor_code(path)
    elif choice == "3":
        my_car = Car("Toyota", "Corolla", 2023)
        print("Pre-Built Example Output:\n", my_car)
    else:
        print("Invalid choice. Exiting.")
