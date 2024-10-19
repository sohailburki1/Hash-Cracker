# Hash Cracker
## Overview

The **Hash Cracker** is a Python-based utility designed to crack hashed passwords using a wordlist. This project supports multiple hashing algorithms, including **MD5**, **SHA-1**, **SHA-256**, and **SHA-512**. It is built to help users understand hash functions and improve their password security awareness.

## Features

- **Multi-Algorithm Support**: Crack passwords hashed with the following algorithms:
  - **MD5**: Produces a 128-bit hash value (32 characters).
  - **SHA-1**: Produces a 160-bit hash value (40 characters).
  - **SHA-256**: Produces a 256-bit hash value (64 characters).
  - **SHA-512**: Produces a 512-bit hash value (128 characters).

- **Customizable Wordlist**: Users can specify their own wordlist file to attempt cracking hashed passwords.

- **User-Friendly Interface**: Simple command-line interface for easy interaction and prompts for user inputs.

## Getting Started

### Prerequisites

- **Python**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the Repository**: 
   Open your terminal or command prompt and execute the following command:
   ```
   git clone https://github.com/yourusername/hash-cracker.git
   cd hash-cracker
   ```

2. **Install Dependencies**: 
   This project mainly utilizes the built-in `hashlib` library; no additional installations are required. Ensure your Python environment is correctly set up.

Here’s an updated section for your README that includes important information about the Python script's UTF-8 encoding as well as the wordlist file encoding:

---

### Important Note on Wordlist File and Python Script Encoding

To avoid issues when reading the wordlist file and executing the Python script, please ensure that both are saved with **UTF-8** encoding. This is crucial for correctly reading the file contents and ensuring that all passwords in the wordlist are processed accurately.

#### Wordlist File Encoding

- **To Check or Change Encoding**:
  1. Open your wordlist file in a text editor (such as Notepad++, VS Code, or Sublime Text).
  2. Ensure it is saved as **UTF-8** without BOM (Byte Order Mark).
  3. In Notepad++, you can do this by going to `Encoding` > `Convert to UTF-8 (without BOM)` and saving the file.

#### Python Script Encoding

The Python script should also be saved with **UTF-8** encoding to ensure proper handling of string data. This is especially important if your wordlist contains special characters or if you plan to extend the script with additional functionality that requires non-ASCII characters.

- **To Ensure Proper Encoding**:
  1. When creating or editing your Python script, make sure your text editor is set to use **UTF-8** encoding.
  2. In most modern text editors, you can typically find encoding options in the settings or preferences menu.
  3. If you're using an IDE like PyCharm or VS Code, they usually default to UTF-8 encoding, but it's good practice to verify.

By following these guidelines, you can avoid potential issues with character encoding that may lead to errors or incorrect password cracking attempts.

### Usage

To run the hash cracker, use the following command:
```
python hash_cracker.py
```

#### Example Interaction

The program will prompt you for input. Below is an example interaction:
```
Enter the hash to crack: 1f3870be274f6c49b3e31a0c6728957f
Enter the path to the wordlist file: /path/to/your/wordlist.txt
Enter the hash type (md5, sha1, sha256, sha512): md5
```

### Sample Wordlist

You can create a sample wordlist (`wordlist.txt`) with the following content:
```
orange
banana
grape
apple
pear
watermelon
kiwi
```

### How It Works

1. The program takes a hash, a wordlist file, and the hash type as inputs.
2. It reads the wordlist line by line, stripping any whitespace.
3. For each word, it generates the corresponding hash using the specified algorithm.
4. It compares the generated hash with the target hash.
5. If a match is found, it outputs the cracked password; otherwise, it notifies the user that the password was not found.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to fork the repository and submit a pull request.
