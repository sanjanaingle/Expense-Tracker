import csv
import matplotlib.pyplot as plt

total_expense = 0
dates = []
daily_total = []

current_day_total = 0
current_date = ""

with open("expenses.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        date = row[0]
        amount = int(row[2])

        total_expense += amount

        if date != current_date:
            if current_date != "":
                dates.append(current_date)
                daily_total.append(current_day_total)

            current_date = date
            current_day_total = amount
        else:
            current_day_total += amount

    dates.append(current_date)
    daily_total.append(current_day_total)

# assume income
income = 2000
savings = income - total_expense

print("Total Expense:", total_expense)
print("Income:", income)
print("Savings:", savings)

# line graph
plt.plot(dates, daily_total)

plt.title("Daily Expense Trend")
plt.xlabel("Date")
plt.ylabel("Amount")

plt.show()