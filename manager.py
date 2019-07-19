# -*- coding: utf-8 -*-
_build = '009'
_date = '07.19.2019'
import urllib.request, urllib.parse, urllib.error, urllib.request
print('pyos manager: checking for updates')
l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/manager.py'
save = urllib.request.urlretrieve(l, 't.txt')
r = open('t.txt')
words = r.read()
r.close()
if int(words[34:37]) > int(_build):
    urllib.request.urlretrieve(l, 'manager{}.py'.format(words[34:37]))
    print('Manager updated from b{} to b{}'.format(_build, words[34:37]))
elif int(words[34:37]) < int(_build):
    print('Update GitHub for manager')
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
    urllib.request.urlretrieve(l, 'variables{}.py'.format(words[34:37]))
    print('Variables updated from b{} to b{}'.format(_build, words[34:37]))
elif int(words[34:37]) < int(other[34:37]):
    print('Update GitHub for variables')
else:
    print('Variables up to date (b{})'.format(_build))
l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/main.py'
save = urllib.request.urlretrieve(l, 't.txt')
r = open('t.txt')
words = r.read()
r.close()
m = open('main.py')
other = m.read()
m.close()
if int(words[34:37]) > int(other[34:37]):
    urllib.request.urlretrieve(l, 'main{}.py'.format(words[34:37]))
    print('Main updated from b{} to b{}'.format(_build, words[34:37]))
elif int(words[34:37]) < int(other[34:37]):
    print('Update GitHub for main')
else:
    print('Main up to date (b{})'.format(_build))