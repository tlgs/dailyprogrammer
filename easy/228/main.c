/* 25/01/2017 */
//just trying out some obfuscated code
#include <stdio.h>
#include <string.h>
#define S argv[1]
#define T printf(
char z[] = {78,79,84,0},y[] = {73,78,' ',
79,'R',68,69,82,0};int main(
int argc, char* argv[]){char p[10 << 1
];strcpy(p, S);while(*++S){if(*S
<*(S-1)){T"%s %s %s",
p,z,y);return 0;}}
T"%s %s",p,y);}
