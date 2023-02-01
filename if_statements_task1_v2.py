def calculate_gross_pay(hours, rate):
    if hours <= 40:
        gross_pay = hours * rate
    else:
        overtime = hours - 40
        overtime_pay = overtime * rate * 1.5
        gross_pay = (40 * rate) + overtime_pay

    return f"Gross pay for the week: £{gross_pay:.2f}"

hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter your rate of pay in pounds: "))
print(calculate_gross_pay(hours, rate))