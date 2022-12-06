GIFTS = ["Twelve drummers drumming",
         "Eleven pipers piping",
         "Ten lords a-leaping",
         "Nine ladies dancing",
         "Eight maids a-milking",
         "Seven swans a-swimming",
         "Six geese a-laying",
         "Five golden rings",
         "Four calling birds",
         "Three french hens",
         "Two turtle doves",
         "A partridge in a pear tree. "]

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


def song(day, chorus, gifts):
    print(chorus)
    for i in range(day):
        print(chorus)


def chorus(day):
    print(f"On the {DAYS[day]} of Christmas, my true love gave to me...\n")


def main():
    day = input("Enter day of Christmas (1-12): ")

    if day.isdigit():
        day = int(day)
    else:
        print("Please enter an integer. ")
    if day > 12:
        print("There are only 12 days of Christmas. ")
    if day < 1:
        print("You'll have to wait until the first day of Christmas for your gift. ")
    else:
        chorus(day)


main()
