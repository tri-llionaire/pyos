# -*- coding: utf-8 -*-
_build = '199'
_hash = '41BA268600D537A977074A3B706988CFFE3C32365325892A8FCB02BF5F39E29C'
_version = '3.1.3.3'
_date = '08.11.19'
_counter = 1
gr = input('(g)raphic/(t)erminal startup: ')
import subprocess, data
tmp = subprocess.call(data.term, shell=True)
if gr == 't':
    print('[{:03d}] [0.00000000] boot: starting, getting time'.format(_counter))
    _counter += 1
    import time
    starttime = time.time()
    print('[{:03d}] [{:.8f}] boot: loading sys'.format(_counter, time.time() - starttime))
    _counter += 1
    import sys
    print('[{:03d}] [{:.8f}] boot: loading variables'.format(_counter, time.time() - starttime))
    _counter += 1
    import variables
    print('[{:03d}] [{:.8f}] boot: loading platform'.format(_counter, time.time() - starttime))
    _counter += 1
    import platform
    print('[{:03d}] [{:.8f}] boot: on {}'.format(_counter, time.time() - starttime, platform.uname()))
    _counter += 1
    print('[{:03d}] [{:.8f}] boot: checking internet connection'.format(_counter, time.time() - starttime))
    _counter += 1
    if variables.check() is True:
        _internet = True
        print('[{:03d}] [{:.8f}] boot: internet connection succeeded'.format(_counter, time.time() - starttime))
        _counter += 1
    else:
        _internet = False
        print('[{:03d}] [{:.8f}] boot: internet connection failed'.format(_counter, time.time() - starttime))
        _counter += 1
    print('[{:03d}] [{:.8f}] boot: loading login'.format(_counter, time.time() - starttime))
    _user = input('usr: ')
    _pswd = input('pwd: ')
else:
    import time, sys, variables, platform
    sys.stdout.write('PPPP Y  Y OOOO SSSS 3333\nP  P  YY  O  O SS   3333\nPPPP   Y  O  O   SS    3\nP      Y  OOOO SSSS 3333\n\n\n        login\n')
    _user = input('        usr: ')
    _pswd = input('        pwd: ')
if _user == 'root' and _pswd == 'root':
    _path = 'root/'
    paths = ['root/']
else:
    print('incorrect login')
    _path = 'temp/'
    paths = ['temp/']
print('\n\n\n')
cmdlist = ['start', 'exit', 'rb', 'cd', 'md', 'ls', 'pd', 'cf', 'cl', 'help', 'cotw', 'scan', 'hash', 'cat', 'edit', 'del']
filedict = {}
waiting = 0
added = []
tmp = subprocess.call(data.term, shell=True)
print('pyos 3.1.3.1 194.021.041 08.11.19 Price et al Mingle, Swan')
sys.stdout.write('(pysh 1.0.6) ')
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
                        variables.cotw(variables.c_countries, variables.c_answers)
                    elif x == 'scan':
                        variables.scan()
                    elif x == 'hash':
                        variables.thsh(variables.h_char)
                    elif x == 'help':
                        print('exit: exit pyos\nrb: reboot pyos\ncd $: change directory to $\nmd $: create directory $\nls: list contents of current directory\npd: print working directory (useless)\ncf $: create file $\ncat $: print contents of $\ndel $: delete file $\nedit $: edit file $\ncl: clear screen\nhelp: show this\ncotw: start countriesoftheworld\nscan: start utf8scan6\nhash: start hash converter')
                    elif x == 'cl':
                        tmp = subprocess.call(data.term, shell=True)
                    elif x == 'rb':
                        exec(open('main.py').read())
                    else:
                        sys.exit()
                else:
                    print('pyos: pysh: consecutive cmd {}'.format(x))
            else:
                if waiting == 1:
                    if x == '..':
                        _path = _path[:-1].rsplit('/', 1)[0] + '/'
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
                    except KeyError:
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
