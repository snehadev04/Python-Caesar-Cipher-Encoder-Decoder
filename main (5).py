# Import the logo from the art module
from art import logo

# Create a list containing all the lowercase letters of the alphabet twice to handle shifts beyond 'z'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Print the logo
print(logo)

# Define a function to perform the Caesar cipher encryption or decryption
def caesar_cipher(text, shift, direction):
    # Initialize an empty string to store the result
    cesar_text = ""
    # Adjust the shift for decryption
    if direction == "decode":
        shift *= -1
    # Iterate over each character in the input text
    for char in text:
        # Check if the character is a letter in the alphabet
        if char in alphabet:
            # Find the index of the character in the alphabet list
            position = alphabet.index(char)
            # Calculate the new position after shifting
            new_position = (position + shift) % 26
            # Append the shifted character to the result
            cesar_text += alphabet[new_position]
        else:
            # If the character is not a letter, keep it unchanged
            cesar_text += char
    # Print the result
    print(f"Your {direction}d message is: {cesar_text}")

# Initialize a variable to control the loop
should_end = False
# Continue the loop until should_end becomes True
while not should_end:
    # Prompt the user to choose between encryption and decryption
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Check if the input is valid
    if direction not in ["encode", "decode"]:
        # Print an error message for invalid input and continue to the next iteration
        print("Invalid input. Please type 'encode' or 'decode'.")
        continue
    # Prompt the user to enter the message to be encrypted or decrypted
    text = input("Type your message:\n").lower()
    # Prompt the user to enter the shift value
    shift = int(input("Type the shift number:\n"))
    # Ensure the shift value is within the range of the alphabet (0-25)
    shift = shift % 26
    # Call the caesar_cipher function to perform encryption or decryption
    caesar_cipher(text, shift, direction)
    # Prompt the user to choose whether to continue or end the program
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    # Check if the user wants to end the program
    if restart == "no":
        # Set should_end to True to exit the loop
        should_end = True
        # Print a farewell message
        print("Goodbye")

  