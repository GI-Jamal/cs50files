#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

char rotate(char character, int key);
bool only_digits(string text);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        if (only_digits(argv[1]))
        {
            string plaintext = get_string("plaintext:  ");
            int key = atoi(argv[1]) % 26;

            int i = 0;
            while (plaintext[i] != '\0')
            {
                plaintext[i] = rotate(plaintext[i], key);
                i++;
            }

            printf("ciphertext: %s\n", plaintext);
            return 0;
        }

        else
        {
            printf("Argument is not a positive integer. Usage: ./caesar key\n");
            return 1;
        }
    }

    else
    {
        printf("Too many or too few arguments. Usage: ./caesar key\n");
        return 1;
    }
}

char rotate(char character, int key)
{
    int asciival = character;
    if (islower(character))
    {
        asciival = asciival - 97 + key;
        if (asciival > 25)
        {
            asciival = asciival - 26;
            char cipherchar = asciival + 97;
            return cipherchar;
        }

        else
        {
            char cipherchar = asciival + 97;
            return cipherchar;
        }
    }

    else if (isupper(character))
    {
        asciival = asciival - 65 + key;
        if (asciival > 25)
        {
            asciival = asciival - 26;
            char cipherchar = asciival + 65;
            return cipherchar;
        }

        else
        {
            char cipherchar = asciival + 65;
            return cipherchar;
        }
    }
    else
    {
        return character;
    }
}

bool only_digits(string text)
{
    int i = 0;
    while (text[i] != '\0')
    {
        if (isdigit(text[i]))
        {
            i++;
        }
        else
        {
            return false;
        }
    }
    return true;
}