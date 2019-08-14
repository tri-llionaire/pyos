# -*- coding: utf-8 -*-
_build = '234'
import subprocess, platform
red = ''
green = ''
other = ''
white = ''
term = 'cls'
if platform.system() == 'Linux':
    red = '\033[91m'
    green = '\033[92m'
    other = '\033[95m'
    white = '\033[0m'
    term = 'clear'
tmp = subprocess.call(term, shell=True)
print('[001] [0.00000000] boot: starting, getting time')
import time
starttime = time.time()
print('[002] [{:.8f}] boot: loading sys'.format(time.time() - starttime))
import sys
print('[003] [{:.8f}] boot: loading variables'.format(time.time() - starttime))
import variables
print('[004] [{:.8f}] boot: loading datetime'.format(time.time() - starttime))
import datetime
print('[005] [{:.8f}] boot: on {}{}{}{}{}'.format(time.time() - starttime, platform.system(), platform.release(), platform.version(), platform.machine(), platform.node()))
print('[006] [{:.8f}] boot: checking internet connection'.format(time.time() - starttime))
if variables.check() is True:
    _internet = ''
    print('[007] [{:.8f}] boot: internet connection succeeded'.format(time.time() - starttime))
else:
    _internet = 'No '
    print('[007] [{:.8f}] boot: internet connection failed'.format(time.time() - starttime))
    print('[008] [{:.8f}] boot: loading login'.format(time.time() - starttime))
sys.stdout.write('\n\nPPPPP Y   Y OOOOO SSSSS 33333\nP   P  Y Y  O   O S         3\nPPPPP   Y   O   O SSSSS 33333\nP       Y   O   O     S     3\nP       Y   OOOOO SSSSS 33333\n\n\n        login\n')
_user = input('        usr: ')
_pswd = input('        pwd: ')
cmdlist = ['start', 'exit', 'rb', 'cd', 'md', 'ls', 'pd', 'cf', 'cl', 'help', 'cotw', 'scan', 'hash', 'cat', 'edit', 'del']
filedict = {}
waiting = 0
added = []
tmp = subprocess.call(term, shell=True)
print('pyos 3.3.0.3 234.043.071 08.14.19 Price et al Mingle, Swan')
if _user == 'root' and _pswd == 'root':
    _path = 'root/'
    paths = ['root/']
else:
    sys.stdout.write('(Incorrect login) ')
    _path = 'temp/'
    paths = ['temp/']
print('Last login at {} UTC\n{}Internet connection'.format( datetime.datetime.now(), _internet))
sys.stdout.write('(pysh 1.1.1) ')
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
                        variables.cotw(variables.c_countries, variables.c_answers, '0')
                    elif x == 'scan':
                        variables.scan('0', '0')
                    elif x == 'hash':
                        variables.thsh(variables.h_char, '0')
                    elif x == 'help':
                        print('exit: exit pyos\nrb: reboot pyos\ncd $: change directory to $\nmd $: create directory $\nls: list contents of current directory\npd: print working directory (useless)\ncf $: create file $\ncat $: print contents of $\ndel $: delete file $\nedit $: edit file $\ncl: clear screen\nhelp: show this\ncotw(x): start countriesoftheworld with optional parameters for settings\nscan(x)(x): start utf8scan6 with optional parameters for settings and hashes\nhash(x): start hash converter with optional parameters for hashes')
                    elif x == 'cl':
                        tmp = subprocess.call(term, shell=True)
                    elif x == 'rb':
                        exec(open('manager.py').read())
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
                elif x.startswith('scan'):
                    valid1 = ['3', '4', '5']
                    valid2 = ['1', '2']
                    valid3 = ['md5', 'sha1', 't-hash', 'sha256', 'sha384', 'sha512']
                    if x[4] in valid1 and x[5:] in valid3:
                        variables.scan(x[4], x[5:])
                    elif x[4] in valid2:
                        variables.scan(x[4], '0')
                    else:
                        variables.scan('0', '0')
                elif x.startswith('cotw'):
                    valid1 = ['1', '2']
                    if x[4] in valid1:
                        variables.cotw(variables.c_countries, variables.c_answers, x[4])
                    else:
                        variables.cotw(variables.c_countries, variables.c_answers, '0')
                elif x.startswith('hash'):
                    valid2 = ['md5', 'sha1', 't-hash', 'sha256', 'sha384', 'sha512']
                    if x[4:] in valid2:
                        variables.thsh(variables.h_char, x[4:])
                    else:
                        variables.thsh(variables.h_char, '0')
                else:
                    print('pyos: pysh: {} not found.'.format(x))
                    waiting = 0
