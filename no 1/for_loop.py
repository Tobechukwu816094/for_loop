"""
write a program that ask the user for their name and how
many times to print it.The program should print out the user's name the specified number 
of times.

"""
password = input("please enter your name:")
number =int(input("please enter how many times to print it:"))
for i in range( number ):
    print(i+1 , password )




