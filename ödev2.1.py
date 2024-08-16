"""
def max_value(list):
    num = list[0]
    for i in range(len(list)+1):
        if list[i] > num:
            num = list[i]
            
    return num
"""
"""
def mean(list):
    length = len(list)
    sum = 0
    
    if length == 0 :
        return 0.0
    else:
        for i in range(length):
            sum +=list[i]
        average = sum / length
        return average    
""" 
""" 
def print_list(list):
    for i in range(len(list)):
        print("element [{}] is {}".format(i,list[i]))
""" 
""" 
def sorted(list):
    list2 = list.copy()
    list2.sort()
    if len(list) == 1:
        return True
    
    if list == list2:
        return True
    else:
        return False
""" 
""" 
def mirror(list):
    lst = list.copy()
    lst.reverse()
    print(list.extend(lst))
""" 
""" 
print("+---+")
for i in range(1,4):
    print("\\   /")
    print("/   \\")
print("+---+")
""" 
""" 
def n_copies(list):
    length = len(list)
    newList = []
    
    for i in range(length):
        if list[i] <= 0:
            continue 
        else:
            for j in range(list[i]):
                newList.append(list[i])
    return newList  
""" 
""" 
def  remove_even_length(list):
    
    for i in range(len(list)):
        if len(list[i]) % 2 == 0:
            list.remove(list[i])
        else:
            continue    
        print(list)    
        
remove_even_length((['This', 'is', 'a', 'test']))       
""" 
""" 
def index_of(list,num):
    if not num in list:
        return -1
    else:
         for i in range(len(list)):
             if list[i] == num:
                 return list.index(list[i])
"""
"""
def stutter(word):
	word.insert()  
stutter([17, -4, 0, 212, 212, 8468])
"""
"""
def find_median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None
    
find_median([5, 2, 4, 17, 55, 4, 3, 26, 18, 2, 17])
"""
"""
def collection_mystery2(map1,map2):
    result = {}
    for s1 in map1.keys():
        if map1[s1] in map2:
            result[s1] = map2[map1[s1]]
    return result

        
map1 = {'bar': 1, 'baz': 2, 'foo': 3, 'mumble': 4}
map2 = {1: 'earth', 2: 'wind', 3: 'air', 4: 'fire'}
map3 = {'five': 105, 'four': 104, 'one': 101, 'six': 106, 'three': 103, 'two': 102}    
map4 = {99: 'uno', 101: 'dos', 103: 'tres', 105: 'cuatro'}    
map5 = {'a': 42, 'b': 9, 'c': 7, 'd': 15, 'e': 11, 'f': 24, 'g': 7} 
map6 = {1: 'four', 3: 'score', 5: 'and', 7: 'seven', 9: 'years', 11: 'ago'}
collection_mystery2(map1,map2)
collection_mystery2(map3,map4)
collection_mystery2(map5,map6)
"""