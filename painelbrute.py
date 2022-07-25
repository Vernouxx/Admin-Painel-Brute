import requests
import re
import os
import linecache
#Programado por @Vernoux!
def limpa():
	os.system('clear')
print ('''
\033[1;91mProjeto De painel finder
BETA
\033[1;97m@\033[1;92mBy Vernoux
\033[0;0m''')
try:
	url = input('\033[1;91mInsira a url: \033[1;92m')
except KeyboardInterrupt:
	limpa()
	print ('Script parado!')
	exit(0)



print ('Sua url ', url)
try:

	status = requests.get(url)
	foda = (status.status_code)

except requests.exceptions.ConnectionError:
	limpa()
	print ('INSIRA UMA URL VALIDA!')
	exit(0)
except requests.exceptions.MissingSchema:
	limpa()
	print ('INSIRA UMA URL VALIDA!')
	exit(0)



def brute():
	num = 0
	try:
		arquivo = input('\033[1;91mInsira a wordlist: \033[1;92m')
		a=open(arquivo,'r')
		l=a.read()
		count=l.splitlines()
		linhas = len(count)
	except FileNotFoundError:
		print ('ARQUIVO INEXISTENTE!')
		exit(0)
	print (f'''
O arquivo {arquivo} possui {linhas} list!
	''')

	for i in range(linhas):
		num = num + 1
		data = linecache.getline(arquivo, num).strip()
		status = requests.get(f'{url}/{data}')
		foda = (status.status_code)
		if foda == 403:
			print(f'\033[1;91mERRO \033[1;97m"{url}/{data}"\033[1;97m > \033[1;91mForbidden\033[0;0m')
		if foda == 404:
			print(f'\033[1;91mERRO \033[1;97m"{url}/{data}"\033[1;97m >  \033[1;91mNot Found\033[0;0m')
		if foda == 200:
			print(f'\033[1;92mSUCESSO! \033[1;97m>  \033[1;91m{url}/{data}\033[0;0m')
	print ('brute force finalizado ;)')
	exit(0)
print ('teste feito')
brute()