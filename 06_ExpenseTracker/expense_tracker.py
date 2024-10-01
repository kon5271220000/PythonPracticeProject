from expense import expense

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


def main():
    #1)ask for input
    expense = get_user_input_expense()
    print(expense)
    #2)write to file
    #3)show summary

if __name__ == "__main__":
    main()