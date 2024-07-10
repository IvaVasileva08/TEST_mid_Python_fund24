from math import ceil
budget = float(input())
student = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

packages_flour = student  - student // 5
total_flour_cost = packages_flour * price_flour
total_egg_cost = student  * 10 * price_egg
total_apron_cost = ceil(student * 1.2) * price_apron
needed_items = total_flour_cost + total_egg_cost + total_apron_cost

if needed_items <= budget:
    print(f"Items purchased for {needed_items:.2f}$.")
else:
    print(f"{(needed_items - budget):.2f}$ more needed.")