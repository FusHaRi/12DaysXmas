GIFTS = {1: "and a partridge in a pear tree. \n",
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


def song(day):
    print(f"On the {DAYS[day]} day of Christmas, my true love gave to me...")
    for i in range(day+1, 0, -1):
        print(GIFTS[i])


def main():
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
            song(day)
        print(
            f"By the {DAYS[day]} day of Christmas you've received {int((day-1)*(day/2))} gifts")
        break


main()
