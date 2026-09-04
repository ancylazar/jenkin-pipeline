mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- Student Result ---")
print("Total:", total)
print("Average:", average)

# Pass criterion: Average must be 50 or above
if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")