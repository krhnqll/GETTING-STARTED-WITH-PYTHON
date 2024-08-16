from operator import truediv
import math

"""
def print_numbers1():
    for i in range(1, 6):
        for j in range(1, i+1):
            print(i, end=".")
        print()


print_numbers1()

print('"-"-"-"-"')
print("\\       \\")
print("/       /")
print("\\       \\")
print("/       /")
print("\\       \\")
print('"-"-"-"-"')

print("     A \\ or a /?")


def print_pyramid():
    k = 0
    rows = 6
    for i in range(1, rows+1):
        for space in range(0, (rows-i)+1):
            print(end=" ")

        while k != (2*i-1):
            print("*", end="")
            k += 1
        k = 0
        print()


print_pyramid()


def main():
    print("  *")
    print(" ***")
    print("*****")
    print("-----")
    print("-----")
    print(" ###")
    print(" ###")
    print("-----")
    print("-----")
    print()
    print("  *")
    print(" ***")
    print("*****")
    print("-----")
    print("-----")
    print(" ###")
    print(" ###")
    print()
    print("  *")
    print(" ***")
    print("*****")
    print(" ###")
    print(" ###")


main()


def print_numbers(num):

    for i in range(1, num+1):
        print("[", i, "]", end=" ")


print_numbers(15)


def first_digit(num):
    num_str = str(num)
    if (num >= 0):
        print(num_str[0])
    else:
        print(num_str[1])


first_digit(-3579)


def even_average():
    stop = 0
    while (not stop):
        input_guess = (int)(input())
        if (input_guess == stop):
            break
        else:
            even_sum = 0
            if (input_guess % 2 == 0):
                even_sum += input_guess
                evenAverage = even_sum / input_guess
                print(evenAverage)


print("Which is better?")
print("\tA \\ or a  /?")
print("/\\_/\\")
print(" . .")


def write():
    name_surname = input("What is your name? ")
    list = name_surname.split()
    first_name = list[0]
    last_name = list[1]

    print(first_name)
    print(last_name)

    print(first_name, ",",)


def print_wave():
    for i in range(-2, 7):
        for j in range(-1, i+2, 2):
            print("v", end='')
        print()
    for i in range(5, -3, -1):
        for j in range(-1, i+2, 2):
            print("v", end='')
        print()


def five_to_five():
    for i in range(-5, 6):
        print(i, end=" ")


five_to_five()


def squares():
    for i in range(1, 6):
        print(i*i, end=" ")


squares()


print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("|| FEAR THE TREE! ||")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


print("This program converts feet and inches to centimeters.")
feet = int(input("Enter number of feet: "))
inches  = int(input("Enter number of inches: "))
cm = (feet*30.48)+(2.54*inches)
print(feet,"ft",inches,"in = ", cm)

for i in range(1, 11):
    for j in range(1, 11-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print("")


for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end="")
    print("")


def circle_Area(num):
    area = (math.pi)*(num)*(num)
    print(area)


circle_Area(5)


def fraction_sum(num):
    total = 0
    for i in range(1, num+1):
        total += 1/i
    return total


word = "a"
while len(word) < 10:
    word = "b" + word + "b"
print(word)


def is_multiple(num1, num2):

    if (num1 % num2 == 0):
        return True
    else:
        return False


def carbonated(coke, soda, pop):
    print("say", soda, "not", pop, "or", coke)


def main():
    soda = "coke"
    pop = "pepsi"
    coke = "pop"
    pepsi = "soda"
    say = pop

    carbonated(coke, soda, pop)
    carbonated(pop, pepsi, pepsi)
    carbonated("pop", pop, "koolaid")
    carbonated(say, "say", pop)


main()


def mystery(x):
    y = 1
    z = 0
    while 2 * y <= x:
        y = y*2
        z += 1
    print(y, z)


mystery(1)
mystery(6)
mystery(19)
mystery(39)
mystery(74)


def coin_flip(k,side):
    count = 0
    text = "HT"
    if side not in text or k<0:
        print("ERROR!")
    else:
        while(count!=k):
            index=random.randint(0,len(text)-1)
            print(text[index],end=' ')
            if(text[index]==side):
                count+=1
            else:
                count=0
        print()
        print("You got " +side+' '+str(k)+" times in a row!")
    


def factorial(num):
    total_mult = 1
    for i in range(1, num+1):
        if num == 0 or num == 1:
            continue
        else:
            total_mult *= i
    print(num, "factorial = ", total_mult)


factorial(5)


def print_last_digit(num):
    print("Last digit of", num, str(num)[-1])


print_last_digit(3572)


def firs_digit(num):
    if num >= 0:
        return int(str(num)[0])
    else:
        return int(str(num)[1])


firs_digit(3572)
firs_digit(-947)


def first_digit(num):
    if math.fabs(num) < 10:
        return num
    else:
        return int(math.fabs(firs_digit(num / 10)))


def triangle(num):
    for i in range(1, num+1):
        print(" "*(num-i)+"*"*i)


triangle(6)


def sum_to(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i


def even_average():
    eventotal = 0
    evencount = 0


def even_sum_max():
    totalint = int(input("how many integers?"))
    sum = 0
    evenmax = 0
    for i in range(0, totalint):
        newint = int(input("next integer?"))
        if(newint % 2 ==0):
            sum+=newint
            if(evenmax<newint):
                evenmax = newint
        else:
            sum+=0    
    print("even sum =",sum)
    print("even max =",evenmax)

def days_in_month(num):
    first = 31
    second = 30 
    third = 28
    if (num > 0 and num <=12):
        if(num == 1 or num == 3 or num == 5 or num ==7 or num == 8 or num ==10 or num ==12):
            return first
        elif(num ==4 or num==6 or num ==9 or num == 11):
            return second
        else:
            return third
days_in_month(1)        

def main():
    twoline()
    threeline() 
    print()
    twoline()
    threeline()
    twoline()
    print()
    tline()
    twoline()
    threeline()
def twoline():
    print("*****\n*****")
def threeline():
    print(" * *")
    print("  *  ")
    print(" * *")
def tline():    
      print("  *")
      print("  *")
      print("  *")
            
main()


def biggest_and_smallest():
    num = int(input("How many nmubers? "))
    list = []
        
    for n in range(num):
        numbers = int(input("Next number? "))
        list.append(numbers)
    print("Biggest =",max(list))
    print("Smallest =",min(list))
        
biggest_and_smallest()        
        
        
def count_factors(n):
    arr = []
    for i in range(1, n + 1):
        if n % i == 0:   # a factor 
            arr.append(i)
            return len(arr)        
        



def even_average():
    count = 0
    even_sum = 0

    num = int(input("Integer? "))
    while (num != 0):
        if (num % 2 == 0):
            count += 1
            even_sum += num
        num = int(input("Integer? "))
    print("Average:", even_sum/count)


even_average()
"""

def name_game():
    name = str(input("What is your name? "))
    cut = name.split(" ")
    name_one = cut[0]
    name_two = cut[1]
    
    print(name_one.upper(),",",name_one.upper,",")
name_game()    
    
    