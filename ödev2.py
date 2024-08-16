"""
import random
counter = 0
gamecounter = 0
n = random.randint(1, 100)
print("This program allows you to guess random numbers.")
print("I will think of a number between 1 and 100")
print("and you will try to guess it.")
print("After each guess, I will give you a clue about")
print("whether the correct number is higher or lower.")
print()
print("I'm thinking of a number between 1 and 100...")
guess = int(input("Your guess? "))
if guess < n:
    print("It's lower.")
    counter += 1
    guess = int(input("Your guess? "))
elif guess > n:
    print("It's higher.")
    counter += 1
    guess = int(input("Your guess? "))
else:
    gamecounter += 1
    print("You got it right in {} guesses!".format(counter))
again = input("Do you want to play again? ")

if again.upper() == "Y" or again.upper() == "YES":
    n = random.randint(1, 100)
    while n != guess:
        counter += 1
        if guess < n:
            print("It's lower.")
            guess = int(input("Your guess? "))
        elif guess > n:
            print("It's higher.")
            guess = int(input("Your guess? "))
        else:
            break
    print("You got it right in {} guesses!".format(counter))
"""
"""
    def scale_by_k(list):
        length = len(list)
        newList = []
        
        for i in range(length):
            if list[i] <= 0:
                continue 
            else:
                for j in range(list[i]):
                    newList.append(list[i])
        print(newList) 
"""
"""

def collapse_pairs(lst):
    for i in range(0, len(lst), 2):
        # Add the pair of numbers
        sum_of_pair = lst[i] + lst[i+1]

        # Replace the pair of numbers with the sum
        if sum_of_pair % 2 == 0:
            lst[i] = sum_of_pair
            lst[i+1] = 0
        else:
            lst[i] = 0
            lst[i+1] = sum_of_pair
"""
"""
def contains(a1, a2):
    # Iterate over all possible starting positions in a1
    for i in range(len(a1) - len(a2) + 1):
        # Check if the sequence at this starting position matches a2
        matches = True
        for j in range(len(a2)):
            if a1[i+j] != a2[j]:
                matches = False
                break
        if matches:
            return True
    return False
"""
"""
def count_duplicates(lst):
    
    seen = set()
    
    count = 0

    
    for i in lst:
        
        if i in seen:
           
            count += 1
        else:
            
            seen.add(i)

   
    return count
"""

"""
def find_range(list):

    min_value = min(list)
    max_value = max(list)
    average = max_value - min_value + 1

    if len(list) == 1:
        return average
    else:
        return abs(average)

"""

"""
def flip_half(lst):
    # Get the length of the list
    n = len(lst)

    # Create a copy of the list to use as auxiliary storage
    aux = lst[:]

    # Iterate over the elements in the list
    for i in range(n):
        # Check if the current index is odd
        if i % 2 == 1:
            # If it is, reverse the order of the element at the current index
            # by swapping it with the element at the corresponding position in
            # the auxiliary list
            lst[i] = aux[n - i - 1]
"""
"""
def split(list):
    new_list = []
    
    for i in range(len(list)):
        if list[i] % 2 == 0:
            new_list.append(list[i] // 2)
            new_list.append(list[i] // 2)
        else:
            new_list.append((list[i] // 2)+1)    
            new_list.append(list[i] // 2)
    return new_list        
""" 
""" 

def get_percent_even(list):
    if len(list) == 0:
        return 0.0
    else:
        num_even =  sum(1 for i in list if i % 2 == 0)
        num_total = len(list)
        return 100 * num_even / num_total                
"""
  
def num_in_common(list1, list2):
    
    unique_ints = set()
    
    for num in list1:
        unique_ints.add(num)
  
    for num in list2:
        unique_ints.add(num)

    return len(unique_ints)

