string = input("Enter a string")
strlen=len(string)
rev=string[strlen::-1]
if (rev==string):
    print("pallindrome")
else:
    print("Not a pallindrome")
