from cmath import exp
from datetime import date
import csv
from fileinput import filename


today = date.today()
today = today.strftime("%d/%m/%Y")
filename = "test.csv"
expense = []
stopped = False

with open(filename, "a", newline="") as file:
    csvwriter = csv.writer(file)

    while not stopped:
        user_input = int(input("What is the expense (type 0 to stop): "))
        if user_input == 0:
            stopped = True
        else:
            csvwriter.writerow([today, user_input])
            expense.append(user_input)

file.close()

print("Your expenses today are:", expense)
print("The total is: ", sum(expense))