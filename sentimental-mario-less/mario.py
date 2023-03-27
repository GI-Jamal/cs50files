from cs50 import get_int


def main():
    while (True):
        height = get_int("Height: ")
        if height >= 1 and height <= 8:
            break
    print_pyramid(height)


def print_pyramid(height):
    counter = height - 1
    for i in range(height):
        print(" " * counter, end="")
        print("#" * (height - counter))
        counter -= 1


main()