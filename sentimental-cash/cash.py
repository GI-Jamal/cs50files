from cs50 import get_float


def main():
    cents = get_cents()
    quarters = get_quarters(cents)
    cents = cents - (quarters * 25)
    dimes = get_dimes(cents)
    cents = cents - (dimes * 10)
    nickels = get_nickels(cents)
    cents = cents - (nickels * 5)
    pennies = get_pennies(cents)
    total = quarters + dimes + nickels + pennies
    print(int(total))


def get_cents():
    while (True):
        cents = get_float("Change owed: ")
        if cents >= 0:
            return cents * 100


def get_quarters(cents):
    quarter_mod = cents % 25
    quarter_count = (cents - quarter_mod) / 25
    return quarter_count


def get_dimes(cents):
    dime_mod = cents % 10
    dime_count = (cents - dime_mod) / 10
    return dime_count


def get_nickels(cents):
    nickel_mod = cents % 5
    nickel_count = (cents - nickel_mod) / 5
    return nickel_count


def get_pennies(cents):
    return cents


main()