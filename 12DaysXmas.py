# Dictionary of Christmas gifts. Key represents day of Christmas
GIFTS = {1: "A partridge in a pear tree. \n",
         2: "Two turtle doves",
         3: "Three french hens",
         4: "Four calling birds",
         5: "Five golden rings",
         6: "Six geese a-laying",
         7: "Seven swans a-swimming",
         8: "Eight maids a-milking",
         9: "Nine ladies dancing",
         10: "Ten lords a-leaping",
         11: "Eleven pipers piping",
         12: "Twelve drummers drumming"}

# Dictionary of appropriate word forms for each day
DAYS = {1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"}


def verses(day):
    print(f"On the {DAYS[day]} day of Christmas, my true love gave to me...")
    for i in range(day, 0, -1):
        if day == 1:
            print(GIFTS[i])
        elif i == 1:
            print(f"And {GIFTS[1].lower()}")
        else:
            print(GIFTS[i])
# Prints the chorus filled with the appropriate word form for the chosen day followed by the gifts received up until that day
# Changes the first day gift verse to be grammatically appropriate for multiple days versus just one day


def total_gifts(day):
    if day == 1:
        print(
            f"By the {DAYS[day]} day of Christmas you've received {sum(int(i) for i in range(1, day+1))} gift. Wow!")
    else:
        print(
            f"By the {DAYS[day]} day of Christmas you've received {sum(int(i) for i in range(1, day+1))} gifts. Wow!")
# Prints the total gifts received by the chosen day including those received on that day.
# 'if' statement is literally just to change the word "gifts" to "gift" if first day is selected


def song():
    while True:
        day = input("Enter day of Christmas (1-12): ")
        print()
        if day.isdigit():
            day = int(day)
        else:
            print("Please enter an integer. ")
            return
        if day > 12:
            print("There are only 12 days of Christmas. ")
            return
        if day < 1:
            print("You'll have to wait until the first day of Christmas for your gift. ")
            return
        else:
            verses(day)
        total_gifts(day)
        break


song()
