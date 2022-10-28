#!/bin/python3

import requests, time

x = requests.get('http://10.10.100.200:40589/number/')

blow = x.content

tango = blow.decode('utf-8')

#print(tango)
r = requests.get(f'http://10.10.100.200:40589/number/?answer={tango}')
print(r.content.decode('utf-8'))
