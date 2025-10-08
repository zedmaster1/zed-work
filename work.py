
"""
r = 12

b = 6

print(r+b)

if b > r :
  print("print b is grea")
else : 
  print("r is graet")



x = "awaesome"

def myfunk(y,x):
 print("python is " + x + " and " + y)

x = "great"
myfunk("good",x)





b = ("Hello World")

#print(b[:8])

#print(b[-7:-2])

print(b.lower())



name = "parsa"

age = 12

txt = f"my name is {name},i am {age}"

print(txt)





txt = f"my pris is {20 + 31}"
print(txt) end
jlase 2




mylist = ["apple","orange","bananas","chery"]

print(len(mylist))





parsalist = ["apple", "oranges", "bananas"]

parsalist[2] = "coconat"

print(parsalist)





parsalist = ["apple", "bananas"]
parsalist2 =["papaye", "piapple"]

parsalist.extend(parsalist2)

print(parsalist)








thislist = ["apple", "bananas", "chery"]

for i in range(len(thislist)):
    print(thislist[i])
    #print(len(thislist))



thislist = ["apple", "bananas", "oranges"]

i = 0

while i < len(thislist):
    print(thislist[i])
    i =i +1

    #end class 2

    



thislist = {"apple", "bananas", "chery"}

x = thislist.pop()

print(x)

print(thislist)






mycar = {
        "car":"dorg",
         "model":"chalenger",
         "year": 2024,
         "color":["blue","red","green"]
        }

print(mycar)










a = 20

b = 1

if b > a :
  print("b big greaf a")
elif a > b :
  print("a small b")
else :
  print("a and b is acoal")
  



a = 2

b =132

print("a") if a > b else print("b")









a = 350
b = 153
c = 432

if a > b and c > a :
  print ("all True")




a = 350
b = 153
c = 43

if a > b or c > a :
 print("all true")

 

day = 6
match day :
    case 1|2|3|4|5|6|7|8 :
        print("all day good")

    case 6|7 :  
       print("day chemg")



 

p = 0
while p < 50 :
    print(p)
    p += 2


print("enter your name")

name = input()

print(f"hello {name}")


    
    


p =7 

def parsa(haji) :
  haji += 10
  print (f"your result is: {haji}")

print("enter two number")
x = input()
y = input()
haji = int(x) + int(y)
parsa(haji)




print ("enter your number") 
x = input()
i = 1

while i <= int(x) :
    if(i % 2 == 0) :
        print(i)
    i += 1


    




x = range(11 ,50,2)

print(x)


print(list(x))

    

print("enter a number")
x = input()
y = lambda x : x *  10




print(y(intp(x)))


"""

class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myplus(self,x) :
    return (x + self.age)  
  
  def mymines(self,x) :
    return (x + self.age)  


p1 = person("jomt", 36)

print(f"my name is {p1.name} i am {p1.myplus(4)}year old")
print(f"my name is {p1.name} i am {p1.mymines(3)}year old")
