RGBTRIPLE temp_image[height][width];

    for (int i = 1; i < height; i++)
    {
        for (int j = 1; j < width; j++)
        {
            temp_image[i][j] = image[i][j];
        }
    }

