from cs50 import get_int


def main():
    card_number = get_cardnumber()
    card_length = get_cardlength(card_number)
    card_type = get_cardtype(card_number)
    card_mod = get_cardmod(card_number)
    check_card(card_length, card_type, card_mod)


def get_cardnumber():
    while (True):
        card_number = get_int("Number: ")
        if card_number >= 0:
            return card_number


def get_cardlength(card_number):
    card_length = len(str(card_number))
    return card_length


def get_cardtype(card_number):
    while card_number > 99:
        card_number = card_number // 10
    return card_number


def get_cardmod(card_number):
    remainder = 0
    sum = 0
    while card_number > 0:
        remainder = remainder + (card_number % 10)
        card_number = card_number // 10
        luhnmod = (card_number % 10) * 2
        if luhnmod > 9:
            sum = sum + (luhnmod - 9)
        else:
            sum = sum + luhnmod
        card_number = card_number // 10
    card_mod = (remainder + sum) % 10
    return card_mod


def check_card(card_length, card_type, card_mod):
    if card_mod == 0:
        if (card_type == 34 or card_type == 37) and card_length == 15:
            print("AMEX")
        elif (card_type >= 51 and card_type <= 55) and card_length == 16:
            print("MASTERCARD")
        elif (card_type >= 40 and card_type <= 49) and (card_length == 13 or card_length == 16):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


main()