
def expenses_add(enter_amount, enter_category,enter_description):
    show_expenses ={'amount': enter_amount,'category':enter_category,'description':enter_description} 
    show_expenses.update(show_expenses)
    
def category_list(show_expenses):
    rs = show_expenses.get('category')  
    print(rs)
    
def list_expenses(show_expenses):
    ks = show_expenses.keys() 
    for expenses in sorted(ks):
       print(expenses,show_expenses[expenses])
       print("\n")

       
def expense_value(show_expenses):
   for P_expenses in show_expenses:
      category = show_expenses[P_expenses]
      print(category)

