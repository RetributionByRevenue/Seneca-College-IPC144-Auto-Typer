#include "stdio.h"
#include "unistd.h"
int i;

int main (int argc, const char * argv[])
{
printf("pre-tee\n");
//***
//MAKE SURE YOU HAVE XDOTOOL.EXE IN SAME DIRECTORY OF THIS C PROGRAM!!!
//***
//tee concept introduced in ULI101, using the same concept in C programming language
//compiled with GCC
    
char* my_str = R"(7
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
?)";


for (i = 0; my_str[i] != '\0'; ++i){
printf("%d\n", i);
}//for loop used for getting the length of the string

if(dup2(fileno(popen("tee outputfile.bat", "w")), STDOUT_FILENO) < 0) {
	fprintf(stderr, "couldn't redirect output\n");
	return 1;//All printf statements will be saved to a file after this line
}
printf("\n");
printf("@echo off\n:: you have 5 seconds to click on the terminal\nTIMEOUT 4\n");
int counter = 0;

while (counter<i){
if (my_str[counter] == ' '){
printf("xdotool key +' '\n");
}
else if (my_str[counter] == '\n'){
printf("xdotool key + \"\{ENTER\}\"");
printf("\n");
}
else{
printf("xdotool key %c\n",my_str[counter]);
}
counter=counter+1;
//sleep currently the sleep is set for 0.2 seconds, change the 200 to influnce the sleep value.
printf("echo WScript.Sleep 200 > %temp%\sleep.vbs & cscript %temp%\sleep.vbs %sleepMs% //B & del %temp%\sleep.vbs");
}

return 0;

}
