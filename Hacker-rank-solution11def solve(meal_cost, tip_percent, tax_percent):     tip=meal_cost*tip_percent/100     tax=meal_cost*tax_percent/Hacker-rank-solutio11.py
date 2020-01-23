#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
#and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

def solve(meal_cost, tip_percent, tax_percent):
    tip=meal_cost*tip_percent/100
    tax=meal_cost*tax_percent/100
    total=int(round(meal_cost+tip+tax))
    print(total)

meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())
