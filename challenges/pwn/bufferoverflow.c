#include <stdio.h>
#include <string.h>

void vuln_func(char* input) {
    char buffer[16];
    strcpy(buffer, input);
    printf("Input stored in buffer: %s", buffer);
}

void flag() {
    printf("buffer");
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Please provide an input");
        return 1;
    }
    vuln_func(argv[1]);
    return 0;
}