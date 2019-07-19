# -*- coding: utf-8 -*-
_build = '025'
_date = '07.19.2019'
import urllib.request, urllib.parse, urllib.error, urllib.request, time, os
print('pyos manager: checking for updates')
l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/manager.py'
save = urllib.request.urlretrieve(l, 't.txt')
r = open('t.txt')
words = r.read()
r.close()
if int(words[34:37]) > int(_build):
    urllib.request.urlretrieve(l, 'manager.py')
    print('Manager updated from b{} to b{}'.format(_build, words[34:37]))
elif int(words[34:37]) < int(_build):
    print('Update GitHub for manager (b{} to b{})'.format(words[34:37], _build))
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
    print('Update GitHub for variables (b{} to b{})'.format(words[34:37], other[34:37]))
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
    print('Update GitHub for main (b{} to b{})'.format(words[34:37], other[34:37]))
else:
    print('Main up to date (b{})'.format(other[34:37]))
input('Enter to boot pyos')
exec(open("main.py").read())