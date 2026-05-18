print("=== Employee Performance Evaluation System ===\n")

name = input("Enter employee name: ")

attendance = int(input("Enter attendance percentage: "))
quality = int(input("Enter work quality marks (out of 10): "))
teamwork = int(input("Enter teamwork marks (out of 10): "))
punctuality = int(input("Enter punctuality marks (out of 10): "))

# Calculate total score
total = quality + teamwork + punctuality

# Expert System Rules
if attendance >= 90 and total >= 24:
    performance = "Excellent"
    bonus = 10000

elif attendance >= 75 and total >= 18:
    performance = "Good"
    bonus = 5000

elif attendance >= 60 and total >= 12:
    performance = "Average"
    bonus = 2000

else:
    performance = "Poor"
    bonus = 0


# Display Report
print("\n===== Employee Report =====")
print("Employee Name :", name)
print("Attendance    :", attendance, "%")
print("Total Score   :", total, "/30")
print("Performance   :", performance)
print("Bonus Amount  :", bonus)