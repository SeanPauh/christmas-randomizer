#Welcome to my code for assigning random numbers to a list of names
#First we need to import the python randomizer library
import random

#Next we ask the user to give us the list of names that they would like to have numbers assigned to
input_string = input('Enter the names of those you would like to assign numbers to. Please separate the names by spaces.\n')
name_list = input_string.split( )
#print('Name list is', name_list)
#print(len(name_list))

#Now we ask them how high they want the list to go. This can be any number, within reason,
#and just provides and upper limit for the numbers
input_num = input('How high would you like the possible number to go to?\n')

#Area of improvement: Need to put a line in for if list given is less than number of names
int_input_num = int(input_num)
num_list = list(range(1, int_input_num + 1))
#print('List of numbers is:', num_list)
#print('number of elements:', len(num_list))

christmas_list = []
rand_list = []
i = 1
while i <= len(name_list):
    random_value = str(random.choice(num_list))
    if rand_list.count(random_value) > 0:
        random_value = str(random.choice(num_list))   
    rand_list.append(random_value)
    christmas_list.insert(i-1, name_list[i-1]+ ':'+ rand_list[i-1])
    i += 1
#print('List of randmized numbers is:',  rand_list)

print('Christmas List is:', christmas_list)