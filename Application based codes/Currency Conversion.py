#Dollar to Rupees and vice versa
def currency_conversion():
    print("Currency Conversion")
    print("1. Rupees to Dollar")
    print("1. Dollar to Ruppes")
    choice = int(input("Enter the corresponding number with respect to coversion i.e (1 or 2) - "))

    # Fixing rate of currency
    current_1_Dollar_rate_wrt_Rupee = 86.30

    if choice == 1:
        Rupees = float(input("Enter the total Rupees you have to convert into Dollars"))
        Dollar = Rupees/current_1_Dollar_rate_wrt_Rupee
        print(f"The rate of Dollar is {Dollar:.4f}.") # It will print only 4 decimal answer
    elif choice ==2:
        Dollar = float(input("Enter the total Dollars you have to convert into Rupees"))
        Rupees = Dollar*current_1_Dollar_rate_wrt_Rupee
        print(f"The rate of Dollar is {Rupees:.4f}.")  # It will print only 4 decimal answer
    else:
        print("Enter Invalid Option")

#Calling Currency Conversion function
currency_conversion()