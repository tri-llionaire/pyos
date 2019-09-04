# -*- coding: utf-8 -*-
_build = '081'
try:
    import urllib.request, urllib.error, hashlib, random, sys, platform, time
    red = ''
    green = ''
    blue = ''
    white = ''
    term = 'cls'
    if platform.system() == 'Linux':
        red = '\033[91m'
        green = '\033[92m'
        blue = '\033[95m'
        white = '\033[0m'
        term = 'clear'
    class check:
        def check():
            try:
                urllib.request.urlopen('http://216.58.192.142', timeout=1)
                return True
            except urllib.error.URLError:
                return False
    class hashing:
        h_char = {' ': '169', '$': '157', '(': '144', ',': '156', '0': '140', '4': '160', '8': '180', '<': '149', '@': '142', 'D': '110', 'H': '138', 'L': '106', 'P': '167', 'T': '126', 'X': '195', '\\': '124', '`': '151', 'd': '159', 'h': '114', 'l': '119', 'p': '139', 't': '174', 'x': '103', '|': '138', '#': '192', '\'': '186', '+': '163', '/': '176', '3': '191', '7': '100', ';': '191', '?': '115', 'C': '121', 'G': '154', 'K': '161', 'O': '172', 'S': '197', 'W': '162', '[': '182', '_': '114', 'c': '159', 'g': '101', 'k': '159', 'o': '134', 's': '121', 'w': '123', '{': '185', '\"': '193', '&': '118', '*': '172', '.': '106', '2': '135', '6': '119', ': ': '123', '>': '190', 'B': '114', 'F': '180', 'J': '119', 'N': '121', 'R': '119', 'V': '188', 'Z': '102', '^': '133', 'b': '105', 'f': '190', 'j': '113', 'n': '139', 'r': '162', 'v': '152', 'z': '181', '~': '185', '!': '118', '%': '121', ')': '137', '-': '99', '1': '158', '5': '147', '9': '161', '=': '109', 'A': '106', 'E': '179', 'I': '151', 'M': '195', 'Q': '111', 'U': '100', 'Y': '101', ']': '185', 'a': '174', 'e': '172', 'i': '154', 'm': '198', 'q': '145', 'u': '130', 'y': '170', '}': '148'}
        def thsh(t_char, t_which):
            t_n = ''
            if t_which == '0':
                t_which = input('t-hash, md5, sha1, sha256, sha384, or sha512? ')
            if t_which == 't-hash':
                t_key = int(input('enter a key (2-100): '))
                if 2 <= t_key <= 100:
                    t_s = input('enter string: ')
                    if len(t_s) > 32:
                        t_s = t_s[:33]
                    else:
                        t_s = t_s + (' '*(32-len(t_s)))
                    for t_a in t_s:
                        if t_a in t_char:
                            t_n = t_char[t_a] + t_n
                        else:
                            t_n = t_char[' '] + t_n
                    print(hex(int(t_n)/t_key)[2:-1])
                else:
                    pass
            else:
                t_s = input('enter string: ')
                hashing.otherhash(t_which, t_s)
        def itsh(i_s, i_key, i_char):
            i_n = ''
            if 2 <= i_key <= 100:
                if len(i_s) > 32:
                    i_s = i_s[:33]
                else:
                    i_s = i_s + (' '*(32-len(i_s)))
                for i_a in i_s:
                    if i_a in i_char:
                        i_n = i_char[i_a] + i_n
                    else:
                        i_n = i_char[' '] + i_n
                return hex(int(int(i_n)/i_key))[2:-1]
            else:
                print('pyos: pysh: scan: t-hash: invalid key')
        def otherhash(s_hs, s_st):
            if s_hs == 'md5':
                s_st = hashlib.md5(s_st.encode()).hexdigest()
            elif s_hs == 'sha1':
                s_st = hashlib.sha1(s_st.encode()).hexdigest()
            elif s_hs == 'sha256':
                s_st = hashlib.sha256(s_st.encode()).hexdigest()
            elif s_hs == 'sha384':
                s_st = hashlib.sha384(s_st.encode()).hexdigest()
            elif s_hs == 'sha512':
                s_st = hashlib.sha512(s_st.encode()).hexdigest()
            else:
                print('pyos: pysh: hash: invalid hash')
    class scan:
        def scan(s_ch, s_hs):
            if s_ch == '0':
                s_ch = input('python utf8scan6.3.6\nchoose an option to convert:\n1: Non-condensed, non-hashed\n2: Condensed, non-hashed\n3: Non-condensed, hashed\n4: Condensed, hashed\n5: Super condensed, hashed\n')
            if s_ch == '3' or s_ch == '4' or s_ch == '5' or s_hs == '0':
                s_hs = input('t-hash, md5, sha1, sha256, sha384, or sha512? ')
            s_st = input('enter your string: ')
            s_r = len(s_st) + 3
            s_z = len(s_st) + 5
            s_bi = ''.join(format(ord(s_x), 'b') for s_x in s_st)
            s_x = 0
            def s_output_end(s_x, s_r):
                sys.stdout.write(' '*(s_r-s_x))
                sys.stdout.write('|\n\\'+(s_r*'-')+'/\n')
            def s_output_opt(s_x, s_r, s_hs):
                sys.stdout.write(' '*(s_z-s_x))
                if s_hs == 'md5':
                    sys.stdout.write('|\n\\md5'+((s_z-3)*'-')+'/\n')
                elif s_hs == 'sha1':
                    sys.stdout.write('|\n\\sha1'+((s_z-4)*'-')+'/\n')
                else:
                    sys.stdout.write('|\n\\{}'.format(s_hs)+((s_z-6)*'-')+'/\n')
            if s_ch == '1':
                sys.stdout.write('/U8S1'+((s_z-6)*'-')+'\\\n|')
                for s_i in s_bi:
                    if s_x == s_r:
                        sys.stdout.write('|\n|')
                        s_x = 0
                    else:
                        pass
                    if s_i == '1':
                        sys.stdout.write('■')
                    else:
                        sys.stdout.write(' ')
                    s_x += 1
                    sys.stdout.flush()
                s_output_end(s_x, s_r)
            elif s_ch == '2':
                sys.stdout.write('/U8S2'+((s_z-6)*'-')+'\\\n|')
                for s_i in [s_bi[s_i:s_i+2] for s_i in range(0, len(s_bi), 2)]:
                    if s_x == s_r:
                        sys.stdout.write('|\n|')
                        s_x = 0
                    else:
                        pass
                    if s_i == '11':
                        sys.stdout.write('■')
                    elif s_i == '10':
                        sys.stdout.write('=')
                    elif s_i == '01':
                        sys.stdout.write('o')
                    else:
                        sys.stdout.write(' ')
                    s_x += 1
                s_output_end(s_x, s_r)
            elif s_ch == '3':
                if s_hs == 't-hash':
                    s_key = input('enter key (2-100): ')
                    s_st = str(hashing.itsh(s_st, int(s_key), hashing.h_char))
                else:
                    hashing.otherhash(s_hs, s_st)
                s_r = len(s_st)
                sys.stdout.write('/U8S{}'.format(s_ch)+((s_z-4)*'-')+'\\\n|')
                s_bi = ''.join(format(ord(s_x), 'b') for s_x in s_st)
                for s_i in s_bi:
                    if s_x == s_z:
                        sys.stdout.write('|\n|')
                        s_x = 0
                    else:
                        pass
                    if s_i == '1':
                        sys.stdout.write('■')
                    else:
                        sys.stdout.write(' ')
                    s_x += 1
                s_output_opt(s_x, s_r, s_hs)
            elif s_ch == '4':
                if s_hs == 't-hash':
                    s_key = input('enter key (2-100): ')
                    s_st = str(hashing.itsh(s_st, int(s_key), hashing.h_char))
                else:
                    hashing.otherhash(s_hs, s_st)
                s_r = len(s_st)
                sys.stdout.write('/U8S{}'.format(s_ch)+((s_z-4)*'-')+'\\\n|')
                s_bi = ''.join(format(ord(s_x), 'b') for s_x in s_st)
                for s_i in [s_bi[s_i:s_i+2] for s_i in range(0, len(s_bi), 2)]:
                    if s_x == s_z:
                        sys.stdout.write('|\n|')
                        s_x = 0
                    else:
                        pass
                    if s_i == '11':
                        sys.stdout.write('■')
                    elif s_i == '10':
                        sys.stdout.write('=')
                    elif s_i == '01':
                        sys.stdout.write('o')
                    else:
                        sys.stdout.write(' ')
                    s_x += 1
                s_output_opt(s_x, s_r, s_hs)
            elif s_ch == '5':
                if s_hs == 't-hash':
                    s_key = input('enter key (2-100): ')
                    s_st = str(hashing.itsh(s_st, int(s_key), hashing.h_char))
                else:
                    hashing.otherhash(s_hs, s_st)
                s_r = len(s_st)
                sys.stdout.write('/U8S{}'.format(s_ch)+((s_z-4)*'-')+'\\\n|')
                s_bi = ''.join(format(ord(s_x), 'b') for s_x in s_st)
                for s_i in [s_bi[s_i:s_i+3] for s_i in range(0, len(s_bi), 3)]:
                    if s_x == s_z:
                        sys.stdout.write('|\n|')
                        s_x = 0
                    else:
                        pass
                    if s_i == '001':
                        sys.stdout.write('■')
                    elif s_i == '010':
                        sys.stdout.write('=')
                    elif s_i == '011':
                        sys.stdout.write('o')
                    elif s_i == '100':
                        sys.stdout.write('+')
                    elif s_i == '101':
                        sys.stdout.write('x')
                    elif s_i == '110':
                        sys.stdout.write('<')
                    elif s_i == '111':
                        sys.stdout.write('>')
                    else:
                        sys.stdout.write(' ')
                    s_x += 1
                s_output_opt(s_x, s_r, s_hs)
            else:
                print('pyos: pysh: scan: unknown option')
    class cotw:
        c_countries = [
            'Afghanistan',
            'Albania',
            'Algeria',
            'Andorra',
            'Angola',
            'Anguilla',
            'Antigua and Barbuda',
            'Argentina',
            'Armenia',
            'Aruba',
            'Australia',
            'Austria',
            'Azerbaijan',
            'Bahamas',
            'Bahrain',
            'Bangladesh',
            'Barbados',
            'Belarus',
            'Belgium',
            'Belize',
            'Benin',
            'Bermuda',
            'Bhutan',
            'Bolivia',
            'Bosnia and Herzegovina',
            'Botswana',
            'Brazil',
            'British Virgin Islands',
            'Brunei',
            'Bulgaria',
            'Burkina Faso',
            'Burundi',
            'Cabo Verde',
            'Cambodia',
            'Cameroon',
            'Canada',
            'Cayman Islands',
            'Central African Republic',
            'Chad',
            'Chile',
            'China',
            'Colombia',
            'Comoros',
            'Democratic Republic of the Congo',
            'Republic of the Congo',
            'Cook Islands',
            'Costa Rica',
            'Cote d\'Ivoire',
            'Croatia',
            'Cuba',
            'Curacao',
            'Cyprus',
            'Czechia',
            'Denmark',
            'Djibouti',
            'Dominica',
            'Dominican Republic',
            'Ecuador',
            'Egypt',
            'El Salvador',
            'Equatorial Guinea',
            'Eritrea',
            'Estonia',
            'Eswatini',
            'Ethiopia',
            'Falkland Islands',
            'Faroe Islands',
            'Fiji',
            'Finland',
            'France',
            'French Polynesia',
            'Gabon',
            'Gambia',
            'Georgia',
            'Germany',
            'Ghana',
            'Gibraltar',
            'Greece',
            'Greenland',
            'Grenada',
            'Guam',
            'Guatemala',
            'Guernsey',
            'Guinea',
            'Guinea-Bissau',
            'Guyana',
            'Haiti',
            'Honduras',
            'Hungary',
            'Iceland',
            'India',
            'Indonesia',
            'Iran',
            'Iraq',
            'Ireland',
            'Isle of Man',
            'Israel',
            'Italy',
            'Jamaica',
            'Japan',
            'Jersey',
            'Jordan',
            'Kazakhstan',
            'Kenya',
            'Kiribati',
            'Kosovo',
            'Kuwait',
            'Kyrgyzstan',
            'Laos',
            'Latvia',
            'Lebanon',
            'Lesotho',
            'Liberia',
            'Libya',
            'Liechtenstein',
            'Lithuania',
            'Luxembourg',
            'Macedonia',
            'Madagascar',
            'Malawi',
            'Malaysia',
            'Maldives',
            'Mali',
            'Malta',
            'Marshall Islands',
            'Mauritania',
            'Mauritius',
            'Mexico',
            'Micronesia',
            'Moldova',
            'Monaco',
            'Mongolia',
            'Montenegro',
            'Montserrat',
            'Morocco',
            'Mozambique',
            'Myanmar',
            'Namibia',
            'Nauru',
            'Nepal',
            'Netherlands',
            'New Caledonia',
            'New Zealand',
            'Nicaragua',
            'Niger',
            'Nigeria',
            'Niue',
            'Northern Mariana Islands',
            'North Korea',
            'Norway',
            'Oman',
            'Pakistan',
            'Palau',
            'Panama',
            'Papua New Guinea',
            'Paraguay',
            'Peru',
            'Philippines',
            'Poland',
            'Portugal',
            'Qatar',
            'Romania',
            'Russia',
            'Rwanda',
            'Saint Helena, Ascension, and Tristan da Cunha',
            'Saint Kitts and Nevis',
            'Saint Lucia',
            'Saint Martin',
            'Saint Pierre and Miquelon',
            'Saint Vincent and the Grenadines',
            'Samoa',
            'San Marino',
            'Sao Tome and Principe',
            'Saudi Arabia',
            'Senegal',
            'Serbia',
            'Seychelles',
            'Sierra Leone',
            'Singapore',
            'Sint Maarten',
            'Slovakia',
            'Slovenia',
            'Solomon Islands',
            'Somalia',
            'South Africa',
            'South Korea',
            'South Sudan',
            'Spain',
            'Sri Lanka',
            'Sudan',
            'Suriname',
            'Sweden',
            'Switzerland',
            'Syria',
            'Taiwan',
            'Tajikistan',
            'Tanzania',
            'Thailand',
            'Timor-Leste',
            'Togo',
            'Tokelau',
            'Tonga',
            'Trinidad and Tobago',
            'Tunisia',
            'Turkey',
            'Turkmenistan',
            'Turks and Caicos Islands',
            'Tuvalu',
            'Uganda',
            'Ukraine',
            'United Arab Emirates',
            'United Kingdom',
            'United States of America',
            'Uruguay',
            'Uzbekistan',
            'Vanuatu',
            'Vatican City',
            'Venezuela',
            'Vietnam',
            'Virgin Islands',
            'Wallis and Futuna',
            'Western Sahara',
            'Yemen',
            'Zambia',
            'Zimbabwe',
        ]
        c_answers = {
            'Afghanistan': 'Kabul',
            'Albania': 'Tirana',
            'Algeria': 'Algiers',
            'Andorra': 'Andorra la Vella',
            'Angola': 'Luanda',
            'Anguilla': 'The Valley',
            'Antigua and Barbuda': 'Saint John\'s',
            'Argentina': 'Buenos Aires',
            'Armenia': 'Yerevan',
            'Aruba': 'Oranjestad',
            'Australia': 'Canberra',
            'Austria': 'Vienna',
            'Azerbaijan': 'Baku',
            'Bahamas': 'Nassau',
            'Bahrain': 'Manama',
            'Bangladesh': 'Dhaka',
            'Barbados': 'Bridgetown',
            'Belarus': 'Minsk',
            'Belgium': 'Brussels',
            'Belize': 'Belmopan',
            'Benin': 'Porto-Novo',
            'Bermuda': 'Hamilton',
            'Bhutan': 'Thimphu',
            'Bolivia': 'Sucre',
            'Bosnia and Herzegovina': 'Sarajevo',
            'Botswana': 'Gaborone',
            'Brazil': 'Brasilia',
            'British Virgin Islands': 'Road Town',
            'Brunei': 'Bandar Seri Begawan',
            'Bulgaria': 'Sofia',
            'Burkina Faso': 'Ouagadougou',
            'Burundi': 'Bujumbura',
            'Cabo Verde': 'Praia',
            'Cambodia': 'Phnom Penh',
            'Cameroon': 'Yaounde',
            'Canada': 'Ottawa',
            'Cayman Islands': 'George Town',
            'Central African Republic': 'Bangui',
            'Chad': 'N\'Djamena',
            'Chile': 'Santiago',
            'China': 'Beijing',
            'Colombia': 'Bogota',
            'Comoros': 'Moroni',
            'Democratic Republic of the Congo': 'Kinshasa',
            'Republic of the Congo': 'Brazzaville',
            'Cook Islands': 'Avarua',
            'Costa Rica': 'San Jose',
            'Cote d\'Ivoire': 'Yamoussoukro',
            'Croatia': 'Zagreb',
            'Cuba': 'Havana',
            'Curacao': 'Willemstad',
            'Cyprus': 'Nicosia',
            'Czechia': 'Prague',
            'Denmark': 'Copenhagen',
            'Djibouti': 'Djibouti',
            'Dominica': 'Roseau',
            'Dominican Republic': 'Santo Domingo',
            'Ecuador': 'Quito',
            'Egypt': 'Cairo',
            'El Salvador': 'San Salvador',
            'Equatorial Guinea': 'Malabo',
            'Eritrea': 'Asmara',
            'Estonia': 'Tallinn',
            'Eswatini': 'Mbabane',
            'Ethiopia': 'Addis Ababa',
            'Falkland Islands': 'Stanley',
            'Faroe Islands': 'Torshavn',
            'Fiji': 'Suva',
            'Finland': 'Helsinki',
            'France': 'Paris',
            'French Polynesia': 'Papeete',
            'Gabon': 'Libreville',
            'Gambia': 'Banjul',
            'Georgia': 'Tbilisi',
            'Germany': 'Berlin',
            'Gibraltar': 'Gibraltar',
            'Ghana': 'Accra',
            'Greece': 'Athens',
            'Greenland': 'Nuuk',
            'Grenada': 'Saint George\'s',
            'Guam': 'Agana',
            'Guatemala': 'Guatemala City',
            'Guernsey': 'Saint Peter Port',
            'Guinea': 'Conakry',
            'Guinea-Bissau': 'Bissau',
            'Guyana': 'Georgetown',
            'Haiti': 'Port-au-Prince',
            'Honduras': 'Tegucigalpa',
            'Hungary': 'Budapest',
            'Iceland': 'Reykjavik',
            'India': 'New Delhi',
            'Indonesia': 'Jakarta',
            'Iran': 'Tehran',
            'Iraq': 'Baghdad',
            'Ireland': 'Dublin',
            'Isle of Man': 'Douglas',
            'Israel': 'Jerusalem',
            'Italy': 'Rome',
            'Jamaica': 'Kingston',
            'Japan': 'Tokyo',
            'Jersey': 'Saint Helier',
            'Jordan': 'Amman',
            'Kazakhstan': 'Astana',
            'Kenya': 'Nairobi',
            'Kiribati': 'Tarawa',
            'Kosovo': 'Pristina',
            'Kuwait': 'Kuwait City',
            'Kyrgyzstan': 'Bishkek',
            'Laos': 'Vientiane',
            'Latvia': 'Riga',
            'Lebanon': 'Beirut',
            'Lesotho': 'Maseru',
            'Liberia': 'Monrovia',
            'Libya': 'Tripoli',
            'Liechtenstein': 'Vaduz',
            'Lithuania': 'Vilnius',
            'Luxembourg': 'Luxembourg',
            'Macedonia': 'Skopje',
            'Madagascar': 'Antananarivo',
            'Malawi': 'Lilongwe',
            'Malaysia': 'Kuala Lumpur',
            'Maldives': 'Male',
            'Mali': 'Bamako',
            'Malta': 'Valletta',
            'Marshall Islands': 'Majuro',
            'Mauritania': 'Nouakchott',
            'Mauritius': 'Port Louis',
            'Mexico': 'Mexico City',
            'Micronesia': 'Palikir',
            'Moldova': 'Chisinau',
            'Monaco': 'Monaco',
            'Mongolia': 'Ulaanbaatar',
            'Montenegro': 'Podgorica',
            'Montserrat': 'Brades',
            'Morocco': 'Rabat',
            'Mozambique': 'Maputo',
            'Myanmar': 'Naypyidaw',
            'Namibia': 'Windhoek',
            'Nauru': 'Yaren District',
            'Nepal': 'Kathmandu',
            'Netherlands': 'Amsterdam',
            'New Caledonia': 'Noumea',
            'New Zealand': 'Wellington',
            'Nicaragua': 'Managua',
            'Niger': 'Niamey',
            'Nigeria': 'Abuja',
            'Niue': 'Alofi',
            'Northern Mariana Islands': 'Saipan',
            'North Korea': 'Pyongyang',
            'Norway': 'Oslo',
            'Oman': 'Muscat',
            'Pakistan': 'Islamabad',
            'Palau': 'Ngerulmud',
            'Panama': 'Panama City',
            'Papua New Guinea': 'Port Moresby',
            'Paraguay': 'Asuncion',
            'Peru': 'Lima',
            'Philippines': 'Manila',
            'Poland': 'Warsaw',
            'Portugal': 'Lisbon',
            'Qatar': 'Doha',
            'Romania': 'Bucharest',
            'Russia': 'Moscow',
            'Rwanda': 'Kigali',
            'Saint Helena, Ascension, and Tristan da Cunha': 'Jamestown',
            'Saint Kitts and Nevis': 'Basseterre',
            'Saint Lucia': 'Castries',
            'Saint Martin': 'Marigot',
            'Saint Pierre and Miquelon': 'Saint-Pierre',
            'Saint Vincent and the Grenadines': 'Kingstown',
            'Samoa': 'Apia',
            'San Marino': 'San Marino',
            'Sao Tome and Principe': 'Sao Tome',
            'Saudi Arabia': 'Riyadh',
            'Senegal': 'Dakar',
            'Serbia': 'Belgrade',
            'Seychelles': 'Victoria',
            'Sierra Leone': 'Freetown',
            'Singapore': 'Singapore',
            'Sint Maarten': 'Philipsburg',
            'Slovakia': 'Bratislava',
            'Slovenia': 'Ljubljana',
            'Solomon Islands': 'Honiara',
            'Somalia': 'Mogadishu',
            'South Africa': 'Pretoria',
            'South Korea': 'Seoul',
            'South Sudan': 'Juba',
            'Spain': 'Madrid',
            'Sri Lanka': 'Sri Jayawardenepura Kotte',
            'Sudan': 'Khartoum',
            'Suriname': 'Paramaribo',
            'Sweden': 'Stockholm',
            'Switzerland': 'Bern',
            'Syria': 'Damascus',
            'Taiwan': 'Taipei',
            'Tajikistan': 'Dushanbe',
            'Tanzania': 'Dodoma',
            'Thailand': 'Bangkok',
            'Timor-Leste': 'Dili',
            'Togo': 'Lome',
            'Tokelau': 'Nukunonu',
            'Tonga': 'Nuku\'alofa',
            'Trinidad and Tobago': 'Port of Spain',
            'Tunisia': 'Tunis',
            'Turkey': 'Ankara',
            'Turkmenistan': 'Ashgabat',
            'Turks and Caicos Islands': 'Grand Turk',
            'Tuvalu': 'Funafuti',
            'Uganda': 'Kampala',
            'Ukraine': 'Kiev',
            'United Arab Emirates': 'Abu Dhabi',
            'United Kingdom': 'London',
            'United States of America': 'Washington, D.C.',
            'Uruguay': 'Montevideo',
            'Uzbekistan': 'Tashkent',
            'Vanuatu': 'Port Vila',
            'Vatican City': 'Vatican City',
            'Venezuela': 'Caracas',
            'Vietnam': 'Hanoi',
            'Virgin Islands': 'Charlotte Amalie',
            'Wallis and Futuna': 'Mata-Utu',
            'Western Sahara': 'Laayoune',
            'Yemen': 'Sana\'a',
            'Zambia': 'Lusaka',
            'Zimbabwe': 'Harare',
        }
        def cotw(c_countries, c_answers, c_choose):
            c_right = 0
            c_wrong = 0
            c_total = c_right + c_wrong
            c_ans = 'x'
            print('the cia world factbook 2019\ncountriesoftheworld 1.6.8.41\n\'end\' to end the program\n')
            def c_get_key(c_val):
                for c_key, c_value in list(c_answers.items()):
                    if c_val == c_value:
                        return c_key
            def c_c_w_r(c_right, c_wrong):
                return '\n{}{}/{}{}'.format(green, c_right, c_wrong, white)
            def c_c_w_w(c_right, c_wrong):
                return '\n{}{}/{}{}'.format(red, c_right, c_wrong, white)
            def c_perc(c_right, c_wrong):
                return '{0:.2f}'.format(100.00 / float(c_total) * float(c_right))
            if c_choose == '0':
                c_choose = input('Answer with the countries or capitals? (1 or 2): ')
            elif c_choose == '2':
                while c_ans.lower() != 'end':
                    c_n = random.randint(0, 196)
                    print('\nWhat is the capital of the country {}{}{}?\n'.format(blue, c_get_key(c_answers.get(c_countries[c_n])), white))
                    c_ans = input()
                    if c_ans.lower() == 'end':
                        pass
                    elif c_ans.lower() == c_answers.get(c_countries[c_n]).lower():
                        print('\n{}CORRECT'.format(green))
                        c_right += 1
                        c_total = c_right + c_wrong
                        print(c_c_w_r(c_right, c_total))
                        print('{}{}'.format(blue, str(c_perc(c_right, c_wrong))) + '%{}\n'.format(white))
                    else:
                        print('\n{}WRONG. '.format(red) + c_answers.get(c_countries[c_n]))
                        c_wrong += 1
                        c_total = c_right + c_wrong
                        print(c_c_w_w(c_right, c_total))
                        print('{}{}'.format(blue, str(c_perc(c_right, c_wrong))) + '%{}\n'.format(white))
            elif c_choose == '1':
                while c_ans.lower() != 'end':
                    c_n = random.randint(0, 196)
                    print('\nWhich country has the capital {}{}{}?\n'.format(blue, c_answers.get(c_countries[c_n]), white))
                    c_ans = input()
                    if c_ans.lower() == 'end':
                        pass
                    elif c_ans.lower() == c_get_key(c_answers.get(c_countries[c_n])).lower():
                        print('\n{}CORRECT'.format(green))
                        c_right += 1
                        c_total = c_right + c_wrong
                        print(c_c_w_r(c_right, c_total))
                        print('{}{}'.format(blue, str(c_perc(c_right, c_wrong))) + '%{}\n'.format(white))
                    else:
                        print('\n{}WRONG. '.format(red) + c_get_key(c_answers.get(c_countries[c_n])))
                        c_wrong += 1
                        c_total = c_right + c_wrong
                        print(c_c_w_w(c_right, c_total))
                        print('{}{}'.format(blue, str(c_perc(c_right, c_wrong))) + '%{}\n'.format(white))
            else:
                print('Um')
                pass
    class stock:
        def stocks():
            money = 50
            print('(3.6.2) Welcome to Python Stock Central!\nHow much money can you make in 10 days?\n\'end\' to quit')
            yours = []
            stocks = {
                'Microsoft': 20,
                'Google': 20,
                'IBM': 20,
                'Diamler': 20,
                'Mozilla': 20,
                'Apple': 20,
                'Samsung': 20,
                'Lenovo': 20,
                'HP': 20,
                'Walmart': 20,
                'Toyota': 20,
                'Volkswagen': 20,
                'Honda': 20,
                'Shell': 20,
                'Exxon': 20,
                'AT&T': 20,
                'Ford': 20,
                'Amazon': 20,
                'GE': 20,
                'Verizon': 20,
                'WellsFargo': 20,
                'GM': 20,
                'Costco': 20,
                'Allianz': 20,
                'Kroger': 20,
                'Boeing': 20,
                'Comcast': 20,
                'Sony': 20,
                'Mitsubishi': 20,
                'Nestle': 20,
            }
            x = 1
            while x < 12:
                h = 0
                print('DAY {}'.format(str(x)))
                moneyx = money
                old_stocks = stocks.copy()
                for j in stocks:
                    change = random.randint(-10, 10)
                    stocks[j] += change
                stockx = sorted(stocks, key=stocks.get)
                for i in stockx:
                    if stocks[i] <= 0:
                        pass
                    else:
                        if stocks[i] - old_stocks[i] >= 0:
                            y = '{}[+'.format(green) + str(stocks[i] - old_stocks[i]) + ']'
                        else:
                            y = '{}['.format(red) + str(stocks[i] - old_stocks[i]) + ']'
                        if i in yours:
                            if h == 3:
                                sys.stdout.write('\n{} {}{}: {} (OWNED)'.format(y, white, i, stocks.get(i)) + ' ' * (35 - len('{} {}{}: {} (OWNED)'.format(y, white, i, stocks.get(i)))))
                                h = 1
                            else:
                                sys.stdout.write('{} {}{}: {} (OWNED)'.format(y, white, i, stocks.get(i)) + ' ' * (35 - len('{} {}{}: {} (OWNED)'.format(y, white, i, stocks.get(i)))))
                                money += stocks[i] - old_stocks[i]
                                h += 1
                        else:
                            if h == 3:
                                sys.stdout.write('\n{} {}{}: {}'.format(y, white, i, stocks.get(i)) + ' ' * (35 - len('{} {}[0m{}: {}'.format(y, white, i, stocks.get(i)))))
                                h = 1
                            else:
                                sys.stdout.write('{} {}{}: {}'.format(y, white, i, stocks.get(i)) + ' ' * (35 - len('{} {}{}: {}'.format(y, white, i, stocks.get(i)))))
                                h += 1
                if x > 1:
                    print('\nYou made ${} yesterday.'.format(str(money - moneyx)))
                else:
                    pass
                if x == 11:
                    pass
                else:
                    print('\nYou have ${} before purchases.'.format(money))
                    which = input('What would you like to invest in? ').split()
                    if which == 'end':
                        break
                    for i in which:
                        if i in stocks:
                            if i != yours:
                                if money >= stocks.get(i):
                                    yours.append(i)
                                    money -= stocks.get(i)
                                else:
                                    print('Not enough money!')
                            else:
                                print('Already owned.')
                        else:
                            print('Error')
                print('You have ${} after purchases.\n'.format(money))
                x += 1
    class clock:
        def stopwatch():
            input('Hit enter to start/stop')
            started = time.time()
            input()
            print(time.time() - started)
        def timer(seconds):
            if seconds == '':
                seconds = input('How many seconds? ')
            print('Starting')
            time.sleep(seconds)
            print('Done')
    class convert:
        def base(opt, to, number):
            if opt == '':
                opt = input('from base (d)ec, (o)ct, (h)ex, or (b)in? ')
            if to == '':
                to = input('to base (d)ec, (o)ct, (h)ex, or (b)in? ')
            if number == '':
                number = input('enter the number: ')
            if opt == 'd':
                if to == 'h':
                    print(hex(int(number)))
                elif to == 'o':
                    print(oct(int(number)))
                elif to == 'b':
                    print(bin(int(number)))
                else:
                    print(number)
            elif opt == 'o':
                if to == 'd':
                    print(int(number, 8))
                elif to == 'b':
                    print(bin(int(number, 8)))
                elif to == 'h':
                    print(hex(int(number, 8)))
                else:
                    print(number)
            elif opt == 'h':
                if to == 'd':
                    print(int(str(number), 16))
                elif to == 'o':
                    print(oct(int(str(number), 16)))
                elif to == 'b':
                    print(bin(int(str(number), 16)))
                else:
                    print(number)
            elif opt == 'b':
                if to == 'd':
                    print(int(number, 2))
                elif to == 'o':
                    print(oct(int(number, 2)))
                elif to == 'h':
                    print(hex(int(number, 2)))
                else:
                    print(number)
            else:
                print('error')
except Exception as err:
    print(type, err)
    pass
