import base64
import string
import random
import json
import time
import pyfiglet
from hashlib import sha1
from progress.bar import IncrementalBar
from colorama import init, Fore, Back, Style
init()
print(Fore.GREEN)
print(Style.NORMAL)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminodeviceid", font="bell"))
print(pyfiglet.figlet_format("generatorbo", font="bell"))
def deviceIdgenerator(st : int = 69):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = st))
    deviceid = '01' + (MetaSpecial := sha1(ran.encode("utf-8"))).hexdigest() + sha1(bytes.fromhex('01') + MetaSpecial.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()
    return deviceid

def deviceIdgenerationproccess():
	try:
		bar = IncrementalBar('Generated', max = generatingnumber)
		for i in range(generatingnumber):
			device = deviceIdgenerator()
			devfile = open('deviceids.txt', "a+")
			devfile.write(device + '\n')
			bar.next()
	except:
		return

generatingnumber = int(input("How Much DeviceId Generate: "))

deviceIdgenerationproccess()
print(f"\nGenerated {generatingnumber} deviceids")
