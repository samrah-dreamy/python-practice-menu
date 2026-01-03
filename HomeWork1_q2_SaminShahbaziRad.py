
def print_the_multiplication():
    print("------------------------------")
    number_to_multiplication = 0
    range_end_number = 10
    while True:
        try:
            print("Enter the desired item: ")
            number_to_multiplication = int(input("عدد مورد نظر را وارد کنید:\n"))
        except ValueError:
            print("the value you entered should be float number")
            print("مقدار مورد نظر باید عدد طبیعی باشد")
            continue
        else:
            print("عدد مورد نظر با موفقیت دریافت شد")
            break

    print("------------------------------")

    while True:
        try:
            range_end_number = int(input("بازه مورد نظر از 1 تا چه عددی میخواهید را تعیین کنید. (پیش فرض 10 است و باید یک عدد وارد کنید):\n") or 10)
        except ValueError:
            print("مقدار مورد نظر باید عدد طبیعی باشد")
            continue
        else:
            print(f"بازه مورد نظر از 1 تا {range_end_number} با موفقیت تعیین شد")
            break

    print("------------------------------")

    for i in range(1, range_end_number + 1):
        print(f"{number_to_multiplication} x {i:2d} = {number_to_multiplication * i}")

    print("------------------------------")


if __name__ == "__main__":
    print_the_multiplication()
