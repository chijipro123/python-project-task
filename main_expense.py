import expense_project
# create the welcome display screen menu option
      
print("how much are the expenses made?")
try:
        enter_amount = int(input(">")) 
except  ValueError: 
        print("wrong input, please try again ")
except ZeroDivisionError:
        print("Error: do not enter zero")

print("On which category was expenses made?")
try:
       enter_category = input(">") 
except ValueError: 
        print("wrong input, please try again ")

expense_project.expenses_add(enter_amount, enter_category)
#list of all expenses
expense_project.expenses_list()
expense_project.category_list()              