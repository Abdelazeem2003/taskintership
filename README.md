# taskintership
encrypt file by python 
#Explain The Code
1- from cryptography.fernet import Fernet
import os :-

Fernet from the cryptography library: Provides an easy and secure way to encrypt

os: We use it to check if files exist in the system.

2- operation = input("Encrypt (e) or decrypt (d)? ").lower()

Here
We ask the user to specify the desired operation (encryption or decryption).
.lower() converts the input to lowercase to avoid errors.

3-key = input("Enter encryption key (leave empty to generate new): ").encode()
if not key:
    key = Fernet.generate_key()
    print(f"Your new key: {key.decode()}")
We ask the user to enter an existing key or leave the field blank to generate a new one.
If the field is left blank, we generate a new key using Fernet.generate_key().
We display the new key to the user because they will need it later for decryption.

4- while True:
    file_name = input("File to process: ").strip()
    if os.path.exists(file_name):
        break
    print(f"Error: File '{file_name}' not found! Please try again.")

We use an infinite loop to ensure a valid filename is entered.
Strip() removes any extra spaces.
We check for the file's existence using os.path.exists().
If the file doesn't exist, we display an error message and request input again.

5-with open(file_name, 'rb') as f:
    data = f.read()

We open the file in binary read mode ('rb'). We read the entire contents of the file and store it in the data variable.

6- fernet = Fernet(key)
result = fernet.encrypt(data) if operation == 'e' else fernet.decrypt(data)



We create a Fernet object using the key.
We use encryption if the choice is 'e', ​​or decryption if 'd'.

7- new_name = file_name + ('.enc' if operation == 'e' else '.dec')
with open(new_name, 'wb') as f:
    f.write(result)


We specify the new file name by adding .enc or .dec, depending on the operation.
We open a new file in binary writing mode ('wb').
We write the processed data (encrypted or decrypted) to the new file


8-print(f"Done! File saved as {new_name}")

We display a message confirming the success of the operation and the new file name.

