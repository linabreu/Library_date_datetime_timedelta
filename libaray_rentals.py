#!/usr/bin/env python3

#library due date calculator using date, datetime and timedelta objects

from datetime import date, datetime, timedelta

def get_checkout_date():
    while True:
        checkout_date_input = input("Enter the checkout date (MM/DD/YYYY): ")
        try:
            date_obj = datetime.strptime(checkout_date_input, "%m/%d/%Y") #convert user input to datetime object
        except ValueError:
            print("Error.Incorrect date format. Please try again")
            continue
        
        checkout_date = date(date_obj.year, date_obj.month, date_obj.day)

        if checkout_date > date.today():
            print("Error.Checkout date cannot be in the future")
            continue
        else:
            return checkout_date


def main():
    print("County Library Due Date Program")
    print()

    while True:
        checkout_date = get_checkout_date()
        print()

        #calculate due date and number of days overdue
        due_date = checkout_date + timedelta(days=14) #books are due 14 days from rental date
        today = date.today() #get current date
        days_overdue = (today - due_date).days #calculate how many days overdue

        #display information
        print("Checkout Date:  " + checkout_date.strftime("%B %d, %Y")) #format as Month, DD, YYYY
        print("Due Date:    :  " + due_date.strftime("%B %d, %Y"))
        print("Today's Date :  " + today.strftime("%B %d, %Y"))
        print()
        if days_overdue > 0:
            print("This book is", days_overdue, "day(s) overdue.")
            late_fee = str(days_overdue * 0.10) #10 cents per day late
            print("The late fee is: " + "$" +late_fee + "0")
        else:
            days_until_due = days_overdue * -1
            print("This book is due in", days_until_due, "day(s).")
        print()

        #ask if they want to check the status of another rental
        another = input("Would you like to check the status of another rental? (y/n): ")
        print()
        if another.lower() !="y" or another.upper() !="Y": #make sure they can put in upper or lower case
            print("Thank you for renting with the County Library")
            break
        
if __name__ == "__main__":
    main()
