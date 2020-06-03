#!/usr/bin/env python3

import re
import urllib.request
from pathlib import Path
import os
if os.path.exists("converted.txt"):
  os.remove("converted.txt")

FORMAT_DESCRIPTOR = "#EXTM3U"
RECORD_MARKER = "#EXTINF"
M3U_PLAYLIST_NAME = 'playlist.m3u8'

content = Path(M3U_PLAYLIST_NAME).read_text()

url = 'http://dev.iptv.azedunet.az/stalker_portal/server/tools/m3u.php'
urllib.request.urlretrieve(url, './playlist.m3u8')

'''
Регулярка для мультикаст группы: (\d{3}.\d{3}.\d{1,3}.\d{1,3}):(\d{1,5})(\S)*
Регулярка для значений Название,Группа,Порт (^\w+( \w+)*$)\n(\d{3}.\d{3}.\d{1,3}.\d{1,3}):(\d{1,5})(\S)*
'''

def delExcessiveInfo():
    #r = open(M3U_PLAYLIST_NAME, 'r')
    f = open('converted.txt', 'a+')

    regex = ['r"(#EXTINF:0,\d+\.[\s]+(~|-).+\n)(udp|http):\/\/.*$"', 'r"(#EXTINF:0,\d+\.[\s]+(~|-).+\n)"', 'r"(#EXTINF:0,\d+\.[\s]+(~|-).+\n)(udp|http):\/\/.*$"']
    
    matches = re.finditer(regex[0], content, re.MULTILINE)
    #print(matches)

    for matchNum, match in enumerate(matches, start=1):
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    
    # for str in M3U_PLAYLIST_NAME:
    #     rmtxt = exclude.search(str)
    #     print(rmtxt)

    '''
    for string in r:
            if re.match('udp://'):
                m = re.sub(r"(udp:\/\/[@]*)", '', string)
                print(string[:m.start()] + string[m.end():])
    '''

    '''
    for string in r:
        if string.startswith('#EXTINF'):
            #m = re.sub(r"(#EXTINF:0,\d+\.\s~.+\n)", '', string)
            #m = re.sub(r"(#EXTINF:0,\d+\.\s)", '', m)
            m = re.sub(r"(#EXTINF:0,\d+\.[\s]+(~|-).+\n)", '', string)
            f.write(m)
        elif string.startswith('http') or string.startswith('udp'):
            h = re.sub(r"(#EXTINF:0,\d+\.[\s]+(~|-).+\n)(udp|http):\/\/.*$", '', string)
            #h = re.sub(r"(http:\/\/.*\n)", '', string)
            f.write(h)
        #elif string.startswith('udp'):
            ##d = re.sub(r"udp:\/\/[@]*")
            #u = re.sub(r"(udp:\/\/[@]*)", '', string)
            #f.write(u)
        else:
            e = re.sub(r"#EXTM3U\n", '', string)
            f.write(e)
    '''

    f.close()
    #r.close()

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
