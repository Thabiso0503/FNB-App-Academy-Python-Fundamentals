# we  want to build a student grade classifier

# it must take a learner's name and marks for three subjects

name =input("Enter your name: ")

subject_1 = float(input("Enter your mark :"))
subject_2 =float(input("Enter your mark :"))
subject_3 =float(input("Enter your mark :"))

# Calculate average
avg = (subject_1 + subject_2 + subject_3)/3.0

# Assign letter grade
if avg >=80 :
    grade = "A"
elif 70 <= avg <= 79:
    grade = "B"
elif 60 <= avg <= 69:
    grade = "C"
elif 50 <= avg <= 59:
    grade = "D"
elif avg < 50:
    grade = "F"

# Assign pass status
if avg >= 50:
    status = "Pass"
else:
    status = "Fail"


# Check for intervention
print(status)


intervention = ""

if subject_1 < 40:
    intervention += "Subject 1 needs intervention\n"

if subject_2 < 40:
    intervention += "Subject 2 needs intervention\n"

if subject_3 < 40:
    intervention += "Subject 3 needs intervention\n"

if intervention == "":
    intervention = "No intervention required"
    
# Display report card
print("\n========== REPORT CARD ==========")
print(f"Learner Name : {name}")
print(f"Subject 1    : {subject_1}")
print(f"Subject 2    : {subject_2}")
print(f"Subject 3    : {subject_3}")
print(f"Average      : {avg:.2f}")
print(f"Grade        : {grade}")
print(f"Status       : {status}")
print("\nIntervention:")
print(intervention)
