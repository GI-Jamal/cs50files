#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    float charactercount = count_letters(text);
    int wordcount = count_words(text);
    float sentencecount = count_sentences(text);
    int offset = sentencecount - 1;
    int truewordcount = wordcount - offset;

    float L = (charactercount / truewordcount) * 100;
    float S = (sentencecount / truewordcount) * 100;

    float grade = (0.0588 * L) - (0.296 * S) - 15.8;

    int roundedgrade = round(grade);

    if (roundedgrade < 1)
    {
        printf("Before Grade 1\n");
    }

    else if (roundedgrade >= 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %i\n", roundedgrade);
    }
}

int count_letters(string text)
{
    int i = 0;
    int count = 0;
    while (text[i] != '\0')
    {
        if (isalnum(text[i]))
        {
            count++;
            i++;
        }
        else
        {
            i++;
        }
    }
    return count;
}

int count_words(string text)
{
    int i = 0;
    int count = 0;
    while (text[i] != '\0')
    {
        if (text[i] == ' ' || text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            count++;
            i++;
        }
        else
        {
            i++;
        }
    }
    return count;
}

int count_sentences(string text)
{
    int i = 0;
    int count = 0;
    while (text[i] != '\0')
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            count++;
            i++;
        }
        else
        {
            i++;
        }
    }
    return count;
}