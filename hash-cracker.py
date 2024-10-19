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

def main():
    target_hash = input("Enter the hash to crack: ")
    wordlist = input("Path to wordlist: ")
    hash_type = input("Enter the hash type (md5, sha1, sha256, sha512): ").lower()

    crack_hash(target_hash, wordlist, hash_type)


def crack_hash(hash_to_crack, wordlist_file, hash_type='md5'):
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
                    time.sleep(2)
                    print("Cracking Hash.......")
                    time.sleep(3)
                    print(f"\nHash cracked! The password is: {word}")
                    return

            print("Password not found in wordlist.")
    except FileNotFoundError:
        print("Wordlist file not found. Please check the file path.")

if __name__ == '__main__':
    main()
