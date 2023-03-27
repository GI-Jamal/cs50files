#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            int gs_average = round((red + green + blue) / 3);

            image[i][j].rgbtRed = gs_average;
            image[i][j].rgbtGreen = gs_average;
            image[i][j].rgbtBlue = gs_average;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            float sp_valr = round(.393 * red + .769 * green + .189 * blue);
            float sp_valg = round(.349 * red + .686 * green + .168 * blue);
            float sp_valb = round(.272 * red + .534 * green + .131 * blue);

            if (sp_valr > 255)
            {
                sp_valr = 255;
            }

            if (sp_valg > 255)
            {
                sp_valg = 255;
            }

            if (sp_valb > 255)
            {
                sp_valb = 255;
            }

            image[i][j].rgbtRed = sp_valr;
            image[i][j].rgbtGreen = sp_valg;
            image[i][j].rgbtBlue = sp_valb;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp_pixel[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            temp_pixel[i][j] = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp_pixel[i][j];
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp_image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red_total = 0;
            float green_total = 0;
            float blue_total = 0;
            int counter = 0;

            for (int y = -1; y < 2; y++)
            {
                for (int x = -1; x < 2 ; x++)
                {
                    int y_val = i + y;
                    int x_val = j + x;

                    if (x_val < 0 || y_val < 0 || x_val > (width - 1) || y_val > (height - 1))
                    {

                    }

                    else
                    {
                        red_total += image[y_val][x_val].rgbtRed;
                        green_total += image[y_val][x_val].rgbtGreen;
                        blue_total += image[y_val][x_val].rgbtBlue;
                        counter++;
                    }
                }
            }

            temp_image[i][j].rgbtRed = round(red_total / counter);
            temp_image[i][j].rgbtGreen = round(green_total / counter);
            temp_image[i][j].rgbtBlue = round(blue_total / counter);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp_image[i][j];
        }
    }

    return;
}