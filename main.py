
import HomeWork1_q1_SaminShahbaziRad as q1
import HomeWork1_q2_SaminShahbaziRad as q2
import HomeWork1_q3_SaminShahbaziRad as q3


while True:
    print("------------------------------")
    print("--- به منوی حل سوالات خوش امدید ---")
    print("--- Welcome to the Problem Solving Menu ---")

    print("برای دیدن حل سوال اول (بررسی محیط و مساحت مستطیل) عدد یک را فشار دهید.", "1")
    print("Press 1 to see the solution to Question 1 (Rectangle area and perimeter).")

    print("برای دیدن حل سوال دوم (نمایش جدول ضرب عدد دلخواه) عدد دو را فشار دهید.", "2")
    print("Press 2 to see the solution to Question 2 (Display the multiplication table of a given number).")

    print("برای دیدن حل سوال سوم (جمع اعداد زوج صفر تا صد) عدد سه را فشار دهید.", "3")
    print("Press 3 to see the solution to Question 3 (Sum of even numbers from 0 to 100).")

    print("برای خارج شدن از منو عدد چهار را فشار دهید.", "4")
    print("Press 4 to exit the menu.")
    print("------------------------------")

    try:
        choice_menu = int(input())
    except ValueError:
        print("لطفا با توجه به منو عدد وارد کنید")
        print("Please enter a number according to the menu.")
        continue
    else:
        print("در حال پردازش ورودی...")
        print("Processing your input...")

    if choice_menu == 1:
        q1.calculate_area_and_perimeter_of_a_rectangle()
    elif choice_menu == 2:
        q2.print_the_multiplication()
    elif choice_menu == 3:
        q3.sum_all_the_even_numbers_from_0_to_100()
    elif choice_menu == 4:
        print("بازم برگرد! 3>")
        print("Come back again! See you soon! <3")
        break
    else:
        print("لطفا منو را با دقت بررسی کرده و با توجه به منو از اعداد 1 تا 4 عدد مورد نظر را انتخاب کنید")
        print("Please check the menu carefully and choose a number between 1 and 4.")
