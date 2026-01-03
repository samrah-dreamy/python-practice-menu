
def calculate_area_and_perimeter_of_a_rectangle():
    print("------------------------------")
    rectangle_length, rectangle_width = 1, 1
    while True:
        try:
            print("please enter the rectangle length: ")
            rectangle_length = float(input("طول مستطیل مورد نظر را وارد کنید:\n"))
        except ValueError:
            print("مقدار مورد نظر باید عدد باشد")
            print("the value you entered should be float number")
            continue
        else:
            print("طول با موفقیت دریافت شد")
            print("Rectangle length received successfully")
            break

    print("------------------------------")

    while True:
        try:
            print("please enter the rectangle width: ")
            rectangle_width = float(input("عرض مستطیل مورد نظر را وارد کنید:\n"))
        except ValueError:
            print("مقدار مورد نظر باید عدد باشد")
            print("the value you entered should be float number")
            continue
        else:
            print("عرض با موفقیت دریافت شد")
            print("Rectangle length received successfully")
            break

    print("------------------------------")

    rectangle_area = rectangle_length * rectangle_width
    rectangle_perimeter = 2 * (rectangle_length + rectangle_width)

    print("مساحت (Area) مستطیل مورد نظر شما: ", rectangle_area)
    print("Area of your desired rectangle: ", rectangle_area)

    print("محیط (Perimeter) مورد نظر شما: ", rectangle_perimeter)
    print("Your desired perimeter: ", rectangle_area)

    print("------------------------------")


if __name__ == "__main__":
    calculate_area_and_perimeter_of_a_rectangle()
