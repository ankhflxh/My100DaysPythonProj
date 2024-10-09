#prints out the header
print("Welcome to the Band Name Generator\n")
#Takes in input from user and stores in variables city and pet respectively
city = input("What's the name of the city you grew up in?\n")
pet = input("What is your pet's name?\n")
#concatinates the results and stores in a variable bandname that can be called later
bandname = city + " " + pet
#print the result as suggestion for bandname
print("Your band name could be " + bandname)