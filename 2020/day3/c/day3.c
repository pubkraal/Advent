#include <stdio.h>
#include <string.h>

#define BUFHEIGHT 350
#define BUFWIDTH 50

#define ARRLENGTH(x) (sizeof(x)/sizeof((x)[0]))

int num_trees(char chart[][BUFWIDTH], int h, int w, int vector[2]) {
    int x = 0;
    int y = 0;

    int trees = 0;
    for (int y = 0; y < h; y+=vector[1]) {
        char pos = chart[y][x];
        if (pos == '#') {
            trees += 1;
        }
        x = (x + vector[0]) % w;
    }

    return trees;
}

int main(int argc, char **argv) {
    char chart[BUFHEIGHT][BUFWIDTH];
    FILE *f = fopen("input.txt", "r");
    int h = 0;
    int w = 0;

    for (int i = 0; fgets(chart[i], sizeof(chart[0]), f) && !feof(f); i++) {
        int line_length = strlen(chart[i]);
        if (chart[i][line_length - 1] == '\n') {
            chart[i][line_length - 1] = '\0';
        }
        h++;
    }
    fclose(f);
    w = strlen(chart[0]);

    int vector[2] = {3,1};
    printf("Step 1: %d\n", num_trees(chart, h, w, vector));

    unsigned long long product = 1;
    int vectors[][2] = {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}};
    for (int i = 0; i < ARRLENGTH(vectors); i++) {
        product *= num_trees(chart, h, w, vectors[i]);
    }
    printf("Step 2: %llu\n", product);

    return 0;
}
