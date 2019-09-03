# -*- coding: utf-8 -*-
_build = '094'
try:
    print('loading pre-log necessaries')
    import time, os
    starttime = time.time()
    try:
        os.remove('log')
    except:
        pass
    n = open('log', 'a+')
    n.write('started manager log\n')
    k = 'loading modules'
    print(k)
    n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
    import urllib
    n.write('[{:.8f}] status: urllib loaded\n'.format(time.time() - starttime))
    import platform
    n.write('[{:.8f}] status: platform loaded\n'.format(time.time() - starttime))
    import subprocess
    n.write('[{:.8f}] status: subprocess loaded\n'.format(time.time() - starttime))
    from variables import check
    n.write('[{:.8f}] status: variables.check loaded\n'.format(time.time() - starttime))
    k = 'checking for internet'
    print(k)
    n.write('[{:.8f}] manager: {}'.format(time.time() - starttime, k))
    if check.check() is True:
        n.write('[{:.8f}] status: check.check() successful\n'.format(time.time() - starttime))
        k = '(w)eb update or (p)eertopeer update? '
        choice = input(k)
        n.write('[{:.8f}] query: {}\n'.format(time.time() - starttime, k))
        if choice == 'p':
            n.write('[{:.8f}] input: {}\n'.format(time.time() - starttime, choice))
            k = '(s)end or (r)eceive? '
            second = input(k)
            n.write('[{:.8f}] query: {}\n'.format(time.time() - starttime, k))
            if second == 'r':
                n.write('[{:.8f}] input: {}\n'.format(time.time() - starttime, second))
                files = ['main', 'variables', 'manager']
                n.write('[{:.8f}] status: loaded file names\n'.format(time.time() - starttime))
                import socket
                n.write('[{:.8f}] status: socket loaded\n'.format(time.time() - starttime))
                s = socket.socket()
                s.bind((socket.gethostname(), 5004))
                n.write('[{:.8f}] socket: built\n'.format(time.time() - starttime))
                for x in files:
                    f = open('{}.py'.format(x), 'wb')
                    n.write('[{:.8f}] status: opened {} for receiving\n'.format(time.time() - starttime, x))
                    s.listen(5)
                    while True:
                        c, addr = s.accept()
                        k = 'got connection for {} from {}\n'.format(x, addr)
                        print(k)
                        n.write('[{:.8f}] socket: {}\n'.format(time.time() - starttime, k))
                        k = 'receiving {}...'.format(x)
                        print(k)
                        n.write('[{:.8f}] socket: {}\n'.format(time.time() - starttime, k))
                        l = c.recv(1024)
                        while l:
                            f.write(l)
                            l = c.recv(1024)
                        f.close()
                        k = 'done receiving {}'.format(x)
                        print(k)
                        n.write('[{:.8f}] socket: {}\n'.format(time.time() - starttime, k))
                        c.close()
                        break
            if second == 's':
                n.write('[{:.8f}] input: {}\n'.format(time.time() - starttime, second))
                files = ['main', 'variables', 'manager']
                n.write('[{:.8f}] status: loaded file names\n'.format(time.time() - starttime))
                import socket
                n.write('[{:.8f}] status: socket loaded\n'.format(time.time() - starttime))
                s = socket.socket()
                s.connect((socket.gethostname(), 5004))
                n.write('[{:.8f}] socket: built\n'.format(time.time() - starttime))
                for x in files:
                    f = open('{}.py'.format(x), 'rb')
                    n.write('[{:.8f}] status: opened {} for sending\n'.format(time.time() - starttime, x))
                    k = 'sending {}...'.format(x)
                    print(k)
                    n.write('[{:.8f}] socket: {}\n'.format(time.time() - starttime, k))
                    l = f.read(1024)
                    while l:
                        s.send(l)
                        l = f.read(1024)
                    f.close()
                    k = 'done sending {}'.format(x)
                    print(k)
                    n.write('[{:.8f}] socket: {}\n'.format(time.time() - starttime, k))
                s.shutdown(socket.SHUT_WR)
                print(s.recv(1024))
                s.close()
                n.write('[{:.8f}] socket: shutdown successfully\n'.format(time.time() - starttime))
        else:
            k = 'checking for updates'
            print(k)
            n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
            l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/main.py'
            urllib.request.urlretrieve(l, 'cache')
            n.write('[{:.8f}] status: got url for main.py update\n'.format(time.time() - starttime))
            r = open('cache', 'r')
            words = r.read()
            r.close()
            n.write('[{:.8f}] status: successfully read cache\n'.format(time.time() - starttime))
            try:
                m = open('main.py', 'r')
                other = m.read()
                m.close()
                n.write('[{:.8f}] status: successfully read main.py\n'.format(time.time() - starttime))
            except OSError:
                other[34:37] = '000'
                n.write('[{:.8f}] status: failed to read main.py, setting _build to 000\n'.format(time.time() - starttime))
            if int(words[34:37]) > int(other[34:37]):
                urllib.request.urlretrieve(l, 'main.py')
                k = 'main updated from b{} to b{}'.format(other[34:37], words[34:37])
                print(k)
                n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
            elif int(words[34:37]) < int(other[34:37]):
                k = 'update github for main (b{} to b{})'.format(words[34:37], other[34:37])
                print(k)
                n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
            else:
                k = 'main up to date (b{})'.format(other[34:37])
                print(k)
                n.write('[{:.8f}] manager: {}\n\n'.format(time.time() - starttime, k))
            l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/variables.py'
            urllib.request.urlretrieve(l, 'cache')
            n.write('[{:.8f}] status: got url for variables.py update\n'.format(time.time() - starttime))
            r = open('cache', 'r')
            words = r.read()
            r.close()
            n.write('[{:.8f}] status: successfully read cache\n'.format(time.time() - starttime))
            try:
                m = open('variables.py', 'r')
                other = m.read()
                m.close()
                n.write('[{:.8f}] status: successfully read variables.py\n'.format(time.time() - starttime))
            except OSError:
                other[34:37] = '000'
                n.write('[{:.8f}] status: failed to read variables.py, setting _build to 000\n'.format(time.time() - starttime))
            if int(words[34:37]) > int(other[34:37]):
                urllib.request.urlretrieve(l, 'variables.py')
                k = 'variables updated from b{} to b{}'.format(other[34:37], words[34:37])
                print(k)
                n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
            elif int(words[34:37]) < int(other[34:37]):
                k = 'update github for variables (b{} to b{})'.format(words[34:37], other[34:37])
                print(k)
                n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
            else:
                k = 'variables up to date (b{})'.format(other[34:37])
                print(k)
                n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
            l = 'https://raw.githubusercontent.com/tri-llionaire/pyos/master/manager.py'
            urllib.request.urlretrieve(l, 'cache')
            n.write('[{:.8f}] status: got url for manager.py update\n'.format(time.time() - starttime))
            r = open('cache', 'r')
            words = r.read()
            r.close()
            n.write('[{:.8f}] status: successfully read manager.py\n'.format(time.time() - starttime))
            if int(words[34:37]) > int(_build):
                urllib.request.urlretrieve(l, 'manager.py')
                k = 'manager updated from b{} to b{}'.format(_build, words[34:37])
                print(k)
                n.write('[{:.8f}] manager: {}; restarting\n'.format(time.time() - starttime, k))
                exec(open('manager.py', 'r').read())
            elif int(words[34:37]) < int(_build):
                k = 'update github for manager (b{} to b{})'.format(words[34:37], _build)
                print(k)
                n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
            else:
                k = 'manager up to date (b{})'.format(_build)
                print(k)
                n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
            k = 'Total runtime: {:.8f}'.format(time.time() - starttime)
            print(k)
            n.write('[{:.8f}] manager: {}\n'.format(time.time() - starttime, k))
        input('Enter to boot pyos')
    else:
        k = 'no internet'
        print(k)
        n.write('[{:.8f}] status: check.check() unsuccessful\n'.format(time.time() - starttime))
    term = 'cls'
    if platform.system() == 'Linux':
        term = 'clear'
    tmp = subprocess.call(term, shell=True)
    n.write('[{:.8f}] manager: terms loaded, screen cleared\n'.format(time.time() - starttime))
    n.write('[{:.8f}] manager: pyos booted\n'.format(time.time() - starttime))
    n.close()
    exec(open('main.py', 'r').read())
except Exception as err:
    print(type, err)
