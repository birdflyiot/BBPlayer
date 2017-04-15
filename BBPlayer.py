# coding:utf-8
import ctypes
import time
import re

player = ctypes.windll.kernel32

# notes = [0,523,587,659,698,784,880,988]

q = 1.06 # 每阶音的倍数
q2 = q * q
dolist = {'C':523,'D':587,'E':659,'F':698,'G':784,'A':880,'B':988}

pitchs = {'l':0.5,'m':1,'h':2}



def BBPlayer(filename,dokey,speed):
    do = int(dolist[dokey]) # 获取对应调的do的频率
    re = int(do * q2)
    mi = int(re * q2)
    fa = int(mi * q)
    sol = int(fa * q2)
    la = int(sol * q2)
    si = int(la *q2)	
    notes = [0,do,re,mi,fa,sol,la,si]
    beats = 60/speed*1000
    
    # print(beats)
    with open(filename) as fp:
        song = fp.read().replace('\n','').split(',')
        # print(type(song))
        # print(song)

        for music in song:
            # print(type(music))
            # p = re.findall(r'[lmh]',music)[0] # 获取music中的字母
            p = music[1]
            p = float(pitchs[p]) # 高低音
            # music = re.split(r'[lmh]',music,maxsplit = 0,flags = 0)
            n = int(notes[int(music[0])]) # 音符
            b = float(music[2:]) # 节拍
            #print(music[0])
            print(n)
            # print(p)
            #print(music[2:])
            
            # print(b*beats)
            if n==0:
                time.sleep(b*beats/1000)
            else:
                player.Beep(int(n*p),int(b*beats))


BBPlayer('dayu','D',65)

