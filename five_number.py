#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, showing numbers from 1000 to 2000, five in a row


def main():
    # This function shows numbers from 1000 - 2000

    # process & output
    for initial_counter in range(1000, 2001):
        if (initial_counter + 1) % 5 == 0:
            print("{}".format(initial_counter))
        else:
            print(initial_counter, end = " ")
    print("\n\nDone.")


if __name__ == "__main__":
    main()
