import hashlib
import time

ascii_art = r"""
------------------------------------------------------------
  _  _   _   ___ _  _    ___ ___    _   ___ _  _____ ___ 
 | || | /_\ / __| || |  / __| _ \  /_\ / __| |/ / __| _ \
 | __ |/ _ \\__ \ __ | | (__|   / / _ \ (__| ' <| _||   /
 |_||_/_/ \_\___/_||_|  \___|_|_\/_/ \_\___|_|\_\___|_|_\
                                                         
by Muhammad Sohail
------------------------------------------------------------
"""

ascii_art2 = r"""
----------------------------------------------------------------------
  _  _   _   ___ _  _    ___ ___  ___ _  _ _____ ___ ___ ___ ___ ___ 
 | || | /_\ / __| || |  |_ _|   \| __| \| |_   _|_ _| __|_ _| __| _ \
 | __ |/ _ \\__ \ __ |   | || |) | _|| .` | | |  | || _| | || _||   /
 |_||_/_/ \_\___/_||_|  |___|___/|___|_|\_| |_| |___|_| |___|___|_|_\
                                                                     
by Muhammad Sohail
----------------------------------------------------------------------
"""

def main():
    user_choice = input("Choose an option: \n1. Hash Identifier  \n2. Hash Cracker\nYour choice: ")
    if user_choice == '1':
        hash_value = input("Enter the hash to identify: ")
        print(ascii_art2)
        if all(c in '0123456789abcdefABCDEF' for c in hash_value):
            hash_type = identify_hash(hash_value)
            print("Identifying the given hash type.........")
            time.sleep(5)
            print(f"\nThe hash type is: {hash_type}")
        else:
            print("Invalid hash format. Please ensure it is a hexadecimal string.")
        identify_hash(hash_value)
    elif user_choice == '2':
        target_hash = input("Enter the hash to crack: ")
        wordlist = input("Path to wordlist: ")
        hash_type = input("Enter the hash type (md5, sha1, sha256, sha512): ").lower()
        crack_hash(target_hash, wordlist, hash_type)
    else:
        print("Invalid Input!")

def identify_hash(hash_value):
    hash_length = len(hash_value)

    if hash_length == 32:
        return "MD5"
    elif hash_length == 40:
        return "SHA-1"
    elif hash_length == 64:
        return "SHA-256"
    elif hash_length == 128:
        return "SHA-512"
    else:
        return "Unknown hash type"


def crack_hash(hash_to_crack, wordlist_file, hash_type):
    print(ascii_art)
    try:
        with open(wordlist_file, 'r') as file:
            for word in file.readlines():
                word = word.strip()

                if hash_type == 'md5':
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha512':
                    hashed_word = hashlib.sha512(word.encode()).hexdigest()
                else:
                    print("Unsupported hash type!")
                    return

                if hashed_word == hash_to_crack:
                    print("Cracking Hash.......")
                    time.sleep(3)
                    print(f"\nHash cracked! The password is: {word}")
                    return

            print("Password not found in wordlist.")
    except FileNotFoundError:
        print("Wordlist file not found. Please check the file path.")

if __name__ == '__main__':
    main()
