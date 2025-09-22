#initialize an empty list for transactions
transactions = []

#define the main function
def main():
    # a while loop to display the menu
    while True :
        print('============== << MENU >>  ==============  ')
        print (f"\n 1.Add a new transaction \n 2.View Summary \n 3.View All transactions \n 4.Filter transactions by category"
               f" \n 5.Exit")
        try:
            choice = int(input("Hey ! please enter a number from the menu options:  "))
        except ValueError:
            print("Invalid input. Please enter a number from the menu :(1 to 6).")

        if choice == 1:
                print('adding new transaction!')
                add_transactions(transactions)
        elif choice == 2:
                results_summary = calculate_summary(transactions)
                display_report(results_summary)
        elif choice == 3:
                view_transactions(transactions)
        elif choice == 4:
                view_by_category(transactions)
        else :
            break
        print('==========================================')



#define an add_transactions function and add the logic of validation input to it , i pass the transactions as a parametr in the function so i could work with it without the urgent to declare it as a global ...
def add_transactions(transactions):
        #transaction_type validation
        while True   :
            transaction_type = input('Enter the transaction type: ')
            if transaction_type.lower() == 'income' or transaction_type.lower() == 'expense':
                break
            else :
                print("the type you entered is not valid ! try again and enter 'income' or 'expense'")
        #transaction_amount validation
        while True :
            transaction_amount = input('Please enter the transaction amount: ')
            try :
                amount = float(transaction_amount)
                if amount > 0 :
                    input_valid = True
                    print('transaction amount saved with success !')
                    break
                else :
                    print("Amount must be a positive number.")

            except :
                print("Invalid input. Please enter a numerical amount.")

        #store the category
        category = input('Enter the transaction category: ')

        #create the transaction dictionary
        transaction = {
            'type' : transaction_type.lower() ,
            'amount' : amount ,
            'category' : category ,
        }
        #add the transaction to the list of transactions
        transactions.append(transaction)
        print(f"transaction added ! {transaction_type.capitalize()} of {amount:.2f} in {category}")

#define a function to view the transactions
def view_transactions(transactions):
    #checking if there is any transactions before trying to display them
    if len(transactions) == 0 :
        print('No transactions to display !')
    else :
        print('=========== All Transactions =============')
        for transaction in transactions :
            print(f" {transaction['type'].capitalize()} :"
                  f" {transaction['category'].capitalize()} | ${transaction['amount']:.2f} ")

#define a filtering by category function
def view_by_category(transactions):
    #check if there is a transaction
    if transactions == [] :
        print('no transactions to display yet !')
    else :
        #store the input category
        user_category = input('please enter the category to filter by: ')
        category_filter = user_category.lower()
        found_transactions = False
        for transaction in transactions :
            #compare the input category with each category in the transaction
            category =  transaction['category']
            if category == category_filter :
                print(f" {transaction['type'].capitalize()} :"
                      f" {transaction['category'].capitalize()} | ${transaction['amount']:.2f} ")
                found_transactions = True
        #a message to display incase the input category not found
        if found_transactions == False :
            print('no transactions is done for the category:',category_filter)

#Define calculate_summary():
def calculate_summary(transactions):
    #Initialize Aggregators
    total_income = 0.0
    total_expense = 0.0
    #dictionary where keys are categories and values are the total expense for that category
    expenses_by_category = {}
    #Aggregate Totals and Categories:
    for transaction in transactions :
        if transaction['type'] == 'income':
            total_income += transaction['amount']
        elif transaction['type'] == 'expense':
            amount = transaction['amount']
            category = transaction['category']
            total_expense += amount
            # using the get method : get the value for the key; if key isn't found, it returns default_value instead.
            # gets the current sum for category (or 0.0 if it's new) and adds the amount to it, then updates the dictionary.
            expenses_by_category[category] = expenses_by_category.get(category, 0.0) + amount

    #Calculate Percentages of Total Expenses
    percentages_by_category = {}
    if total_expense <= 0 :
        print('No percentages can be calculated.')
    else :
        for category , amount in expenses_by_category.items() :
            percentage = (amount / total_expense) * 100
            percentages_by_category[category] = percentage
    results_summary = {
        'total_income' : total_income,
        'total_expense' : total_expense,
        'expenses_by_category' : expenses_by_category,
        'percentages_by_category' : percentages_by_category
    }
    return results_summary

#define a function to display the report
def display_report(results_summary) :
    total_income = results_summary['total_income']
    total_expense = results_summary['total_expense']
    net_savings = total_income - total_expense
    expenses_by_category = results_summary['expenses_by_category']
    percentages_by_category = results_summary['percentages_by_category']
    print("===== Financial Summary =====")
    print(f"Total Income:    ${total_income:>.2f}")
    print(f"Total Expenses: -${total_expense:>.2f}")
    print("-----------------------------")
    print(f"Net Savings:     ${net_savings:>.2f}")
    print("_" * 40)
    print("===== Expenses By Category =====")
    if total_expense <= 0 :
        print('No  expenses recorded!.')
    else :
        for category, amount in expenses_by_category.items():
            if category in percentages_by_category:
                perc = percentages_by_category[category]
                print(f"{category.capitalize():<15}: ${amount:>.2f} ({perc:.1f}%)")
            else :
                print(f"{category.capitalize()}: ${amount:.2f}")
    print("_" * 40)



#to always execute the main function i guess !
if __name__ == "__main__":
    main()







