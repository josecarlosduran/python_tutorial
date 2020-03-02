myString = "This is a string"
myString2 = "This_is_a_string"
allLetters ="AFSFSF"

#print(dir(myString))

print(myString.upper())
print(myString.lower())
print(myString.swapcase())
print(myString.capitalize())
print(myString.replace("string","replaced string").upper())
print(myString.count("i"))
print(myString.startswith("This"))
print(myString.endswith("string"))

print(myString.split())
myList = myString2.split("_")
print(myList)
print(type(myList))

print(myString.find("a"))
print(myString.find("string"))
print(len(myString))
print(myString.isalnum())
print(myString.isnumeric())

print(allLetters.isalpha())
print(myString[5])
print(myString[-1])


#another form of concatenate

name = "Josep"

print ("My name is " + name)
print (f"My name is {name}")
print("My name is {0}".format(name))

