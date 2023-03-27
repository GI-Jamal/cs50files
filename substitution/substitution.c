#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

bool alpha_check(string text);
bool length_check(string text);
bool unique_check(string text);
string uppercase(string text);
string lowercase(string text);
char rotate(char character, string key);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string key = uppercase(argv[1]);

        if (length_check(key))
        {
            if (alpha_check(key))
            {
                if (unique_check(key))
                {
                    string plaintext = get_string("plaintext:  ");
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
                    printf("Argument cannot contain duplicate letters\n");
                    return 1;
                }
            }

            else
            {
                printf("Argument must contain only letters.\n");
                return 1;
            }

        }
        else
        {
            printf("Argument must contain 26 characters.\n");
            return 1;
        }
    }
    else
    {
        printf("Too many or too few arguments.\n");
        return 1;
    }
}

bool alpha_check(string text)
{
    int i = 0;
    while (text[i] != '\0')
    {
        if (isalpha(text[i]))
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

bool unique_check(string text)
{
    int i = 0;
    while (text[i] != '\0')
    {
        int j = i + 1;
        while (text[j] != '\0')
        {
            if (text[i] != text[j])
            {
                j++;
            }
            else
            {
                return false;
            }
        }
        i++;
    }
    return true;
}

bool length_check(string text)
{
    int i = 0;
    while (text[i] != '\0')
    {
        i++;
    }
    if (i == 26)
    {
        return true;
    }
    else
    {
        return false;
    }
}

string uppercase(string text)
{
    int i = 0;
    while (text[i] != '\0')
    {
        if (islower(text[i]))
        {
            text[i] = toupper(text[i]);
            i++;
        }

        else
        {
            i++;
        }
    }
    return text;
}

string lowercase(string text)
{
    int i = 0;
    while (text[i] != '\0')
    {
        if (isupper(text[i]))
        {
            text[i] = tolower(text[i]);
            i++;
        }

        else
        {
            i++;
        }
    }
    return text;
}

char rotate(char character, string key)
{
    int asciival = character;
    if (islower(character))
    {
        asciival = character - 97;
        char cipherchar = key[asciival];
        cipherchar = tolower(cipherchar);
        return cipherchar;
    }

    else if (isupper(character))
    {
        asciival = character - 65;
        char cipherchar = key[asciival];
        return cipherchar;
    }
    else
    {
        return character;
    }
}