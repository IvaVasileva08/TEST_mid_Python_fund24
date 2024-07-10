travel_route = input().split('||')
fuel = int(input())
ammunition = int(input())

for command in travel_route:
    action = command.split()

    if action[0] == "Travel":
        distance = int(action[1])
        if fuel >= distance:
            fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            break

    elif action[0] == "Enemy":
        enemy_armor = int(action[1])
        if ammunition >= enemy_armor:
            ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        elif fuel >= enemy_armor * 2:
            fuel -= enemy_armor * 2
            print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    elif action[0] == "Repair":
        added_amount = int(action[1])
        fuel += added_amount
        ammunition += added_amount * 2
        print(f"Ammunitions added: {added_amount * 2}.")
        print(f"Fuel added: {added_amount}.")

    elif action[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break