
import expense_project
# create the welcome display screen menu option     
print("how much are the expenses made?")
try:
        enter_amount = int(input(">")) 
except  ValueError: 
        print("wrong input, please try again ")
except ZeroDivisionError:
        print("Error: do not enter zero")
        print("\n")
        
print("On which category was expenses made?")
try:
       enter_category = input(">") 
except ValueError: 
        print("wrong input, please try again ")
        print("\n")
        
print ("Enter a brief description of expenses made")
try:
       enter_description = input(">") 
except ValueError: 
        print("wrong input, please try again ")
        print("\n")
        

expense_project.expenses_add(enter_amount, enter_category,enter_description)

expense_project.expense_value(show_expenses= {'amount': enter_amount,'category':enter_category,'description':enter_description})
expense_project.category_list(show_expenses={'amount': enter_amount,'category':enter_category,'description':enter_description})
expense_project.list_expenses(show_expenses={'amount': enter_amount,'category':enter_category,'description':enter_description})