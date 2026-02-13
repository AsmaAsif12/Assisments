print("====================================")
print("   SMALL TUITION MANAGEMENT SYSTEM  ")
print("====================================")

# Student Inputs
student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
grade = input("Enter Grade (Playgroup / 1-3 / 4-6 / 7-10): ")

# Fee Structure
if grade == "Playgroup":
    fee = 2000
elif grade == "1-3":
    fee = 2500
elif grade == "4-6":
    fee = 3000
elif grade == "7-10":
    fee = 3500
else:
    fee = 0
    print("Invalid Grade Entered")

# Payment Status
payment = input("Fees Paid? (Yes / No): ")

# Output Section
print("\n------ Student Record ------")
print("Student ID:", student_id)
print("Name:", name)
print("Grade:", grade)
print("Monthly Fee:", fee)
print("Payment Status:", payment)

print("\nRecord Saved Successfully!")