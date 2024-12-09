

def expense_add(): 
    enter_expense1 ={'amount':'£15.00', 'category':'beans' }
    show_expenses = [enter_expense1]
    enter_expense1 ={'amount':'£20.00', 'category':'CD-Rom' }
    show_expenses.append(enter_expense1)
   
def expenses_add(amount_expense, expense_category):
    expense_select ={'amount': amount_expense,'category': expense_category} 
    show_expenses.append(expense_select) # type: ignore
expense_add()
    
def expenses_list():
    print("expense list are displayed here ")
    count = 0
try:
    for expenses in show_expenses: # type: ignore
        print(count,"-", expenses['amount'],"-",expenses['category'] )
        count = count + 1
        print("\n")
except RuntimeError:
       print("this a runtime run time error , please click again to run")             
expenses_list() 
def category_list():
    print("category list are displayed here ")
    count = 0
try:
    for expenses in show_expenses: # type: ignore
        print(count,"-", expenses['category'] )
        count = count + 1
        print("\n")
               
except RuntimeError:
       print("this a runtime run time error , please click again to run")
       