total_expense = 0
expenses = []
range_value = int(input("enter the total number of expenses"))
for i in range(range_value):
    expenses.append(float(input("enter the expenses")))

total_expense = sum(expenses)
print("total expense "+ str(total_expense))