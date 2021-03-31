import os
import rich
import sys
from rich.console import Console
from rich.table import Table

console = Console()
greetingStyle = "bold white on red"
processStyle = "bold green"

def greeting():
	console.print("Welcome to cryptor!", style=greetingStyle, justify="center")

def comList():
	comlist = Table()
	comlist.add_column("[italic bold blue]Index[/italic bold blue]", justify="left")
	comlist.add_column("[italic bold blue]Name[/italic bold blue]", justify="center")
	comlist.add_column("[italic bold blue]Description[/italic bold blue]", justify="right")
	#data
	comlist.add_row("1", "Encryption using RSA", "It's just encrypts little files")
	comlist.add_row("2", "Dencryption using RSA", "It's just dencrypts little files")
	comlist.add_row("3", "Encryption using AES-256-CBC", "It's just encrypts little files")
	comlist.add_row("4", "Dencryption using AES-256-CBC", "It's just dencrypts little files")
	console.print(comlist)

greeting()

while True:
	comList()
	com = console.input("Enter [i bold red]option[/i bold red]?: ")
	if com == "1":
		name = console.input("Enter enviroment [i bold red]name[/i bold red]: ")
		byteNum = console.input("Enter private key's [i bold red]number of bytes[/i bold red]: ")
		file = console.input("Enter [i bold red]file path[/i bold red]: ")
		os.system("mkdir {}".format(name))
		os.system("openssl genpkey -algorithm RSA -out priv.key -pkeyopt rsa_keygen_bits:{}".format(byteNum))
		console.print("Private key has generated", style=processStyle, justify="left")
		os.system("openssl rsa -in priv.key -pubout -out pub.key")
		console.print("Public key has generated", style=processStyle, justify="left")
		os.system("openssl rsautl -encrypt -pubin -inkey pub.key -in {} -out encrypted".format(file))
		console.print("File has been encrypted with RSA", style=processStyle, justify="left")
		os.system("cp -r priv.key pub.key encrypted {}".format(name))
		os.system("rm -rf priv.key pub.key encrypted")
	if com == "2":
		name = console.input("Enter enviroment [i bold red]name[/i bold red]: ")
		os.system("openssl rsautl -decrypt -inkey {}/priv.key -in {}/encrypted -out {}/dencrypted".format(name, name, name))
		console.print("File has been decrypted with RSA", style=processStyle, justify="left")
	if com == "3":
		name = console.input("Enter enviroment [i bold red]name[/i bold red]: ")
		file = console.input("Enter [i bold red]file path[/i bold red]: ")
		iter = console.input("Enter [i bold red]number of iteration[/i bold red]: ")
		os.system("mkdir {}".format(name))
		os.system("openssl enc -aes-256-cbc -in {} -out encrypted -iter {}".format(file, iter))
		os.system("cp -r encrypted {} && rm -rf encrypted".format(name))
		console.print("File has been encrypted with aes-256-cbc", style=processStyle, justify="left")
	if com == "4":
		name = console.input("Enter enviroment [i bold red]name[/i bold red]: ")
		iter = console.input("Enter [i bold red]number of iteration[/i bold red]: ")
		os.system("openssl enc -aes-256-cbc -d -in {}/encrypted -out {}/decrypted -iter {}".format(name, name, iter))
		console.print("File has been decrypted with aes-256-cbc", style=processStyle, justify="left")
	if com == "q":
		console.print("Bye ...", style=processStyle, justify="left")
		sys.exit()

