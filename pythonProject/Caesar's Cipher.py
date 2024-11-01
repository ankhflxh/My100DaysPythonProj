import string
#Import and print the logo from cipherart.py when the program starts.
import cipherart

print(cipherart.logo)
task = input("encode or decode\n")

#while the input is not encode or decode, using the while loop, it will rerun again
while task != "encode" and task != "decode":
    print("invalid response please!\n")
    task = input("encode or decode\n")

text = input(f"enter word to {task} :\n")
shift = int(input("enter how much you want to shift:\n"))
alphabet = string.ascii_letters.lower()

#Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    cipher =""
    for i in original_text:
        if i not in alphabet:
            cipher += i
        else:
            shifted_amount = alphabet.index(i) + shift
            shifted_amount %= len(alphabet)
            cipher += alphabet[shifted_amount]
    print(f"This is your {task}d word: \n{cipher}")

#Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def decrypt(original_text, shift_amount):
    cipher =""
    for i in original_text:
        if i not in alphabet:
            cipher += i
        else:
            shifted_amount = alphabet.index(i) + shift
            shifted_amount %= len(alphabet)
            cipher += alphabet[shifted_amount]
    print(f"This is your {task}d word: \n{cipher}")
#Create another function to call both functions above with conditions
def checker():
        if task == "encode":
            encrypt(original_text=text, shift_amount=shift)
        elif task == "decode":
            decrypt(original_text=text, shift_amount=shift)
checker()
#sets a while loop to check if user wants to go again
should_continue = True
while should_continue:
    choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if choice == "no":
        should_continue = False
        print("Goodbye and thank you.")
    else:
        task = input("encode or decode\n")
        text = input(f"enter word to {task} :\n")
        shift = int(input("enter how much you want to shift:\n"))
        checker()



