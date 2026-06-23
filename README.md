# MK1_2

A high-performance, multi-threaded command-line tool written in Python, designed for local authentication speed testing, password strength auditing, and security research. Powered by concurrent processing and optimized memory batching.


 __  __ _   __  _ 
|  \/  | |/ / / | 
| |\/| | ' /  | | 
| |  | | . \  | | 
|_|  |_|_|\_\ |_| 

Created By: Kirito34086

✨ Features

    🚀 Intelligent Threading: Customizable concurrency utilizing Python's ThreadPoolExecutor (Supports 1-100 threads).

    🧠 Memory-Efficient Batching: Avoids memory/RAM exhaustion by reading large wordlists (like rockyou.txt) dynamically in highly optimized 1,000-line batches.

    🎯 Advanced Combination Generator: Uses itertools.product to generate and process credential combinations on-the-fly without pre-allocating massive lists.

    🛡️ Robust Input Validation: Full error handling for non-numeric thread selections, invalid file paths, and target response timeouts.

    🛑 Clean Interruption: Gracefully catches KeyboardInterrupt (Ctrl+C) at the root layer to ensure a clean exit without terminal clutter.

🛠️ Installation & Requirements

Make sure you have Python 3 installed on your system. This tool requires the requests module to handle HTTP operations.

    Clone the repository:
    Bash

git clone [https://github.com/YOUR_GITHUB_USERNAME/MK1-Authentication-Auditor.git](https://github.com/YOUR_GITHUB_USERNAME/MK1-Authentication-Auditor.git)
cd MK1-Authentication-Auditor

Install requirements:
Bash

    pip install requests

🚀 How to Use

Simply execute the script using Python. The tool is fully interactive and will prompt you for the necessary configurations:
Bash

python3 brute_forcer.py

📋 Interactive Prompts:

    Target URL: Enter the login endpoint (e.g., http://127.0.0.1:5000/login).

    Username List Path: Provide the full path to your username wordlist (e.g., /usr/share/wordlists/username.txt).

    Password List Path: Provide the full path to your password wordlist (e.g., /usr/share/wordlists/rockyou.txt).

    Number of Threads: Define the concurrency level between 1 and 100 based on your system performance.

⚠️ Educational Disclaimer

This tool is developed and distributed strictly for educational purposes, authorized penetration testing, and security auditing. Do not utilize this script against any production systems or environments without explicit, prior written permission from the system owner. The developer assumes absolutely no liability for any misuse, unauthorized attacks, or damage caused by this utility.
