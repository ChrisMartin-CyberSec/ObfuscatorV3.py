#!/usr/bin/env python

'''
Script Name: 	ObfuscatorV3.py
Author:      	Levi Von Haxor
Purpose:     	Obfuscate a Python or VBScript file passed 
		as an argument
Example:	python ObfuscatorV3.py -v notavirus.vbs
Return: 	obs_notavirus.vbs (This is the payload)
'''

import random
import argparse
import base64
import string
from junkObs import junkPy, junkVBS

def obsFile():
	'''
	Obfuscates the payload
	'''
	DELIMETERS = ['!','@','#','$','%','^','&','*','-']

	global delimeter
	
	delimeter = 5*random.choice(DELIMETERS)

	asciiChars = string.ascii_letters
	translationChars = asciiChars[::-1]
	
	if args['vbscript']:
		file = args['vbscript']

		with open(file) as f:
			contents = f.read()

		asciiValues = [str(ord(c)) for c in contents][::-1] # Reverse the contents of the file and convert to ASCII Values

		delContents = [i + delimeter for i in asciiValues]

		encContents = ''.join(delContents)

	if args['python']:
		file = args['python']

		with open(file) as f:
			contents = f.read()

		trTable = contents.maketrans(asciiChars, translationChars)
		trContents = contents.translate(trTable) # Reverse the contents of the file and convert to ASCII Values

		asciiValues = [str(ord(c)) for c in trContents]

		delContents = [i + delimeter for i in asciiValues]
		delContents = ''.join(delContents)

		contentBytes = delContents.encode("ascii")
		content64 = base64.b64encode(contentBytes)
		encContents = content64.decode("ascii")
	
	return encContents


def obsVBS(EC):
	'''
	Creates the deobfuscation header for a VBScript file
	'''
    
	file = args['vbscript']

	Encoder = "".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15)))    

	with open('obs_' + file, 'w') as f:
		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.write(f'{Encoder} = "{EC}"\n')	

		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)	
		
		f.writelines([f'del = "{delimeter}"\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				f'{Encoder}=split({Encoder},del)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'zero = 0\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n'])
		
		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.writelines([f'length_stuff = ubound({Encoder})-1\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'for i = zero TO length_stuff\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				f'index_blob = {Encoder}(i)\n',
				'char_of_blob = chrw(index_blob)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'all_char = all_char & char_of_blob\n',
				'Next\n',
                		'all_char = StrReverse(all_char)\n' 
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n',
				'WScript.Sleep(0)\n'])

		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.write('executeglobal (all_char)\n')

		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)
	

def obsPY(EC):
	'''
	Creates the deobfuscation header for a Python file
	'''    
	Encoder, var1,var2, var3, var4, var5, var6, var7 = ["".join(random.choices(list(string.ascii_letters), k=random.randint(5, 15))) for x in range(8)]

	file = args['python']
	with open('obs_' + file, 'w') as f:
		
		f.writelines(['import math\n', 'import random\n', 'import string\n', 'import time\n'])
        
		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.write('import base64\n')
		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.write(f"{Encoder} = '{EC}'\n")

		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.write(f'{var1}={Encoder}.encode("ascii")\n')
		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.write(f'{var2}=base64.b64decode({var1});{var3}={var2}.decode("ascii")\n')
		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.write(f'{var4}=[chr(int(i)) for i in {var3}.split("{delimeter}") if i];{var5}="".join({var4})\n')
		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.write(f'{var6} = {var5}.maketrans(string.ascii_letters,string.ascii_letters[::-1]);{var7}= {var5}.translate({var6})\n')
		f.writelines(junk[:round(len(junk)/10)])
		random.shuffle(junk)

		f.write(f'exec({var7})\n')         
		f.writelines(junk[:round(len(junk)/10)])
			

def main():
	global parser, group, args, encContents, junk

	parser = argparse.ArgumentParser(description = 'An obfucation program designed to obfuscate VBScript and Python scripts')

	group = parser.add_mutually_exclusive_group() # Sets the condition where the user cannot choose multiple arguments in the group 'group'
	
	group.add_argument('-v', '--vbscript', help = 'VBScript file to be passed') 
	group.add_argument('-p', '--python', help = 'Python file to be passed')

	args = vars(parser.parse_args()) # Turns the args into a dictionary such as a -p 'file' argument returns args = {'vbscript': None, 'python': 'file'}

	encContents = obsFile()

	if args['vbscript']:

		junk = junkVBS()

		obsVBS(encContents)		
		
	if args['python']:

		junk = junkPy()

		obsPY(encContents)
	
	
if __name__ == '__main__': # Will only run main() function directly from this module unless explicitly imported from another module
	main()
