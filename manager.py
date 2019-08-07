# -*- coding: utf-8 -*-
_build = '036'
_hash = 'E13F8AAF31B9EBAE7C7AF4FD9E2682D0A4EEFBD6A99D285CF825D2EEFB063801'
_date = '08.07.2019'
import urllib.request, urllib.parse, urllib.error, urllib.request
print('pyos manager: checking for internet')
try:
    urllib.request.urlopen('http://216.58.192.142', timeout=1)
    check = 1
except urllib.error.URLError:
    check = 0
if check == 1:
    print('checking for updates')
    l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/manager.py'
    save = urllib.request.urlretrieve(l, 't.txt')
    r = open('t.txt')
    words = r.read()
    r.close()
    if int(words[34:37]) > int(_build):
        urllib.request.urlretrieve(l, 'manager.py')
        print('Manager updated from b{} to b{}'.format(_build, words[34:37]))
    elif int(words[34:37]) < int(_build):
        print('(DEV) Update GitHub for manager (b{} to b{})'.format(words[34:37], _build))
    else:
        print('Manager up to date (b{})'.format(_build))
    l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/variables.py'
    save = urllib.request.urlretrieve(l, 't.txt')
    r = open('t.txt')
    words = r.read()
    r.close()
    m = open('variables.py')
    other = m.read()
    m.close()
    if int(words[34:37]) > int(other[34:37]):
        urllib.request.urlretrieve(l, 'variables.py')
        print('Variables updated from b{} to b{}'.format(other[34:37], words[34:37]))
    elif int(words[34:37]) < int(other[34:37]):
        print('(DEV) Update GitHub for variables (b{} to b{})'.format(words[34:37], other[34:37]))
    else:
        print('Variables up to date (b{})'.format(other[34:37]))
    l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/main.py'
    save = urllib.request.urlretrieve(l, 't.txt')
    r = open('t.txt')
    words = r.read()
    r.close()
    m = open('main.py')
    other = m.read()
    m.close()
    if int(words[34:37]) > int(other[34:37]):
        urllib.request.urlretrieve(l, 'main.py')
        print('Main updated from b{} to b{}'.format(other[34:37], words[34:37]))
    elif int(words[34:37]) < int(other[34:37]):
        print('(DEV) Update GitHub for main (b{} to b{})'.format(words[34:37], other[34:37]))
    else:
        print('Main up to date (b{})'.format(other[34:37]))
    input('Enter to boot pyos')
else:
    print('no internet')
exec(open("main.py").read())
