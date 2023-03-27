#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    do
    {
        height = get_int("How tall is the pyramid? Please input a number from 1 to 8: "); // Asks a user for a valid input from 1 to 8

        if (height >= 1 && height <= 8)
        {
            printf("\n");
            int counter = height - 1;
            for (int i = 0; i < height; i++) // This loop is to iterate through the rows
            {
                bool check = true;

                for (int j = 0; j < (i + 1); j++) // This loop is to iterate through the columns and print the right aligned pyramid
                {
                    while (check == true)
                    {
                        for (int k = 0; k < counter; k++) // This loop will print the leading empty spaces
                        {
                            printf(" ");
                        }
                        check = false;
                    }
                    printf("#");
                }

                for (int x = 0; x < 2; x++) // This loop prints the two empty spaces between the pyramids
                {
                    printf(" ");
                }
                for (int y = 0; y < (i + 1); y++) // This loop prints the left aligned pyramid
                {
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