from cryptography.fernet import Fernet
import os

operation = input("Encrypt (e) or decrypt (d)? ").lower()

key = input("Enter encryption key (leave empty to generate new): ").encode()
if not key:
    key = Fernet.generate_key()
    print(f"Your new key: {key.decode()}")

while True:
    file_name = input("File to process: ").strip()
    if os.path.exists(file_name):
        break
    print(f"Error: File '{file_name}' not found! Please try again.")

with open(file_name, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
result = fernet.encrypt(data) if operation == 'e' else fernet.decrypt(data)

new_name = file_name + ('.enc' if operation == 'e' else '.dec')
with open(new_name, 'wb') as f:
    f.write(result)
print(f"Done! File saved as {new_name}")