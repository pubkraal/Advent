#include <stdio.h>
#include <string.h>

#define MAXLINES 2048
#define BUFSIZE 1024

struct Passport
{
};

int main(int argc, char **argv)
{
    int numlines = 0;
    FILE *f = fopen("input.txt", "r");
    if (f == NULL)
    {
        printf("Could not open input.txt, you sure it exists?\n");
        return 1;
    }

    char buffer[BUFSIZE];

    while (fgets(buffer, BUFSIZE, f) && !feof(f))
    {
        if (buffer[0] == '\n')
        {
            printf("New passport line\n");
            continue;
        }

        int l = strlen(buffer);
        if (buffer[l - 1] == '\n')
            buffer[l - 1] = '\0';

        char *token, *string;
        string = strdup(buffer);
        while ((token = strsep(&string, " ")) != NULL)
        {
            printf("token: %s\n", token);
        }
    }

    fclose(f);

    return 0;
}
