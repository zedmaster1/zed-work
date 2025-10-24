import os

class Student:
    def __init__(self, name="", fathername="", birthdate="", codemelli="", phone="", address=""):
        self.name = name
        self.fathername = fathername
        self.birthdate = birthdate
        self.codemelli = codemelli
        self.phone = phone
        self.address = address

    def registerstudent(self):
        self.name = input("Enter the full name: ")
        self.fathername = input("Enter the father name: ")
        self.birthdate = input("Enter the birthdate (YYYY-MM-DD): ")
        self.codemelli = input("Enter the codemelli: ")
        self.phone = input("Enter the phone: ")
        self.address = input("Enter the address: ")

        filename = f"file-{self.codemelli}.txt"

        with open(filename, "w") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Father Name: {self.fathername}\n")
            f.write(f"Birthdate: {self.birthdate}\n")
            f.write(f"Code Melli: {self.codemelli}\n")
            f.write(f"Phone: {self.phone}\n")
            f.write(f"Address: {self.address}\n")

        print(f"✅ Student '{self.name}' registered successfully.\n")

    def printform(self):
        codemelli = input("Enter the student's Code Melli to view: ")
        filename = f"file-{codemelli}.txt"

        if os.path.exists(filename):
            with open(filename, "r") as f:
                print("\n--- Student Information ---")
                print(f.read())
                print("---------------------------\n")
        else:
            print("❌ No record found.\n")

    def removestudent(self):
        codemelli = input("Enter the student's Code Melli to remove: ")
        filename = f"file-{codemelli}.txt"

        if os.path.exists(filename):
            os.remove(filename)
            print("🗑️ Student record removed successfully.\n")
        else:
            print("❌ Record not found.\n")

    def editstudent(self):
        codemelli = input("Enter the student's Code Melli to edit: ")
        filename = f"file-{codemelli}.txt"

        if os.path.exists(filename):
            print("Enter new details (leave blank to keep current):")

            with open(filename, "r") as f:
                data = f.readlines()

            info = {line.split(": ")[0]: line.split(": ")[1].strip() for line in data}

            for field in info.keys():
                new_value = input(f"{field} ({info[field]}): ")
                if new_value:
                    info[field] = new_value
                    if field == "Code Melli":
                       changefilename = new_value

            with open(filename, "w") as f:
                for k, v in info.items():
                    f.write(f"{k}: {v}\n")
            f.close()

            
            if changefilename and changefilename != codemelli:
                new_filename = f"file-{changefilename}.txt"
                os.rename(filename, new_filename)
            
            print("✏️ Student record updated successfully.\n")
        else:
            print("❌ Record not found.\n")


def mainstudent():
    s = Student()
    while True:
        print("1. Register Student")
        print("2. Print Form")
        print("3. Remove Student")
        print("4. Edit Student")
        print("5. EXIT")

        try:
            b = int(input("\nEnter your choice: "))
        except ValueError:
            print("⚠️ Please enter a valid number.\n")
            continue

        if b == 1:
            s.registerstudent()
        elif b == 2:
            s.printform()
        elif b == 3:
            s.removestudent()
        elif b == 4:
            s.editstudent()
        elif b == 5:
            print("👋 Exiting program.")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")


if __name__ == "__main__":
    mainstudent()

