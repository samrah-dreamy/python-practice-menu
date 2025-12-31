"""
1. write a python program to calculate area and perimeter of a rectangle.
سوال اول تمرین اول - برنامه نویسی پیشرفته
ثمین شهبازی راد - 14044143
"""


def calculate_area_and_perimeter_of_a_rectangle():
    print("------------------------------")
    print("سوال اول تمرین اول - برنامه نویسی پیشرفته")
    print("------------------------------")
    rectangle_length, rectangle_width = 1, 1
    while True:
        try:
            rectangle_length = float(input("طول مستطیل مورد نظر را وارد کنید:\n"))
        except ValueError:
            print("مقدار مورد نظر باید عدد باشد")
            continue
        else:
            print("طول با موفقیت دریافت شد")
            break

    print("------------------------------")

    while True:
        try:
            rectangle_width = float(input("عرض مستطیل مورد نظر را وارد کنید:\n"))
        except ValueError:
            print("مقدار مورد نظر باید عدد باشد")
            continue
        else:
            print("عرض با موفقیت دریافت شد")
            break

    print("------------------------------")

    rectangle_area = rectangle_length * rectangle_width
    rectangle_perimeter = 2 * (rectangle_length + rectangle_width)

    print("مساحت (Area) مستطیل مورد نظر شما:", rectangle_area)
    print("محیط (Perimeter) مورد نظر شما:", rectangle_perimeter)

    print("------------------------------")


if __name__ == "__main__":
    calculate_area_and_perimeter_of_a_rectangle()
