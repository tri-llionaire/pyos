# -*- coding: utf-8 -*-
_build = '300'
print('setting up boot requirements')
import subprocess, platform
red = ''
green = ''
yellow = ''
blue = ''
magenta = ''
cyan = ''
white = ''
term = 'cls'
if platform.system() == 'Linux':
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[0m'
    term = 'clear'
tmp = subprocess.call(term, shell=True)
print('[001] [0.00000000] boot: starting, getting time')
import time
starttime = time.time()
print('[002] [{:.8f}] boot: on {}{}{}{}{}'.format(time.time() - starttime, platform.system(), platform.release(), platform.version(), platform.machine(), platform.node()))
print('[003] [{:.8f}] boot: loading sys'.format(time.time() - starttime))
import sys
print('[004] [{:.8f}] boot: loading internetcheck'.format(time.time() - starttime))
from variables import check
print('[005] [{:.8f}] boot: loading hashing'.format(time.time() - starttime))
from variables import hashing
print('[006] [{:.8f}] boot: loading scan'.format(time.time() - starttime))
from variables import scan
print('[007] [{:.8f}] boot: loading cotw'.format(time.time() - starttime))
from variables import cotw
print('[008] [{:.8f}] boot: loading cotw'.format(time.time() - starttime))
from variables import stock
print('[009] [{:.8f}] boot: loading date'.format(time.time() - starttime))
import datetime
print('[010] [{:.8f}] boot: loading getpass'.format(time.time() - starttime))
import getpass
print('[011] [{:.8f}] boot: checking internet connection'.format(time.time() - starttime))
if check.check() is True:
    _internet = ''
    print('[012] [{:.8f}] boot: internet connection succeeded'.format(time.time() - starttime))
    print('[013] [{:.8f}] boot: loading urllib'.format(time.time() - starttime))
    import urllib
    print('[014] [{:.8f}] boot: loading landrum weather'.format(time.time() - starttime))
    urllib.request.urlretrieve('http://api.openweathermap.org/data/2.5/weather?q=Landrum&APPID=b35975e18dc93725acb092f7272cc6b8&units=imperial', 't.txt')
    z = open('t.txt')
    p = z.read().split('\"')
    z.close()
    print('[015] [{:.8f}] boot: loading cnn headlines'.format(time.time() - starttime))
    urllib.request.urlretrieve('https://lite.cnn.io/en', 't.txt')
    q = open('t.txt')
    v = q.read().split('\">')
    q.close()
    print('[016] [{:.8f}] boot: completed, loading login'.format(time.time() - starttime))
else:
    _internet = '{}No '.format(green)
    print('[012] [{:.8f}] boot: internet connection failed'.format(time.time() - starttime))
    print('[013] [{:.8f}] boot: completed, loading login'.format(time.time() - starttime))
sys.stdout.write('\nPPPPP Y   Y OOOOO SSSSS 33333\nP   P  Y Y  O   O S         3\nPPPPP   Y   O   O SSSSS 33333\nP       Y   O   O     S     3\nP       Y   OOOOO SSSSS 33333\n\nCCC OOO L   DD    CCC OOO W W\nC   O O L   DDD   C   O O WWW\nCCC OOO LLL DDD   CCC OOO WWW\n\n\n        login\n')
_user = input('        usr: ')
_pswd = getpass.getpass(prompt='        pwd: ')
cmdlist = ['start', 'exit', 'rb', 'cd', 'md', 'ls', 'pd', 'cf', 'cl', 'help', 'cotw', 'scan', 'hash', 'cat', 'edit', 'del', 'news', 'time', 'weather', 'pystocks', 'p', 'chusr']
filedict = {}
waiting = 0
addi = ''
added = []
varis = {}
tmp = subprocess.call(term, shell=True)
print('pyos 3.4.4.8 cold cow {}.057.075 08.20.19 @tri-llionaire with @dentafrice, @Akuhcap'.format(_build))
if _user == 'root' and _pswd == 'root':
    _path = 'root/'
    paths = ['root/']
else:
    sys.stdout.write('Incorrect ')
    _path = 'temp/'
    paths = ['temp/']
print('Login at {}{} UTC\n{}{}Internet connection\n{}Weather in Landrum: {}{}F{} and {}{}{} (humidity {}{}%{}, wind speed {}{}mph{})\n{}{}\n{}{}\n{}{}\n{}{}\n{}{}{}'.format(red, datetime.datetime.now(), green, _internet, white, yellow, p[30][1:-1], white, blue, p[13], white, magenta, p[34][1:-1], white, cyan, p[44][1:-1], white, green, v[9][:-68].replace('&#x27;', ''), yellow, v[10][:-68].replace('&#x27;', ''), blue, v[11][:-68].replace('&#x27;', ''), magenta, v[12][:-68].replace('&#x27;', ''), cyan, v[13][:-68].replace('&#x27;', ''), white))
sys.stdout.write('(pysh 1.2.7) ')
entered = 'start'
if entered == 'start':
    while entered != 'exit':
        entered = input('{}{} '.format(_path, addi))
        entered = entered.split()
        for x in entered:
            if x in cmdlist:
                if waiting == 0:
                    if x == 'ls':
                        for i in paths:
                            if _path in paths:
                                if i.startswith(_path) and len(i) > len(_path):
                                    print(i[len(_path):])
                                    
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
                        cotw.cotw(cotw.c_countries, cotw.c_answers, '0')
                    elif x == 'scan':
                        scan.scan('0', '0')
                    elif x == 'hash':
                        hashing.thsh(hashing.h_char, '0')
                    elif x == 'help':
                        print('exit: exit pyos\nrb: reboot pyos\ncd $: change directory to $\nmd $: create directory $\nls: list contents of current directory\npd: print working directory (useless)\ncf $: create file $\ncat $: print contents of $\ndel $: delete file $\nedit $: edit file $\ncl: clear screen\nhelp: show this\ncotw($): start countriesoftheworld with optional parameters for settings\nscan($)($): start utf8scan6 with optional parameters for settings and hashes\nhash($): start hash converter with optional parameters for hashes\ntime: get current time\nweather: get current weather\nnews: get current news\npystocks: stocks game\np $: set prompt to $\nchusr: change user\n:$: exec($)\n$$ = $: set variable $ to $ (run with !$)')
                    elif x == 'cl':
                        tmp = subprocess.call(term, shell=True)
                    elif x == 'rb':
                        exec(open('manager.py').read())
                    elif x == 'time':
                        print('{} UTC'.format(datetime.datetime.now()))
                    elif x == 'weather':
                        print('Weather in Landrum: {}F and {} (humidity {}%, wind speed {}mph)'.format(p[30][1:-1], p[13], p[34][1:-1], p[44][1:-1]))
                    elif x == 'news':
                        print('{}{}\n{}{}\n{}{}\n{}{}\n{}{}{}'.format(green, v[9][:-68].replace('&#x27;', ''), yellow, v[10][:-68].replace('&#x27;', ''), blue, v[11][:-68].replace('&#x27;', ''), magenta, v[12][:-68].replace('&#x27;', ''), cyan, v[13][:-68].replace('&#x27;', ''), white))
                    elif x == 'pystocks':
                        stock.stocks()
                    elif x == 'p':
                        waiting = 7
                    elif x == 'chusr':
                        _user = input('usr: ')
                        _pswd = getpass.getpass(prompt='pwd: ')
                        if _user == 'root' and _pswd == 'root':
                            _path = 'root/'
                            paths = ['root/']
                        else:
                            print('Incorrect Login')
                            _path = 'temp/'
                            paths = ['temp/']
                    else:
                        sys.exit()
                else:
                    print('pyos: pysh: consecutive cmd {}'.format(x))
            else:
                if x.startswith('!'):
                    print(varis[x[1:]])
                elif waiting == 1:
                    if x == '..':
                        _path = _path[:-1].rsplit('/', 1)[0] + '/'
                    else:
                        if _path + x in paths:
                            _path = _path + x
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
                        print('pyos: pysh: {} not a valid directory name'.format(x))
                    waiting = 0
                elif waiting == 3:
                    if x.endswith('/'):
                        print('pyos: pysh: {} not a valid file name'.format(x))
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
                    if x in _path:
                        _path = paths[0]
                elif waiting == 7:
                    addi = x
                    waiting = 0
                elif waiting == 8:
                    if x == '=':
                        waiting = 9
                    else:
                        print('pyos: pysh: not a valid variable assignment')
                        waiting = 0
                elif waiting == 9:
                    varis[t] = x
                    waiting = 0
                elif x.startswith('scan'):
                    valid1 = ['3', '4', '5']
                    valid2 = ['1', '2']
                    valid3 = ['md5', 'sha1', 't-hash', 'sha256', 'sha384', 'sha512']
                    if x[4] in valid1 and x[5:] in valid3:
                        scan.scan(x[4], x[5:])
                    elif x[4] in valid2:
                        scan.scan(x[4], '0')
                    else:
                        scan('0', '0')
                elif x.startswith('cotw'):
                    valid1 = ['1', '2']
                    if x[4] in valid1:
                        cotw.cotw(c_countries, c_answers, x[4])
                    else:
                        cotw.cotw(c_countries, c_answers, '0')
                elif x.startswith('hash'):
                    valid2 = ['md5', 'sha1', 't-hash', 'sha256', 'sha384', 'sha512']
                    if x[4:] in valid2:
                        hashing.thsh(h_char, x[4:])
                    else:
                        hashing.thsh(h_char, '0')
                elif x.startswith('$'):
                    waiting = 8
                    t = x[1:]
                elif x.startswith(':'):
                    exec(x[1:])
                else:
                    print('pyos: pysh: {} not found.'.format(x))
                    waiting = 0
