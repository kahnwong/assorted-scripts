# input as numbers only WITHOUT spaces, e.g. 1234567890121


def ThaiIDCheck(ID):
    ID = str(ID)
    # print(ID)

    if len(ID) != 13:
        print("Invalid ID")
    else:
        first_twelve_digits = ID[:-1]
        # print(first_twelve_digits)
        first_twelve_digits_reversed = first_twelve_digits[::-1]
        # print(first_twelve_digits_reversed)

        total_values = 0
        for index, digit in enumerate(first_twelve_digits_reversed, 2):
            total_values += index * int(digit)
        # print(total_values)

        mod = total_values % 11
        # print(mod)

        final_result = 11 - mod
        final_result = str(final_result)[-1]
        # print(final_result)

        if final_result == ID[-1]:
            print("Your ID is valid!")
        else:
            print("Your ID is invalid")


ThaiIDCheck(00000000)
