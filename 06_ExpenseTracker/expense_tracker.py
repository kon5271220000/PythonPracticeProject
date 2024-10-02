from expense import expense
import datetime
import calendar

def get_user_input_expense():
    print("Get user expense: ")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"{expense_name}, {expense_amount}")

    expense_categories = ["Food", "Home", "Work", "Fun", "Misc"]

    while True:
        print("Choose expense categorie: ")
        i = 1;
        for categorie in expense_categories:
            print(f"{i}. {categorie}")
            i += 1

        expense_categorie = int(input("Enter expense categorie index: "))
        
        if 1 <= expense_categorie <= len(expense_categories):
            new_expense = expense(expense_name, expense_categories[expense_categorie-1], expense_amount)
        else:
            print("your category index's not valid, please try again")
            print("you can only choose frome 1 to " + str(len(expense_categories)))
            expense_categorie = int(input("Enter expense categorie index: "))
            new_expense = expense(expense_name, expense_categories[expense_categorie-1], expense_amount)
        
        return new_expense
    
def write_to_file(expense, filename):
    print(f"save \n{expense} \nto {filename}")
    with open(filename, "a") as file:
        file.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

def summary_user_expense(filename, budget):
    print("summary user expense")
    expenses = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            expense_name, expense_amount, expense_categroy = line.strip().split(",")
            line_expense = expense(expense_name, expense_categroy, float(expense_amount))
            expenses.append(line_expense)

    amount_per_category = {}
    for exp in expenses:
        key = exp.category
        print(key)
        if key in amount_per_category:
            amount_per_category[key] += exp.amount
            print(exp.amount)
        else:
            amount_per_category[key] = exp.amount
    
    for key in amount_per_category:
        print(f"{key} : ${amount_per_category[key]}\n")
    
    total_spent = sum([exp.amount for exp in expenses])
    print(f"your total spent: ${total_spent}")

    remaining_budget = budget - total_spent
    print(f"your budget remaining: ${remaining_budget}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"remaing day in month {remaining_days}")
    
    daily_budget = (budget-total_spent)/remaining_days
    print(f"your daily budget: ${daily_budget}")
    
    

   


def main():

    budget = 2000
    file_name = "06_ExpenseTracker/data.csv"

    #1)ask for input
    expense = get_user_input_expense()

    #2)write to file
    write_to_file(expense, file_name)

    #3)show summary
    summary_user_expense(file_name, budget)

if __name__ == "__main__":
    main()