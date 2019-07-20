# -*- coding: utf-8 -*-
_build = '141'
print('\033[2J\033[H[001] [0.00000000] boot: starting, getting time')
import time
starttime = time.time()
print('[002] [{:.08f}] boot: loading version'.format(time.time() - starttime))
_counter = 3
_version = '1.6.3.0'
_date = '07.19.19'
print('[{:03d}] [{:.8f}] pyos {}.{} ({})'.format(_counter, time.time() - starttime, _version, _build, _date))
_counter += 1
print('[{:03d}] [{:.8f}] boot: Loading random'.format(_counter, time.time() - starttime))
_counter += 1
import random
print('[{:03d}] [{:.8f}] boot: Loading sys'.format(_counter, time.time() - starttime))
_counter += 1
import sys
print('[{:03d}] [{:.8f}] boot: Loading hashlib'.format(_counter, time.time() - starttime))
_counter += 1
import hashlib
print('[{:03d}] [{:.8f}] boot: Loading urllib'.format(_counter, time.time() - starttime))
_counter += 1
import urllib.request, urllib.error, urllib.parse
print('[{:03d}] [{:.8f}] boot: Loading platform'.format(_counter, time.time() - starttime))
_counter += 1
import platform
print('[{:03d}] [{:.8f}] boot: Loading variables'.format(_counter, time.time() - starttime))
_counter += 1
import variables
print('[{:03d}] [{:.8f}] boot: {}{} {} {}'.format(_counter, time.time() - starttime, platform.machine(), platform.processor(), platform.system(), variables.iflinux()))
_counter += 1
print('[{:03d}] [{:.8f}] boot: Checking internet connection'.format(_counter, time.time() - starttime))
_counter += 1
if variables.check() == True:
    _internet = True
    print('[{:03d}] [{:.8f}] boot: Internet connection succeeded'.format(_counter, time.time() - starttime))
    _counter += 1
else:
    _internet = False
    print('[{:03d}] [{:.8f}] boot: Internet connection failed'.format(_counter, time.time() - starttime))
    _counter += 1
print('[{:03d}] [{:.8f}] boot: Loading builtins'.format(_counter, time.time() - starttime))
_counter += 1
h_n = ''
s_w = 0
s_x = 0
s_n = 0
c_versioning = '1.6.5'
c_build = '37'
c_date = '051519'
c_right = 0
c_wrong = 0
c_total = c_right + c_wrong
c_ans = 'x'
print('[{:03d}] [{:.8f}] boot: Setting up login info'.format(_counter, time.time() - starttime))
_counter += 1
users = ['root', 'temp']
passwords = ['root']
print('[{:03d}] [{:.8f}] boot: Setting up pysh info'.format(_counter, time.time() - starttime))
_counter += 1
_path = 'main'
_user = ''
print('[{:03d}] [{:.08f}] {}: Loading login'.format(_counter, time.time() - starttime, _path))
_counter += 1
user = input('usr: ')
_path = 'login'
starttime = time.time()
print('[{:03d}] [{:.08f}] {}: Checking username'.format(_counter, time.time() - starttime, _path))
_counter += 1
if user == users[1]:
    _user = 'temp'
    print('[{:03d}] [{:.08f}] {}: Logged in as temp'.format(_counter, time.time() - starttime, _path))
    _counter += 1
elif user == users[0]:
    passw = input('psw: ')
    starttime = time.time()
    print('[{:03d}] [{:.08f}] {}: Checking password'.format(_counter, time.time() - starttime, _path))
    _counter += 1
    if passw in passwords:
        if passw == passwords[0]:
            _user = 'root'
            print('[{:03d}] [{:.08f}] {}: Logged in as root'.format(_counter, time.time() - starttime, _path))
            _counter += 1
        else:
            print('[{:03d}] [{:.08f}] {}: Wrong password; setting to temp'.format(_counter, time.time() - starttime, _path))
            _counter += 1
            _user = 'temp'
    else:
        print('[{:03d}] [{:.08f}] {}: Wrong password; setting to temp'.format(_counter, time.time() - starttime, _path))
        _counter += 1
        _user = 'temp'
else:
    print('[{:03d}] [{:.08f}] {}: Username doesn\'t exist; setting to temp'.format(_counter, time.time() - starttime, _path))
    _counter += 1
    _user = 'temp'
print('[{:03d}] [{:.08f}] {}: Loading pysh (1.0.6)'.format(_counter, time.time() - starttime, _path))
_counter += 1
if _user == 'root':
    _path = 'root/'
    paths = ['root/']
else:
    _path = 'temp/'
    paths = ['temp/']
cmdlist = ['start','exit', 'rb', 'cd','md','ls','pd','cf','cl', 'help', 'cotw', 'scan', 'hash', 'cat', 'edit', 'del']
filedict = {}
waiting = 0
added = []
print('[{:03d}] [{:.08f}] {}: Ready'.format(_counter, time.time() - starttime, _path[:-1]))
_counter += 1
entered = 'start'
if entered == 'start':
    while entered != 'exit':
        entered = input('{} '.format(_path))
        entered = entered.split()
        for x in entered:
            if x in cmdlist:
                if waiting == 0:
                    if x == 'ls':
                        for i in paths:
                            if i.startswith(_path) and len(i) > len(_path):
                                temp = len(_path)
                                splitted = i[temp:].split('/')
                                if len(splitted) > 1 and (splitted[0] + '/') not in added:
                                    print(splitted[0] + '/')
                                    added.append(splitted[0] + '/')
                                elif len(splitted) < 2 and splitted[0] not in added:
                                    print(splitted[0])
                                    added.append(splitted[0])
                                else:
                                    pass
                            else:
                                pass
                    elif x == 'pd':
                        print(_path)
                    elif x == 'cd':
                        waiting = 1
                    elif x == 'md':
                        waiting = 2
                    elif x == 'cf':
                        waiting = 3
                    elif x == 'cat':
                        waiting = 4
                    elif x == 'edit':
                        waiting = 5
                    elif x == 'del':
                        waiting = 6
                    elif x == 'start':
                        print('already in pysh')
                    elif x == 'cotw':
                        variables.cotw(c_countries, c_answers, c_versioning, c_build, c_date, c_right, c_wrong, c_total, c_ans)
                    elif x == 'scan':
                        variables.scan(s_w, s_x, s_n)
                    elif x == 'hash':
                        variables.thsh(h_char, h_n)
                    elif x == 'help':
                        print('exit: exit pyos\nrb: reboot pyos\ncd $: change directory to $\nmd $: create directory $\nls: list contents of current directory\npd: print working directory (useless)\ncf $: create file $\ncat $: print contents of $\ndel $: delete file $\nedit $: edit file $\ncl: clear screen\nhelp: show this\ncotw: start countriesoftheworld\nscan: start utf8scan6\nhash: start hash converter')
                    elif x == 'cl':
                        sys.stdout.write('\x1b[2J\x1b[H')
                    elif x == 'rb':
                        raise SystemExit
                    else:
                        sys.exit()
                else:
                    print('pyos: pysh: consecutive cmd {}'.format(x))
            else:
                if waiting == 1:
                    if x == '..':
                        _path = _path[:-1].rsplit('/',1)[0] + '/'
                    else:
                        if _path + x + '/' in paths:
                            _path = _path + x + '/'
                        elif x.endswith('/'):
                            if _path + x in paths:
                                _path = _path + x
                            else:
                                print('pyos: pysh: path \'{}\' not found'.format(x))
                        else:
                            print('pyos: pysh: can\'t cd to file \'{}\''.format(x))
                    waiting = 0
                elif waiting == 2:
                    if x.endswith('/'):
                        paths.append(_path + x)
                    else:
                        paths.append(_path + x + '/')
                    waiting = 0
                elif waiting == 3:
                    if x.endswith('/'):
                        paths.append(_path + x - '/')
                    else:
                        paths.append(_path + x)
                    filedict[x] = ''
                    waiting = 0
                elif waiting == 4:
                    try:
                        print(filedict[x])
                    except KeyError as err:
                        print('pyos: pysh: file {} doesn\'t exist'.format(x))
                    waiting = 0
                elif waiting == 5:
                    e = input(filedict[x])
                    filedict[x] = filedict[x] + e
                    waiting = 0
                elif waiting == 6:
                    del filedict[x]
                    waiting = 0
                    for j in paths:
                        if x in j:
                            paths.remove(j)
                        else:
                            pass
                    if x in _path:
                        _path = paths[0]
                    else:
                        pass
                else:
                    print('pyos: pysh: {} not found.'.format(x))
                    waiting = 0
else:
    print('pyos: {} not found'.format(entered))