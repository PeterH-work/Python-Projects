# Before running this decrypter:
# Place the Encrypted text in a text file - named EncryptedText.txt - in the same folder as Decrypter.py

# working decryption scheme:
# Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

# Define the character set
CHAR_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

def decrypt_number(number):
    """Decrypt a single number using the provided method."""
    return CHAR_SET[number % 37]

def decrypt_file(input_file):
    """Decrypt the contents of the input file and print to the screen."""
    with open(input_file, 'r') as infile:
        encrypted_numbers = infile.read().split()
        decrypted_text = ''.join(decrypt_number(int(num)) for num in encrypted_numbers)
        # Wrap the decrypted text in the picoCTF flag format
        wrapped_text = f"picoCTF{{{decrypted_text}}}"
        print(wrapped_text)

# Specify the input file name
input_file = 'EncryptedText.txt'

# Perform the decryption
decrypt_file(input_file)
