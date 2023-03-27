            if (i == (height - 1) && j == (width - 1)) //bottom right corner pixel
            {
                RGBTRIPLE mid = image[i][j];
                RGBTRIPLE up = image[i - 1][j];
                RGBTRIPLE left = image[i][j - 1];
                RGBTRIPLE uleft = image[i - 1][j - 1];

                red_avg = round((mid.rgbtRed + up.rgbtRed + left.rgbtRed + uleft.rgbtRed) / 4);
                green_avg = round((mid.rgbtGreen + up.rgbtGreen + left.rgbtGreen + uleft.rgbtGreen) / 4);
                blue_avg = round((mid.rgbtBlue + up.rgbtBlue + left.rgbtBlue + uleft.rgbtBlue) / 4);
            }

            else if (i == (height - 1) && (0 < j < (width - 1))) //bottom edge pixels between corners
            {
                RGBTRIPLE mid = image[i][j];
                RGBTRIPLE up = image[i - 1][j];
                RGBTRIPLE left = image[i][j - 1];
                RGBTRIPLE right = image[i][j + 1];
                RGBTRIPLE uleft = image[i - 1][j - 1];
                RGBTRIPLE uright = image[i - 1][j + 1];

                red_avg = round((mid.rgbtRed + up.rgbtRed + left.rgbtRed + right.rgbtRed + uleft.rgbtRed + uright.rgbtRed) / 6);
                green_avg = round((mid.rgbtGreen + up.rgbtGreen + left.rgbtGreen + right.rgbtGreen + uleft.rgbtGreen + uright.rgbtGreen) / 6);
                blue_avg = round((mid.rgbtBlue + up.rgbtBlue + left.rgbtBlue + right.rgbtBlue + uleft.rgbtBlue + uright.rgbtBlue) / 6);
            }

            else if (i == (height - 1) && j == 0) //bottom left corner pixel
            {
                RGBTRIPLE mid = image[i][j];
                RGBTRIPLE up = image[i - 1][j];
                RGBTRIPLE right = image[i][j + 1];
                RGBTRIPLE uright = image[i - 1][j + 1];

                red_avg = round((mid.rgbtRed + up.rgbtRed + right.rgbtRed + uright.rgbtRed) / 4);
                green_avg = round((mid.rgbtGreen + up.rgbtGreen + right.rgbtGreen + uright.rgbtGreen) / 4);
                blue_avg = round((mid.rgbtBlue + up.rgbtBlue + right.rgbtBlue + uright.rgbtBlue) / 4);
            }

            else if (((height - 1) > i > 0) && j == (width - 1)) //right edge pixels between corners
            {
                RGBTRIPLE mid = image[i][j];
                RGBTRIPLE up = image[i - 1][j];
                RGBTRIPLE down = image[i + 1][j];
                RGBTRIPLE left = image[i][j - 1];
                RGBTRIPLE uleft = image[i - 1][j - 1];
                RGBTRIPLE dleft = image[i + 1][j - 1];

                red_avg = round((mid.rgbtRed + up.rgbtRed + down.rgbtRed + left.rgbtRed + uleft.rgbtRed + dleft.rgbtRed) / 6);
                green_avg = round((mid.rgbtGreen + up.rgbtGreen + down.rgbtGreen + left.rgbtGreen + uleft.rgbtGreen + dleft.rgbtGreen) / 6);
                blue_avg = round((mid.rgbtBlue + up.rgbtBlue + down.rgbtBlue + left.rgbtBlue + uleft.rgbtBlue + dleft.rgbtBlue) / 6);
            }

            else if (((height - 1) > i > 0) && j == 0) //left edge pixels between corners
            {
                RGBTRIPLE mid = image[i][j];
                RGBTRIPLE up = image[i - 1][j];
                RGBTRIPLE down = image[i + 1][j];
                RGBTRIPLE right = image[i][j + 1];
                RGBTRIPLE uright = image[i - 1][j + 1];
                RGBTRIPLE dright = image[i + 1][j + 1];

                red_avg = round((mid.rgbtRed + up.rgbtRed + down.rgbtRed + right.rgbtRed + uright.rgbtRed + dright.rgbtRed) / 6);
                green_avg = round((mid.rgbtGreen + up.rgbtGreen + down.rgbtGreen + right.rgbtGreen + uright.rgbtGreen + dright.rgbtGreen) / 6);
                blue_avg = round((mid.rgbtBlue + up.rgbtBlue + down.rgbtBlue + right.rgbtBlue + uright.rgbtBlue + dright.rgbtBlue) / 6);
            }

            else if (i == 0 && j == (width - 1)) //top right corner pixel
            {
                RGBTRIPLE mid = image[i][j];
                RGBTRIPLE down = image[i + 1][j];
                RGBTRIPLE left = image[i][j - 1];
                RGBTRIPLE dleft = image[i + 1][j - 1];

                red_avg = round((mid.rgbtRed + left.rgbtRed + down.rgbtRed + dleft.rgbtRed) / 4);
                green_avg = round((mid.rgbtGreen + left.rgbtGreen + down.rgbtGreen + dleft.rgbtGreen) / 4);
                blue_avg = round((mid.rgbtBlue + left.rgbtBlue + down.rgbtBlue + dleft.rgbtBlue) / 4);
            }

            else if  (i == 0 && (0 < j < (width - 1))) //top edge pixels between corners
            {
                RGBTRIPLE mid = image[i][j];
                RGBTRIPLE down = image[i + 1][j];
                RGBTRIPLE left = image[i][j - 1];
                RGBTRIPLE right = image[i][j + 1];
                RGBTRIPLE dleft = image[i + 1][j - 1];
                RGBTRIPLE dright = image[i + 1][j + 1];

                red_avg = round((mid.rgbtRed + left.rgbtRed + right.rgbtRed + down.rgbtRed + dleft.rgbtRed + dright.rgbtRed) / 6);
                green_avg = round((mid.rgbtGreen + left.rgbtGreen + right.rgbtGreen + down.rgbtGreen + dleft.rgbtGreen + dright.rgbtGreen) / 6);
                blue_avg = round((mid.rgbtBlue + left.rgbtBlue + right.rgbtBlue + down.rgbtBlue + dleft.rgbtBlue + dright.rgbtBlue) / 6);
            }

            else if (i == 0 && j == 0) //top left corner pixel
            {
                RGBTRIPLE mid = image[i][j];
                RGBTRIPLE down = image[i + 1][j];
                RGBTRIPLE right = image[i][j + 1];
                RGBTRIPLE dright = image[i + 1][j + 1];

                red_avg = round((mid.rgbtRed + right.rgbtRed + down.rgbtRed + dright.rgbtRed) / 4);
                green_avg = round((mid.rgbtGreen + right.rgbtGreen + down.rgbtGreen + dright.rgbtGreen) / 4);
                blue_avg = round((mid.rgbtBlue + right.rgbtBlue + down.rgbtBlue + dright.rgbtBlue) / 4);
            }

            else //all other pixels
            {
                RGBTRIPLE mid = image[i][j];
                RGBTRIPLE up = image[i - 1][j];
                RGBTRIPLE down = image[i + 1][j];
                RGBTRIPLE left = image[i][j - 1];
                RGBTRIPLE right = image[i][j + 1];
                RGBTRIPLE uleft = image[i - 1][j - 1];
                RGBTRIPLE uright = image[i - 1][j + 1];
                RGBTRIPLE dleft = image[i + 1][j - 1];
                RGBTRIPLE dright = image[i + 1][j + 1];

                red_avg = round((mid.rgbtRed + up.rgbtRed + down.rgbtRed + left.rgbtRed + right.rgbtRed + uleft.rgbtRed + uright.rgbtRed + dleft.rgbtRed + dright.rgbtRed) / 9);
                green_avg = round((mid.rgbtGreen + up.rgbtGreen + down.rgbtGreen + left.rgbtGreen + right.rgbtGreen + uleft.rgbtGreen + uright.rgbtGreen + dleft.rgbtGreen + dright.rgbtGreen) / 9);
                blue_avg = round((mid.rgbtBlue + up.rgbtBlue + down.rgbtBlue + left.rgbtBlue + right.rgbtBlue + uleft.rgbtBlue + uright.rgbtBlue + dleft.rgbtBlue + dright.rgbtBlue) / 9);
            }