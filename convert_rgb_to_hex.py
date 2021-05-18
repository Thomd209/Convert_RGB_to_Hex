def convert_nums_to_letters(nums):
    new_nums = []
    for num in nums:
        if num == 15:
            num = 'F'
        elif num == 14:
            num = 'E'
        elif num == 13:
            num = 'D'
        elif num == 12:
            num = 'C'
        elif num == 11:
            num = 'B'
        elif num == 10:
            num = 'A'

        new_nums.append(num)

    return new_nums


def convert_to_hex(r, g, b):
    # your code here :)
    nums = [r, g, b]
    hex_list = []
    hex_num = 0
    for num in nums:
        if num > 255:
            num = 255
        elif num < 0:
            num = 0

        hex_num = num // 16
        hex_list.append(hex_num)

        hex_num = round(round(num / 16 - int(num / 16), 2) * 16)
        hex_list.append(hex_num)

    hex_list = convert_nums_to_letters(hex_list)
    hex_list = [str(hex_list[i]) for i in range(len(hex_list))]
    hex_str = ''.join(hex_list)

    return hex_str


print(convert_to_hex(-20, 275, 125))
