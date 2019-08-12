# -*- coding: utf-8 -*-
_build = '003'
_hash = 'FFFBF11570DCCF2B1503335704D2BE8BD0FFFDE98D83F3FFBC6C54A5B1AFE9F8'
_date = '08.11.2019'
import platform
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
