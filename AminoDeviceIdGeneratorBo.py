from os import urandom
from hashlib import sha1
from base64 import b64decode
from pyfiglet import figlet_format
from progress.bar import IncrementalBar
from colorama import init, Fore, Style; init()
print(Fore.GREEN + Style.NORMAL)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(figlet_format("aminodeviceidgeneratorbo", font="bell"))

def deviceID_generator(hwid: str):
    return "01" + (identifier := sha1(hwid.encode("utf-8"))).hexdigest() + sha1(bytes.fromhex("01") + identifier.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()

def generation_process(count: int):
	try:
		progress_bar = IncrementalBar("Generated", max=count)
		with open ("device_Ids.txt" "a") as device_Ids:
			for i in range(count):
				device_Id = deviceID_generator(hwid=urandom(20))
				device_Ids.write(f"{device_Id}\n")
				bar.next()
			print(f"-- Successful generated {count} deviceIds!")
			bar.finish()
	except:
		return

count = int(input("-- How many deviceIDs?::: "))
generation_process(count=count)
