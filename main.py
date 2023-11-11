import csv

def avail_pets():
    print("***WELCOME TO PETSTORE*** \n\nWe currently have cats and dogs available for adoption.")
    animals = input('Please type one of the following options: \n1 for Cats Catalogue \n2 for Dogs Cataloge \n\nType your option now: ')
    
    user_option = ''
    if animals == '1':
        user_option = 'cats'
    else:
        user_option = 'dogs'

    with open(f"data/{user_option}.csv", newline='', encoding='utf-8') as f:
        animals_reader = csv.DictReader(f, skipinitialspace=True)
        print(f"\nSee the list below, of the {user_option} available for adoption \n\n" )
        for row in animals_reader:
            print(f"{row['name']} is {row['age']} years-old {row['breed']}")
        
avail_pets()