#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

const int BLOCK_SIZE = 512;

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover input.raw\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    BYTE jpeg[BLOCK_SIZE];
    char filename[8];
    FILE *output;
    int i = 0;

    while (fread(jpeg, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {
        if (jpeg[0] == 0xff && jpeg[1] == 0xd8 && jpeg[2] == 0xff && (jpeg[3] & 0xf0) == 0xe0)
        {
            if (i > 0)
            {
                fclose(output);
            }

            sprintf(filename, "%03i.jpg", i);
            output = fopen(filename, "w");
            i++;
        }

        if (i > 0)
        {
            fwrite(jpeg, 1, BLOCK_SIZE, output);
        }
    }

    fclose(input);
    fclose(output);
    return 0;
}