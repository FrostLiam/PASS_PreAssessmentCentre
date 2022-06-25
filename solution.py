shopping_list = []

#############################################
# This code is an example of the functions they will be writing (Step 2)

def add_to_list(item):
  shopping_list.append(item)
  return

def remove_from_list(item):
  shopping_list.remove(item)
  return

def print_list():
  print("Shopping list contains:")
  for item in shopping_list:
    print(item)
    
#############################################
    
if __name__ == "__main__":
  # function calls go here
  # e.g. run_function_1()

#############################################
# This code is an example of the tests that will be written (Step 3)
  
  add_to_list("Eggs")
  print_list()
  add_to_list("Flour")
  print_list()
  remove_from_list("Eggs")
  print_list()

#############################################