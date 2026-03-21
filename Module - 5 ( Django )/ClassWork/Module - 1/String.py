'''
String = Sequence of characters, enclosed in quotes.
'''

#Length : Gives the length of string
str1="Mohit Sharma"
print("Length : ",len(str1))

#Lower : Convert the string in lower
print("Lower : ",str1.lower())

#Casefold : Convert string strictly to lower including special character
str2 = "Mohit Sharma ß"
print("Casefold : ",str2.casefold())

#upper : Convert the string to upper case
print("Upper : ",str1.upper())

#title : Convert the first Character of all words in sentence to upper case
print("Title : ",str1.title())

#capitalize : Convert the first Character of first word in sentence to upper case
print("Capitalize : ",str1.capitalize())

#Strip : Remove all the leading and trailing spaces
str3 = "   Mohit Sharma    "
print("strip : ",str3.strip())

#Replace : Replace the partcular character.
print("Replace : ",str1.replace('h','T',2))

#Find : Gives the index of perticular character
print("Find : ",str1.find('h'))

#index : Gives the index of the particular letter
print("Index : ",str1.index('a'))

#Startswith : 
print("Startswith M : ",str1.startswith('M'))
print("Startswith N : ",str1.startswith('N'))

#Endswith
print("Endswith a ",str1.endswith('a'))
print("Endswith P ",str1.endswith('P'))

#Split : Split the string with particular character and gives list
str5="Sun rises from east"
print("Split : ",str5.split("s",2))

#join : Join the 2 string
print("abc".join("xyz"))

#isalpha
print("abc".isalpha())

#isdigit
print("123sd".isdigit())

#isalnum
print("abc123".isalnum())
print("abc".isalnum())
print("abc123#".isalnum())

#zfill : Fill the string with 0 
print("abc".zfill(10))

#center : 
print("abc".center(15,"*"))
print("abc".center(16,"*"))

#string Slicing
str1 = "Sun rises from east"

print("1 : ",str1[2:])
print("2 : ",str1[2:7])
print("3 : ",str1[2:15:2])
print("4 : ",str1[:8])
print("5 : ",str1[-4:-1])
print("6 : ",str1[::-1])