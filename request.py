#!/bin/python3
# I created this script in order to successfully complete a challenge on a CTF I was participating in
# MEISTSEC
# 10/2022

import requests

x = requests.get('http://10.10.100.200:40589/number/')

blow = x.content

tango = blow.decode('utf-8')

#print(tango)
r = requests.get(f'http://10.10.100.200:40589/number/?answer={tango}')
print(r.content.decode('utf-8'))
