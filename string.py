#1 For loop 
for x in "Fahad":
    print(x)

#2 string length
a="AEIOU"
print("Length of string = ",len(a))

#3 check string
txt="Hello whatsapp ! "
print("!" in txt)  # if the world is avilble it will return True else False
txt="Hey there "
print("Hello " not in txt)

#4 Upper & Lower case Letter
p="Hello World "
print(p.upper())
print(p.lower())

#5 Remove white space from Start & End
x="                 U Need Any Help !"
print(x.strip())

#6 Replace String 
y="Pakistan"
print(y.replace("k","t"))

#7 Split String
y="Hey Dude"
print(y.split())

#8 string concatenation  or to combine two strings
a="Fahad"
b="khan"
c=a+" "+b  # To add space 
print(c)

#9 String Format
age=19
txt="My name is Fahad , I am {}"
print(txt.format(age))
