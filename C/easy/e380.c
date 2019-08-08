/* 05/08/2019 */
#include <stdio.h>

int main (int argc, char *argv[])
{
    char e[] = "&75+#=)?'8*;$%(92-/\".>,643";
    for (char *p = argv[1]; *p; p++) {
        char x = e[*p - 97] - 32;
        short i = 6;
        while (!((x >> --i) & 1));
        while (i--)
            putchar((x >> i) & 1 ? '.' : '-');
    }
}
