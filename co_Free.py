# coding: utf-8
#Coded By Dm_Hack3ng.py

import all_co_donw
import requests


finder=all_co_donw.Finder()

try:
	finder.find_all_course()
except requests.exceptions.ConnectionError:
	print("[+] Pas de connexion Internet")
	finder.banner()
except KeyboardInterrupt:
	print("[+] Detection de Ctrl+C ... Fin du Programme")
	finder.banner()