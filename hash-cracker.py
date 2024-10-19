import hashlib

def main():
    target_hash = input("Enter the hash to crack: ")
    wordlist = input("Path to wordlist: ")
    hash_type = input("Enter the hash type (md5, sha1, sha256, sha512): ").lower()

    crack_hash(target_hash, wordlist, hash_type)


def crack_hash(hash_to_crack, wordlist_file, hash_type='md5'):
    try:
        with open(wordlist_file, 'r') as file:
            for word in file.readlines():
                word = word.strip()
                print(f"Trying password: {word}")

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
                    print(f"Hash cracked! The password is: {word}")
                    return

            print("Password not found in wordlist.")
    except FileNotFoundError:
        print("Wordlist file not found. Please check the file path.")

if __name__ == '__main__':
    main()
