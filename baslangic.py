print("hello \nworld")
print("--------------")
print("Hello \tworld")
print("--------------")
print("Benim adım {0}, yas {1}".format('Karahan',21))
print("Benim adım {1}, yas {0}".format('Karahan',21))
print("Benim adım {ad}, yas {yas}".format(ad='Karahan',yas=21))
n = [0,1,2,3,4]
for i in n:
    print(i**2) #üs alma.
txt = "hello world"
x = txt.strip() #baştaki ve sondaki boşluğu siler.
print(x)
y = txt.replace("h","J") #replace methodu, karakter değiştirmeye yarıyor.
print(y)
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"] 
fruits.update(more_fruits) #listeleri birbirine eklemeye yarıyor.
print(fruits)
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
