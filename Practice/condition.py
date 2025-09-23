# # age1=int(input("Enter your age:"))
# # age2=int(input("enter ur fri ange"))
# # if age1 < age2: 
# #     print("your age is younger than your friend")
# # else : 
# #     print("your friend is younger than you ")
# #     print("your friend is younger than you by", age1-age2)
# # print("goodbye")

# sentence=input("Enter the sentence:")
# word_count=(sentence.count(" ") +1)
# if word_count<3:
#     print("Your sentence is too short")
# elif 3<= word_count<=8:
#     print("your sentence is good")
# else :
#      print("yoursentec is too long")
#x=4
# y=4
# z=4
# if x<z or y==z:
#     if x!=y or x==z:
#         print('hello')
#         x=x+2
#         y=x+1
#     else: print("hi")
# if y<x and x>z:
#     print("nay")
    
# else: print("yays")
# phrase1 ='Orange'
# phrase2 = 'orange'
# if phrase1[1:4] == phrase2[1:4]:
# 	if phrase1[4] > phrase2[4]:
# 		print('Hello')
# 	else:
# 		print('Hi')
# else:
# 	print('Good morning')
# print('Goodbye')
# temp1 = 30
# temp2 = 45
# temp3 = 60
# if temp1 < temp2 and temp3 == temp2:
# 	print('Hello')
# elif temp1 != temp2 and temp3 < temp2:
# 	print('Hi')
# else:
# 	print('Good morning' ,)

# phrase1 = 'apple'
# phrase2 = 'appl'
# if phrase1.isupper() or phrase1 < phrase2:
# 	print('Hello')
# elif not(phrase2.isupper()) and phrase2 in phrase1:
# 	print('Hi')
# else:
# 	print('Good morning')
# phrase1 = 'Lemon' 
# phrase2 = 'lemon'
# if phrase1 != phrase2:
# 	print('Lemons are sours.')
# else:
# 	print('Lemons are blue.')
# phrase2 = phrase2.capitalize()
# if phrase1 != phrase2:
# 	print('Lemons are sweet.')
# else:
# 	print('Lemons are orange.')
# phrase1 = phrase1.lower()
# if phrase1 != phrase2:
# 	print('Lemons are bitter.')
# else:
# 	print('Lemons are yellow.')

# a = 64
# b = 65
# c = 66
# d = 64
# if not (a < b) and b < c:
# 	if a == d or a < c:
# 		print('Hey')
# elif a > c or a == d:mn
# 	if a < b or d <  c:
# 		print('Yay')
# 	if d < b and c < b:
# 		print('Hurray')
# 	else:
# 		a = a + 2
# else:
# 	print('Nay')
# if a == c and d < b:
# 	print('How are you?')
# print ('Goodbye')
# age=int(input("Enter your age:"))
# citizen=(input("Enter your citizen:"))
# if age >= 18 and citizen.lower() =="bangladesh":
#     print("you are egible to vote.")
# else : 
#     print("You are not eligible to vote.")
# age = int(input("Enter your age: "))
# citizen = input("Enter your citizen: ")

# if age >= 18 and citizen.lower() == "bangladesh":
#     print("You are eligible to vote.")
# else: 
#     print("You are not eligible to vote.")

word=input("Enter the words:").lower() 

if len(word)%5==0 :
    #word=word.upper()
    print(word.upper())
else : 
    print(word)