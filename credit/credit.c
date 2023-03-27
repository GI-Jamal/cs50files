#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long cardNumber;
    long cardType;
    long counter;
    int sum;
    int remainder;
    int luhnMod;
    int cardLength;
    int totalMod;

    do
    {
        cardNumber = get_long("Number: ");
    }
    while (cardNumber < 0);

    cardType = cardNumber;

    while (cardType > 99)
    {
        cardType = cardType / 10;
    }

    counter = cardNumber;

    while (counter > 0)
    {
        cardLength = cardLength + 1;
        counter = counter / 10;
    }

    while (cardNumber > 0)
    {
        remainder = remainder + (cardNumber % 10);
        cardNumber = cardNumber / 10;
        luhnMod = (cardNumber % 10) * 2;
        if (luhnMod > 9)
        {
            sum = sum + (luhnMod - 9);
        }
        else
        {
            sum = sum + luhnMod;
        }
        cardNumber = cardNumber / 10;
    }

    totalMod = (remainder + sum) % 10;

    if (totalMod == 0)
    {
        if ((cardType == 34 || cardType == 37) && cardLength == 15)
        {
            printf("AMEX\n");
        }
        else if ((cardType >= 51 && cardType <= 55) && cardLength == 16)
        {
            printf("MASTERCARD\n");
        }
        else if ((cardType >= 40 && cardType <= 49) && (cardLength == 13 || cardLength == 16))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}