ye#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    do
    {
        height = get_int("How tall is the pyramid? Please input a number from 1 to 8: ");

        if (height >= 1 && height <= 8)
        {
            printf("\n");
            int counter = height - 1;
            for (int i = 0; i < height; i++)
            {
                bool x = true;

                for (int j = 0; j < (i + 1); j++)
                {
                    while (x == true)
                    {
                        for (int k = 0; k < counter; k++)
                        {
                            printf(" ");
                        }
                        x = false;
                    }
                    printf("#");
                }
                counter = counter - 1;
                printf("\n");
            }
        }
        else
        {
            printf("Please input a valid number\n");
        }
    }
    while (height < 1 || height > 8);
}