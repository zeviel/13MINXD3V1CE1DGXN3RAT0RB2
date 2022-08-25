from os import urandom
from hashlib import sha1
from base64 import b64decode
from pyfiglet import figlet_format
from progress.bar import IncrementalBar
print("""Script by zeviel
Github : https://github.com/zeviel""")
print(figlet_format("13MINXD3V1CE1DGXN3RAT0RB2", font="bell"))

def generate_device_id(hwid: str):
    return "01" + (identifier := sha1(hwid.encode("utf-8"))).hexdigest() + sha1(bytes.fromhex("01") + identifier.digest() + b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()

def generation_process(count: int):
	try:
		progress_bar = IncrementalBar("Generated", max=count)
		with open ("device_ids.txt" "a") as device_Ids:
			for i in range(count):
				device_id = generate_device_id(urandom(20))
				device_ids.write(f"{device_id}\n")
				bar.next()
			print(f"-- Successful generated {count} deviceIds!")
			bar.finish()
	except:
		return

count = int(input("-- How many deviceIDs?::: "))
generation_process(count=count)
