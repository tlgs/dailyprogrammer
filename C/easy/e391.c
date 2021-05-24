/* 24/05/2021 */
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

int main(int argc, char *argv[]) {
  if (argc < 2) {
    return EXIT_FAILURE;
  }

  long n = strtol(argv[1], NULL, 10);
  for (int i = 1; i < (1 << n); i++) {
    putchar('`' + ffs(i));
  }
  putchar('\n');
}
