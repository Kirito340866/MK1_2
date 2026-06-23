#  MK1_2

A high-performance, multi-threaded command-line tool written in Python, designed for local authentication speed testing, password strength auditing, and security research. Powered by concurrent processing and optimized memory batching. This repository includes two versions: the interactive script (`bruteforcer.py`) and the advanced CLI argument script (`bruteforcer_arg.py`).
```text
 __  __ _   __  _ 
|  \/  | |/ / / | 
| |\/| | ' /  | | 
| |  | | . \  | | 
|_|  |_|_|\_\ |_| 
```
Created By: Kirito34086

 Features
🔹 Core Engine (Both Versions)

     Intelligent Threading: Customizable concurrency utilizing Python's ThreadPoolExecutor (Supports 1-100 threads).

     Memory-Efficient Batching: Avoids memory/RAM exhaustion by reading large wordlists (like rockyou.txt) dynamically in highly optimized 1,000-line batches.

     Advanced Combination Generator: Uses itertools.product to generate and process credential combinations on-the-fly without pre-allocating massive lists.

     Robust Input Validation: Full error handling for non-numeric thread selections, invalid file paths, and target response timeouts.

     Clean Interruption: Gracefully catches KeyboardInterrupt (Ctrl+C) at the root layer to ensure a clean exit without terminal clutter.

🔹 Exclusive to CLI Version (bruteforcer_arg.py)

     Direct Switch Injection: Fully automated configuration parsing using -u, -n, and -p switches, eliminating internal sequential inputs.

     Suppressed Exceptions: Network dropped frames and packet timeouts inside background threads are captured silently to preserve screen clarity.

 Installation & Requirements

Make sure you have Python 3 installed on your system. This tool requires the requests module to handle HTTP operations.

    Clone the repository:
    Bash

git clone [https://github.com/Kirito34086/MK1.git](https://github.com/Kirito34086/MK1.git)
cd MK1

Install requirements:
Bash

    pip install requests

 Usage Instructions:

Choose the edition that best fits your workflow:
1️ Option A: Advanced CLI Version (bruteforcer_arg.py)

To operate this specific script, run it by providing all required switches directly inside your terminal emulator.
 Syntax:
Bash

python3 bruteforcer_arg.py -u <TARGET_URL> -n <USER_LIST> -p <PASSWORD_LIST>

 Execution Example:
Bash

python3 bruteforcer_arg.py -u [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login) -n usernames.txt -p passwords.txt

 Available Parameters Table:
Parameter	Alternative	Scope & Description	Mandatory
-u	--url	Target remote authentication page URL endpoint	Yes
-n	--names	Local absolute or relative system path to the username file	Yes
-p	--passwords	Local absolute or relative system path to the password file	Yes

    Note: Immediately after execution, the program will halt briefly to prompt you to type the target worker thread volume (1-100) before unleashing the threads concurrently.

2️ Option B: Standard Interactive Version (bruteforcer.py)

Simply execute the script using Python. The tool is fully interactive and will prompt you sequentially for the necessary configurations.
 Execution:
Bash

python3 bruteforcer.py

 Interactive Prompts:

    Target URL: Enter the login endpoint (e.g., http://127.0.0.1:5000/login).

    Username List Path: Provide the full path to your username wordlist (e.g., /usr/share/wordlists/username.txt).

    Password List Path: Provide the full path to your password wordlist (e.g., /usr/share/wordlists/rockyou.txt).

    Number of Threads: Define the concurrency level between 1 and 100 based on your system performance.

⚠️ Educational Disclaimer

This tool is developed and distributed strictly for educational purposes, authorized penetration testing, and security auditing. Do not utilize this script against any production systems or environments without explicit, prior written permission from the system owner. The developer assumes absolutely no liability for any misuse, unauthorized attacks, or damage caused by this utility.
