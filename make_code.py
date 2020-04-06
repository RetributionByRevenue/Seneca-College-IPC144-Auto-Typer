head='''@echo off
:: you have 5 seconds to click on the terminal
TIMEOUT 4

'''
#####################
#modify text below if not matching with MS4 Output
# i use ? to represent press <enter>
text='''7
1
?
2
I Should
y n
yes
y
Not Be
In This List
-77
77
Cityscape Rd.
no
n y
y
bison
-1200
1200
Q8Q 3J3 P3P
Somewhere City
111b223333
1112223333
y n
N
yes
y
222-333-4444
2223334444
?
1
?
2
?
3
6665555
6665551111
?
3
9051112222
yes no
y
Maggie
y
R.
Greene Grimes
y
55
Hightop House
y
222
A9A 3K3
Bolton
y
9051112222
n
n
?
1
?
4
4161112222
n
?
4
4161112222
y
?
1
?
2
Daryl
n
Dixon
11
Forest Road
n
Y2Y 2N2
The Kingdom
9993338888
n
n
?
1
?
3
1112223333
y
Rick
n
Grimes
n
n
?
1
?
5
9052223333
?
5
9998887777
?
6
?
1
?
0
No yes
ny
n
0
y
?'''
text=text.replace('\n','@')
#print(text)

from pathlib import Path
path = str(Path(__file__).parent.absolute())
path1=path.replace("\\","\\\\")

import re
from IPython.utils.io import Tee #Tee just like in ULI101
from contextlib import closing
with closing(Tee(path1+"\\outputfile.bat", "w", channel="stdout")) as outputstream:
 charater_length = len(text) -1
 i=0
 computer='windows' #change to linux if using linux, we dont support mac users. they r lame
 if computer == 'linux':
    while charater_length >= i:    
        sstart=text[i:i+1]
        if bool(re.match(r'[A-Z]+$', sstart)) == True:
            print('xdotool key 0xffe6')
            print('xdotool key 0xffe6')
            print('xdotool key'+' '+sstart+' ')
            print('xdotool key 0xffe6')
            print('xdotool key 0xffe6')
        else:
            if sstart !='@' and sstart != '?' and sstart != ' ' and sstart!='.' and sstart!='-':
                print('xdotool key'+' '+sstart+' ')
            elif sstart == '@':
                print('xdotool key KP_Enter')
            elif sstart=='.': 
                print('xdotool key 0x002e')
            elif sstart=='-': 
                print('xdotool key 0x002d')
            elif sstart == ' ':
                print('xdotool key KP_Space')
            elif sstart == '?':
                print('')
        print("sleep 0.1")
        i=i+1
 if computer == 'windows':
    print(head)
    print('set DIR=path1')
    while charater_length >= i:    
        sstart=text[i:i+1]
        if (bool(re.match(r'[A-Z]+$', sstart)) == True) and False:
            print('')

        else:
            if sstart !='@' and sstart != '?' and sstart != ' ' and sstart!='.' and sstart!='-':
                print('xdotool key'+' '+sstart)
            elif sstart == '@':
                print('xdotool key +"{ENTER}"')
            elif sstart=='.': 
                print('xdotool key .')
            elif sstart=='-': 
                print('xdotool key -')
            elif sstart == ' ':
                print('xdotool key +" "')
            elif sstart == '?':
                print('')
        #to add 0.2 second sleep. to disable, type # in front of print( below
        #print("echo WScript.Sleep 200 > %temp%\sleep.vbs & cscript %temp%\sleep.vbs %sleepMs% //B & del %temp%\sleep.vbs") 
        i=i+1
