
#    Checks if the provided string value is 'end' (case-insensitive).
#    Returns True if the value is 'end', otherwise returns False.

def Is_end(value):
    if (value.lower() == "end"):
        return True
    return False



#    Checks if the provided string value is a valid arithmetic operator.
#    Valid operators are '+', '-', '*', '/'.
#    Returns True if the value is not a valid operator, otherwise returns False.

def Check_false_operator(value):
   valid_operators = ['+','*','/','-']
   if value not in valid_operators:
        return True
   return False 



#    Checks if the provided string value is a key in the provided dictionary.
#    Returns True if the value is not a key in the dictionary, otherwise returns False.

def Check_false_category(value,categ_dict):
    if value not in categ_dict:
        return True
    return False




#################### CREATING NEW ACCOUNTING FILE ####################   
def Create_new_file(month):
    Categories_dict = Get_Std_In_Input()
    Write_to_file(Categories_dict,month)



#    Interactive function to create a new accounting dictionary from user input.
#    Allows users to add categories and values, and modify existing categories.
#    Continues to prompt the user until 'end' is entered.
#    Returns a dictionary of categories with their corresponding values.

def Get_Std_In_Input():
    Categories = {'sasa': 0.0, 'jedlo': 0.0, 'ine_veci': 0.0, 'intrak': 0.0}
    Cat = "start"
    while Cat != "end":
        Cat = input("Enter category of an expense: ").lower()
        if Cat == "end":
            break
        
        elif Cat in Categories:
            print(f"Add to category: {Cat}")
            read = input("Continue or End: ")
            while read != "end":
                read = input()

                if (read.lower() == "end"): break

                if read.lower() == "help":
                    print("To end input: end")
                    print("To add values, write solid int")
                    print("To continue input, write: cont")
                    reader = input()
                    if reader.lower() == "cont":
                        continue
                    if reader.lower() == "end":
                        break
                    else: continue

                try:
                    Categories[Cat] += float(read.strip())
                except:
                    print("Invalid Format")
                    
        

        elif Cat not in Categories:
            Categories[Cat] = 0
    Categories["sasa"] /= 2.0
    return Categories
#################### CREATING NEW ACCOUNTING FILE ####################   

#################### EDITING ACCOUNTING FILE ####################
def Edit_a_file(month):
    edit = input("Which file would you like to change (*.txt): ")
    Categories_dict = Read_file_to_dict(edit)
    Edited_Categories_dict = Edit_expences(Categories_dict)
    month = month + "_edit"
    Write_to_file(Edited_Categories_dict,month)


#    Reads an accounting file and converts it into a dictionary.
#    The file format expected is 'key : value'.
#   Skips lines that are not in the expected format.
#    Returns the dictionary created from the file.

def Read_file_to_dict(file_name):
    result = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            
            if len(parts) == 2:
                key = parts[0].strip()
                try:
                    value = float(parts[1].strip())
                    result[key] = value
                except ValueError:
                    print(f"Skipping line: {line.strip()}")
    result.pop("Celkovo bez vlastnych veci")
    return result



#    Prints all categories and their values from the provided dictionary.
#   Used to display the current state of the accounting dictionary.

def Print_all_categories(c_dict):
    print()
    print("Possible categories to edit: ")
    for key , value in c_dict.items():
        print(f"{key} : {value}")



#    Allows for interactive editing of the provided categories dictionary.
#    Users can choose a category and apply arithmetic operations to its value.
#   Continues to prompt for edits until 'end' is entered.
#    Returns the modified dictionary.

def Edit_expences(categories):
    result = categories
    categ = "Start"

    while categ != "end":
        Print_all_categories(result)
        
        categ = input("Category to edit or end: ").lower()
        if Check_false_category(categ,result): 
            print("Invalid Category name.")
            continue
        if Is_end(categ): break
        
        difference_value_operator = input(f"How would you like to edit value of {categ}: ").strip()

        if (Check_false_operator(difference_value_operator)):
            print("Invalid operator, valid Operators: + - * / ")
            continue

        difference_value = float(input(f"By how much: "))

        if (difference_value_operator == "-"):
            result[categ] -= difference_value
        
        elif (difference_value_operator == "*"):
            result[categ] *= difference_value
        
        elif (difference_value_operator == "/"):
            result[categ] /= difference_value
        
        elif (difference_value_operator == "+"):
            result[categ] += difference_value
        
        else:
            print("Wrong operator given.")
            break


    return result
#################### EDITING ACCOUNTING FILE ####################


#    Writes the contents of the provided categories dictionary to a file.
#    The file is named based on the provided month string.
#    Each category is written in the format 'key : value'.
#    Also calculates and writes the total value excluding 'vlastne'.

def Write_to_file(category_dict,month):
    with open(f'{month}.txt','w') as file:
        total = 0.0
        for key , value in category_dict.items():
            file.write(f"{key} : {value}")
            if key != "vlastne":
                total += value
            file.write('\n')
        file.write('\n')
        file.write(f"Celkovo bez vlastnych veci: {total}")




edit_or_create = input("Do you want to Edit existing file or Create a new one: ").lower()
m = input("Month of accounting: ").lower()
if (edit_or_create == "create"):
    Create_new_file(m)

elif (edit_or_create == "edit"):
    Edit_a_file(m)

else: print("Invalid command.")