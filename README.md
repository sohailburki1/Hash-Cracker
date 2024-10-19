# 🔐 Hash Identifier & Cracker

This Python script allows users to **identify hash types** and **crack hashed passwords** using wordlists. It supports multiple popular hash algorithms, including MD5, SHA-1, SHA-256, and SHA-512.

The script features two main tools:

1. **Hash Identifier**: Determines the hash type based on the hash's length.
2. **Hash Cracker**: Attempts to crack the hash using a provided wordlist, supporting various hash algorithms.

## Features

- **Hash Type Identification**: Quickly identifies the hash type based on its length.
- **Wordlist-based Cracking**: Crack common hashes by comparing them with wordlist entries.
- **Supported Hash Algorithms**: 
  - MD5
  - SHA-1
  - SHA-256
  - SHA-512
- **Detailed ASCII Art** to give a cool interface for both tools.

### 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/hash-cracker.git
   ```

2. **Navigate into the directory**:
   ```bash
   cd hash-cracker
   ```

3. **Run the script**:
   ```bash
   python3 hash_cracker.py
   ```

4. **Select an option**:
   - `1` for identifying the hash type.
   - `2` for cracking a hash with a wordlist.

### 💻 Usage

#### 1. **Hash Identifier**

You can identify the type of a hash by selecting the **Hash Identifier** option.

```plaintext
Choose an option: 
1. Hash Identifier  
2. Hash Cracker
Your choice: 1
```

Enter the hash value, and the script will determine the hash type (MD5, SHA-1, SHA-256, SHA-512).

```plaintext
Enter the hash to identify: f96b697d7cb7938d525a2f31aaf161d0
Identifying the given hash type.........
The hash type is: MD5
```

#### 2. **Hash Cracker**

If you need to crack a hash using a wordlist, select the **Hash Cracker** option.

```plaintext
Choose an option: 
1. Hash Identifier  
2. Hash Cracker
Your choice: 2
```

You will be prompted to enter the hash, the path to your wordlist, and the hash type.

```plaintext
Enter the hash to crack: 5d41402abc4b2a76b9719d911017c592
Path to wordlist: /path/to/wordlist.txt
Enter the hash type (md5, sha1, sha256, sha512): md5
Cracking Hash.......
Hash cracked! The password is: hello
```

### 📂 File Structure

```
├── hash_cracker.py   # Main script
└── wordlist.txt      # Wordlist File
```

### ⚙️ Requirements

- Python 3.x
- A wordlist file (you can find many online or create your own)

---

Enjoy using the **Hash Identifier & Cracker** to crack hashes and identify them with ease! 😎
