
def sum_all_the_even_numbers_from_0_to_100():
    print("------------------------------")

    sum_all_the_even_numbers = 0
    for i in range(0, 102, 2):
        # print(i)
        sum_all_the_even_numbers += i

    print("جمع اعداد زوج صفر تا صد:", sum_all_the_even_numbers)
    print("sum of all the even numbers from 0 to 100 is: ", sum_all_the_even_numbers)


if __name__ == "__main__":
    sum_all_the_even_numbers_from_0_to_100()
