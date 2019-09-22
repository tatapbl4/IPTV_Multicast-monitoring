#!/usr/bin/env python3

import re
import urllib.request
import os
if os.path.exists("converted.txt"):
  os.remove("converted.txt")

FORMAT_DESCRIPTOR = "#EXTM3U"
RECORD_MARKER = "#EXTINF"

url = 'http://test.iptv.azedunet.az/stalker_portal/server/tv.m3u'
#urllib.request.urlretrieve(url, './playlist.m3u8')


'''
Регулярка для мультикаст группы: (\d{3}.\d{3}.\d{1,3}.\d{1,3}):(\d{1,5})(\S)*
Регулярка для значений Название,Группа,Порт (^\w+( \w+)*$)\n(\d{3}.\d{3}.\d{1,3}.\d{1,3}):(\d{1,5})(\S)*

'''

def delExcessiveInfo():
    r = open('playlist.m3u8', 'r')
    f = open('converted.txt', 'a+')

    '''
    for string in r:
            if re.match('udp://'):
                m = re.sub(r"(udp:\/\/[@]*)", '', string)
                print(string[:m.start()] + string[m.end():])
    '''

    for string in r:
        if string.startswith('#EXTINF'):
            m = re.sub(r"(#EXTINF:0,\d+\.\s~.+\n)", '', string)
            m = re.sub(r"(#EXTINF:0,\d+\.\s)", '', m)
            # Use (#EXTINF:0,\d+\.[\s]+(~|-).+\n) insted of above expressions
            f.write(m)
        elif string.startswith('http'):
            h = re.sub(r"(http:\/\/.*\n)", '', string)
            f.write(h)
        elif string.startswith('udp'):
            #d = re.sub(r"udp:\/\/[@]*")
            u = re.sub(r"(udp:\/\/[@]*)", '', string)
            f.write(u)
            # Use (#EXTINF:0,\d+\.[\s]+(~|-).+\n)(udp|http):\/\/.*$ instead of above udp and http regexps
        else:
            e = re.sub(r"#EXTM3U\n", '', string)
            f.write(e)

    f.close()
    r.close()

def conStr():
    f = open('converted.txt', 'r')
    line = re.compile(r'(\d{3}.\d{3}.\d{1,3}.\d{1,3}):(\d{1,5})(\W)?')

    for i in f:
        result = line.search(i)
        print(result)

    f.close()

def getAddr():
    f = open('converted.txt', 'r')

    for i in f:
        re = re.sub(r"", i)

delExcessiveInfo()
conStr()
