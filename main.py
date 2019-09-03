# -*- coding: utf-8 -*-
_build = '354'
try:
    print('loading time')
    import time
    starttime = time.time()
    n = open('log', 'a+')
    n.write('started main log\n')
    print('[{:.8f}] boot: loading platform'.format(time.time() - starttime))
    import platform
    n.write('[{:.8f}] status: platform loaded')
    print('[{:.8f}] boot: loading terminal commands'.format(time.time() - starttime))
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
    n.write('[{:.8f}] status: terminal commands loaded\n')
    print('[{:.8f}] boot: on {}{}{}{}{}'.format(time.time() - starttime, platform.system(), platform.release(), platform.version(), platform.machine(), platform.node()))
    print('[{:.8f}] boot: loading subprocess'.format(time.time() - starttime))
    import subprocess
    print('[{:.8f}] boot: loading sys'.format(time.time() - starttime))
    import sys
    print('[{:.8f}] boot: loading internetcheck'.format(time.time() - starttime))
    from variables import check
    print('[{:.8f}] boot: loading hashing'.format(time.time() - starttime))
    from variables import hashing
    print('[{:.8f}] boot: loading scan'.format(time.time() - starttime))
    from variables import scan
    print('[{:.8f}] boot: loading cotw'.format(time.time() - starttime))
    from variables import cotw
    print('[{:.8f}] boot: loading stock'.format(time.time() - starttime))
    from variables import stock
    print('[{:.8f}] boot: loading clocking'.format(time.time() - starttime))
    from variables import clock
    print('[{:.8f}] boot: loading convert'.format(time.time() - starttime))
    from variables import convert
    print('[{:.8f}] boot: loading date'.format(time.time() - starttime))
    import datetime
    print('[{:.8f}] boot: loading getpass'.format(time.time() - starttime))
    import getpass
    print('[{:.8f}] boot: loading hashlib'.format(time.time() - starttime))
    import hashlib
    print('[{:.8f}] boot: loading data'.format(time.time() - starttime))
    y = open('data', 'r')
    data = y.read()
    y.close()
    print('[{:.8f}] boot: checking internet connection'.format(time.time() - starttime))
    if check.check() is True:
        _internet = ''
        print('[{:.8f}] boot: internet connection succeeded'.format(time.time() - starttime))
        print('[{:.8f}] boot: loading urllib'.format(time.time() - starttime))
        import urllib
        print('[{:.8f}] boot: loading landrum weather'.format(time.time() - starttime))
        urllib.request.urlretrieve('http://api.openweathermap.org/data/2.5/weather?q=Landrum&APPID=b35975e18dc93725acb092f7272cc6b8&units=imperial', 'cache')
        print('[{:.8f}] boot: loading cache weather'.format(time.time() - starttime))
        z = open('cache', 'r')
        p = z.read().split('\"')
        z.close()
        print('[{:.8f}] boot: loading cnn headlines'.format(time.time() - starttime))
        urllib.request.urlretrieve('https://lite.cnn.io/en', 'cache')
        print('[{:.8f}] boot: loading cache headlines'.format(time.time() - starttime))
        q = open('cache', 'r')
        v = q.read().split('\">')
        q.close()
        print('[{:.8f}] boot: completed, loading login'.format(time.time() - starttime))
    else:
        _internet = '{}No '.format(green)
        print('[{:.8f}] boot: internet connection failed'.format(time.time() - starttime))
        print('[{:.8f}] boot: completed, loading login'.format(time.time() - starttime))
    sys.stdout.write('\nPPPPP Y   Y OOOOO SSSSS 4   4\nP   P  Y Y  O   O S     4   4\nPPPPP   Y   O   O SSSSS 44444\nP       Y   O   O     S     4\nP       Y   OOOOO SSSSS     4\n\nDDD AAA N N K K   DDD OOO GGG\nD D A A NNN KK    D D O O GG\nDDD A A N N K K   DDD OOO GGG\n\n\n        login\n')
    _user = input('        usr: ')
    _pswd = getpass.getpass(prompt='        pwd: ')
    cmdlist = ['start', 'exit', 'rb', 'cd', 'md', 'ls', 'pd', 'cf', 'cl', 'help', 'cotw', 'scan', 'hash', 'cat', 'edit', 'news', 'time', 'weather', 'stocks', 'prompt', 'chusr', 'rbu', 'date', '#time', '#log', '#imp', '#emp', '#get', '#del', 'timer', 'stopwatch', 'rn', '#addusr']
    filedict = {}
    waiting = 0
    addi = ''
    added = []
    varis = {}
    _path = ''
    paths = []
    tmp = subprocess.call(term, shell=True)
    for j in data.split('&'):
        if j.split('/')[0] == _user:
            if j.split('/')[1] == hashlib.sha256(_pswd.encode()).hexdigest():
                _path = _user + '/'
                paths = [_user + '/']
    if _path == '':
        _path = 'temp/'
        paths = ['temp/']
    print('pyos 4.0.3.5 dank dog {}.74.94 09.03.19 @tri-llionaire with @dentafrice, @Akuhcap\nLogin at {}{} UTC\n{}{}Internet connection\n{}{}F{} and {}{}{} (humidity {}{}%{}, wind speed {}{}mph{})\n{}{}\n{}{}\n{}{}\n{}{}\n{}{}{}'.format(_build, red, datetime.datetime.now(), green, _internet, yellow, p[30][1:-1], white, blue, p[13], white, magenta, p[34][1:-1], white, cyan, p[44][1:-1], white, green, v[9][:-68].replace('&#x27;', ''), yellow, v[10][:-68].replace('&#x27;', ''), blue, v[11][:-68].replace('&#x27;', ''), magenta, v[12][:-68].replace('&#x27;', ''), cyan, v[13][:-68].replace('&#x27;', ''), white))
    sys.stdout.write('(pysh 1.3.3) ')
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
                        elif x == '#del':
                            if _user == 'root':
                                waiting = 6
                            else:
                                print('pyos: pysh: permission denied')
                        elif x == 'start':
                            print('already in pysh')
                        elif x == 'cotw':
                            cotw.cotw(cotw.c_countries, cotw.c_answers, '0')
                        elif x == 'scan':
                            scan.scan('0', '0')
                        elif x == 'hash':
                            hashing.thsh(hashing.h_char, '0')
                        elif x == 'help':
                            print('help: show this\nexit: exit pyos\nrb: reboot main\nrbu: reboot and check for update\ncd $: change directory to $\nmd $: create directory $\nls: list contents of current directory\npd: print working directory\ncf $: create file $\ncat $: print contents of $\nedit $: edit file $\ncl: clear screen\ncotw($): start countriesoftheworld with optional parameters for settings\nscan($)($): start utf8scan6 with optional parameters for settings and hashes\nhash($): start hash converter with optional parameters for hashes\ntime: get current unix time\ndate: get current utc time\nweather: get current weather\nnews: get current news\nstocks: stocks game\nprompt $: set prompt to $\nchusr: change user\n$$ = $: set variable $ to $ (run with !$)\ntimer $: set a timer for $ seconds\nstopwatch: run a stopwatch\nrn $ $: rename $ to $\nbase: base converter')
                            if _user == 'root':
                                print(':$: exec $\n#time: system runtime\n#log: view syslog\n#imp $: import file $ from base os\n#exp $: export file $ to base os\n#get $ $: save webpage $ as $\n#del $: delete file/directory $\n#addusr: add a user')
                        elif x == 'cl':
                            tmp = subprocess.call(term, shell=True)
                        elif x == 'rb':
                            exec(open('main.py', 'r').read())
                        elif x == 'rbu':
                            exec(open('manager.py', 'r').read())
                        elif x == 'date':
                            print('{} UTC'.format(datetime.datetime.now()))
                        elif x == 'time':
                            print(time.time())
                        elif x == 'weather':
                            urllib.request.urlretrieve('http://api.openweathermap.org/data/2.5/weather?q=Landrum&APPID=b35975e18dc93725acb092f7272cc6b8&units=imperial', 'cache')
                            z = open('cache', 'r')
                            p = z.read().split('\"')
                            z.close()
                            k = '{}{}F{} and {}{}{} (humidity {}{}%{}, wind speed {}{}mph{})'.format(yellow, p[30][1:-1], white, blue, p[13], white, magenta, p[34][1:-1], white, cyan, p[44][1:-1], white)
                            print(k)
                            n.write('[{:.8f}] pysh: {}'.format(time.time() - starttime, k))
                        elif x == 'news':
                            q = open('cache', 'r')
                            v = q.read().split('\">')
                            q.close()
                            k = '{}{}\n{}{}\n{}{}\n{}{}\n{}{}{}'.format(green, v[9][:-68].replace('&#x27;', ''), yellow, v[10][:-68].replace('&#x27;', ''), blue, v[11][:-68].replace('&#x27;', ''), magenta, v[12][:-68].replace('&#x27;', ''), cyan, v[13][:-68].replace('&#x27;', ''), white)
                            print(k)
                            n.write('[{:.8f}] pysh: {}'.format(time.time() - starttime, k))
                        elif x == 'stocks':
                            stock.stocks()
                        elif x == 'base':
                            convert.base()
                        elif x == 'prompt':
                            waiting = 7
                        elif x == 'chusr':
                            _user = input('usr: ')
                            _pswd = getpass.getpass(prompt='pwd: ')
                            y = open('data', 'r')
                            data = y.read()
                            y.close()
                            for j in data.split('&'):
                                if j.split('/')[0] == _user:
                                    if j.split('/')[1] == hashlib.sha256(_pswd.encode()).hexdigest():
                                        _path = _user + '/'
                                        paths = [_user + '/']
                            if _path == '':
                                print('incorrect login')
                                _path = 'temp/'
                                paths = ['temp/']
                        elif x == '#imp':
                            if _user == 'root':
                                waiting = 10
                            else:
                                print('pyos: pysh: permission denied')
                        elif x == '#exp':
                            if _user == 'root':
                                waiting = 11
                            else:
                                print('pyos: pysh: permission denied')
                        elif x == '#get':
                            if _user == 'root':
                                waiting = 14
                            else:
                                print('pyos: pysh: permission denied')
                        elif x == '#time':
                            if _user == 'root':
                                print(time.time() - starttime)
                            else:
                                print('pyos: pysh: permission denied')
                        elif x == '#log':
                            if _user == 'root':
                                print(open('log', 'r').read())
                            else:
                                print('pyos: pysh: permission denied')
                        elif x == '#addusr':
                            if _user == 'root':
                                _user = input('usr: ')
                                _pswd = getpass.getpass(prompt='pwd: ')
                                with open('data', 'a') as y:
                                    y.write('&{}/{}'.format(_user, hashlib.sha256(_pswd.encode()).hexdigest()))
                                print('set user/pswd to {}/{}'.format(_user, _pswd))
                                _path = _user + '/'
                                paths = [_user + '/']
                            else:
                                print('pyos: pysh: permission denied')
                        elif x == 'timer':
                            waiting = 13
                        elif x == 'stopwatch':
                            clock.stopwatch()
                        elif x == 'rn':
                            waiting = 16
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
                        try:
                            del filedict[x]
                            for j in paths:
                                if x in j:
                                    paths.remove(j)
                            if x in _path:
                                _path = paths[0]
                        except:
                            print('pyos: pysh: error while deleting {}'.format(x))
                        waiting = 0
                    elif waiting == 7:
                        addi = x
                        waiting = 0
                    elif waiting == 8:
                        if x.startwith('$') and l in varis:
                            varis[x[1:]] = varis[l]
                        else:
                            varis[l] = x
                        waiting = 0
                    elif waiting == 9:
                        if x == '=':
                            waiting = 8
                        else:
                            print('pyos: pysh: not a valid variable assignment')
                            waiting = 0
                    elif waiting == 10:
                        try:
                            c = open(x, 'r')
                            paths.append(_path + x)
                            filedict[x] = c.read()
                            c.close()
                        except:
                            print('pyos: pysh: error while importing {}'.format(x))
                        waiting = 0
                    elif waiting == 11:
                        try:
                            c = open(x, 'w')
                            c.write(filedict[x])
                            c.close()
                        except:
                            print('pyos: pysh: error while exporting {}'.format(x))
                        waiting = 0
                    elif waiting == 12:
                        try:
                            urllib.request.urlretrieve(l, 'cache')
                            c = open('cache', 'r')
                            paths.append(_path + x)
                            filedict[x] = c.read()
                            c.close()
                        except Exception:
                            print('pyos: pysh: error while getting {}'.format(l))
                        waiting = 0
                    elif waiting == 13:
                        clock.timer(int(x))
                        waiting = 0
                    elif waiting == 14:
                        l = x
                        waiting = 12
                    elif waiting == 15:
                        if _path + previous in paths:
                            filedict[x] = filedict[previous]
                            del filedict[previous]
                        else:
                            print('pyos: pysh: file {} not found'.format(previous))
                    elif waiting == 16:
                        previous = x
                        waiting = 15
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
                            cotw.cotw(cotw.c_countries, cotw.c_answers, x[4])
                        else:
                            cotw.cotw(cotw.c_countries, cotw.c_answers, '0')
                    elif x.startswith('hash'):
                        valid2 = ['md5', 'sha1', 't-hash', 'sha256', 'sha384', 'sha512']
                        if x[4:] in valid2:
                            hashing.thsh(hashing.h_char, x[4:])
                        else:
                            hashing.thsh(hashing.h_char, '0')
                    elif x.startswith('$'):
                        waiting = 9
                        t = x[1:]
                    elif x.startswith(':'):
                        exec(x[1:])
                    else:
                        print('pyos: pysh: {} not found.'.format(x))
                        waiting = 0
    n.close()
except Exception as err:
    print(type(err), err)
