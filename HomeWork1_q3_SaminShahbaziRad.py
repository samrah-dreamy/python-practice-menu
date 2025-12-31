"""
3. Write a script to sum all even numbers between 1 and 100.
سوال سوم تمرین اول - برنامه نویسی پیشرفته
ثمین شهبازی راد - 14044143
"""


def sum_all_the_even_numbers_from_0_to_100():
    print("------------------------------")
    print("سوال سوم تمرین اول - برنامه نویسی پیشرفته")
    print("------------------------------")

    sum_all_the_even_numbers = 0
    for i in range(0, 102, 2):
        # print(i)
        sum_all_the_even_numbers += i

    print("جمع اعداد زوج صفر تا صد:", sum_all_the_even_numbers)


if __name__ == "__main__":
    sum_all_the_even_numbers_from_0_to_100()
