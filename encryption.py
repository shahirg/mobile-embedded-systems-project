from cryptography.fernet import Fernet

def generate_key(file_path):
    key = Fernet.generate_key()

    with open(f'{file_path}/mykey.key', 'wb') as mykey:
        mykey.write(key)
        
    return key

def load_key(file_path):
    with open(file_path, 'rb') as mykey:
        key = mykey.read()
    return key

def encrypt(key, file_path):
    f = Fernet(key)

    with open(file_path, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open (file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt(key, file_path):
    f = Fernet(key)

    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)