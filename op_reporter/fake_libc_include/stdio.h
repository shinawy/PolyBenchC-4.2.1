#include <stddef.h>
typedef struct __fake_file FILE;
int printf(const char *fmt, ...);
int fprintf(FILE *stream, const char *fmt, ...);
