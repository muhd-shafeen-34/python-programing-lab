#create a string from given string where first and last charecters exchanged

text = input("enter the string:- ")
newtext = text[-1]+text[1:-1]+text[0]
print("new string: ",newtext)
