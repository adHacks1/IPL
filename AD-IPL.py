import ipinfo
import pprint
from colorama import Fore, Back, Style
from os import system, name
import os
import webbrowser
def clear():
  if name == 'nt':
    _ = system('cls')
  else:
       _ = system('clear')
while True:
  clear()
  print(Fore.WHITE+ """

  ───────────────────────────────────────────────────────────────────────────────────────
  ─██████████████─████████████──────────────────██████████─██████████████─██████─────────
  ─██░░░░░░░░░░██─██░░░░░░░░████────────────────██░░░░░░██─██░░░░░░░░░░██─██░░██─────────
  ─██░░██████░░██─██░░████░░░░██────────────────████░░████─██░░██████░░██─██░░██─────────
  ─██░░██──██░░██─██░░██──██░░██──────────────────██░░██───██░░██──██░░██─██░░██─────────
  ─██░░██████░░██─██░░██──██░░██─██████████████───██░░██───██░░██████░░██─██░░██─────────
  ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██───██░░██───██░░░░░░░░░░██─██░░██─────────
  ─██░░██████░░██─██░░██──██░░██─██████████████───██░░██───██░░██████████─██░░██─────────
  ─██░░██──██░░██─██░░██──██░░██──────────────────██░░██───██░░██─────────██░░██─────────
  ─██░░██──██░░██─██░░████░░░░██────────────────████░░████─██░░██─────────██░░██████████─
  ─██░░██──██░░██─██░░░░░░░░████────────────────██░░░░░░██─██░░██─────────██░░░░░░░░░░██─
  ─██████──██████─████████████──────────────────██████████─██████─────────██████████████─
  ───────────────────────────────────────────────────────────────────────────────────────
  """)
  print("")
  print(Fore.YELLOW+ "[1] lookup a ip address")
  print(Fore.YELLOW+ "[2] lookup a ip location")
  print(Fore.YELLOW+ "[3] ip location with google maps\n")


  option = input(Fore.RED+ "choose an option : ")
  if option == "1":
    print("")
    ip = input(Fore.GREEN+ "ip > ")
    access_token = '366073ca1b3e97'
    handler = ipinfo.getHandler(access_token)
    ip_address = ip
    details = handler.getDetails(ip_address)
    pprint.pprint(details.all)
    print("")
    input(Fore.WHITE+ "press ENTER to continue....")
  elif option == "2":
    print('')
    ip = input(Fore.GREEN+ "ip > ")
    access_token = '366073ca1b3e97'
    handler = ipinfo.getHandler(access_token)
    ip_address = ip
    details = handler.getDetails(ip_address)
    pprint.pprint(details.loc)
    print("")
    input(Fore.WHITE+ "press ENTER to continue....")
  elif option == "3":
    print('')
    ip = input(Fore.GREEN+ "ip > ")
    access_token = '366073ca1b3e97'
    handler = ipinfo.getHandler(access_token)
    ip_address = ip
    details = handler.getDetails(ip_address)
    pprint.pprint("loc : "+ details.loc)
    print("")
    print(Fore.CYAN+ "GOOGLE MAPS : "+ "https://www.google.com/maps/@"+ details.loc +",16z\n")
    gmap_id = "https://www.google.com/maps/@"+ details.loc +",16z"
    webbrowser.open(gmap_id)
    input(Fore.WHITE+ "press ENTER to continue....")
  