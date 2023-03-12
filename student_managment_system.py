def add_person(my_list, full_name):
    my_list.append(full_name)

def add_many_person(my_list, person):
    my_list.extend(person)

def delete_person(my_list, full_name):
    my_list.remove(full_name)

def delete_many_person(my_list, *args):
    my_new_list = list()
    add_many_person(my_new_list, list(args))

    for person in my_new_list:
        my_list.remove(person)

def display_person(my_list):
    count = 0
    while count < len(my_list):
        print(f"{count + 1}. person {my_list[count]}")
        count += 1
    # We can display the whole variable inside of my list with "for" or "while" loops. I showed both way.
    '''
    for index in range(len(my_list)):
        print(f"{index + 1}. person {my_list[index]}")
    '''


my_person_list = list()

add_person(my_person_list, "Ben Simmons")
add_many_person(my_person_list, ["Derrick Rose", "Kevin Durant", "Micheal Jordan", "Lebron James"])

delete_person(my_person_list, "Ben Simmons")
delete_many_person(my_person_list, "Derrick Rose", "Kevin Durant")

display_person(my_person_list)