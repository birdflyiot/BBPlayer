from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import os
import ctypes
import threading
import time

filename = ''
# notes = [0,523,587,659,698,784,880,988]
q = 1.06 # 每阶音的倍数
q2 = q * q
dolist = {'C':523,'D':587,'E':659,'F':698,'G':784,'A':880,'B':988}
pitchs = {'l':0.5,'m':1,'h':2}
player = ctypes.windll.kernel32
global dokey,dokeyentry
global speed,speedentry


def selectpath():
    global filename
    filename = tkinter.filedialog.askopenfilename()
    file = os.path.basename(filename)
    Label(root,text = file,width = 10).grid(row = 0,column = 1)


def bbplayer(): # 已经有了全局变量filename了所以这里不用参数filename
    dokey = dokeyentry.get()
    speed = int(speedentry.get())
    do = int(dolist[dokey]) # 获取对应调的do的频率
    re = int(do * q2)
    mi = int(re * q2)
    fa = int(mi * q)
    sol = int(fa * q2)
    la = int(sol * q2)
    si = int(la *q2)	
    notes = [0,do,re,mi,fa,sol,la,si]
    beats = 60/speed*1000
    
    #print(beats)
    with open(filename) as fp:
        song = fp.read().replace('\n','').split(',')
        # print(type(song))
        # print(song)

        for music in song:
            print(music)
            # p = re.findall(r'[lmh]',music)[0] # 获取music中的字母
            p = music[1]
            p = float(pitchs[p]) # 高低音
            # music = re.split(r'[lmh]',music,maxsplit = 0,flags = 0)
            n = int(notes[int(music[0])]) # 音符
            b = float(music[2:]) # 节拍
            # print(music[0])
            # print(n)
            # print(p)
            # print(music[2:])
            
            # print(b*beats)
            if n==0:
                time.sleep(b*beats/1000)
            else:
                player.Beep(int(n*p),int(b*beats))

def helpful():
    tkinter.messagebox.askokcancel('提示信息','1、首先点击音乐库选择音乐文件\n2、音调为CDEFGAB调，速度为乐谱速度，如84,96等')

    
# 多线程解决假死问题
def thread():
    th = threading.Thread(target=bbplayer)
    th.setDaemon(True)
    th.start()
    
    
root = Tk()
root.geometry('300x120+200+200')
root.title('逼叨逼播放器 1.0')
Label(root,text = '当前播放:').grid(row = 0,sticky = W)
Button(root,text = '音乐库',command = selectpath).grid(row = 2,column = 0,sticky = W)
Label(root,text = '音调（大调）').grid(row = 3,column = 0)
Label(root,text = '速度').grid(row = 3,column = 2)
dokeyentry = Entry(root)
dokeyentry['width'] = 10
dokeyentry.insert(0,'C')
dokeyentry.grid(row = 3,column = 1)
speedentry = Entry(root)
speedentry['width'] = 10
speedentry.insert(0,100) # 设置默认值
speedentry.grid(row = 3,column = 3)
Button(root,text = '帮助',command = helpful).grid(row = 3,column = 5,sticky = E)
Button(root,text = '播放',background = 'red',command = thread).grid(row = 4,column = 0,sticky = W)

root.mainloop()
