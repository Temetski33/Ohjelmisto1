#Funktiot ja lista parametrina

"""inventory = ["veitsi", "vesipullo"]

def print_inventory(inventory):
    print("Pelaajalla on:")
    for item in inventory:
        print(item)
    inventory.append("uusi juttu lisätty funktion sisällä")

player1_inventory = ["veitsi", "vesipullo"]
player2_inventory = ["kirves", "eväsleipä"]

print_inventory(player1_inventory)
print_inventory(player2_inventory)
print_inventory(player1_inventory)
print_inventory(player2_inventory)"""

def calc_sum(num1=0, num2=0, num3=0):
    print(f"Laskutoimitus: {num1} + {num2} + {num3}")
    return num1 + num2 + num3

print(calc_sum(2))
print(calc_sum(2, num3=5))
print(calc_sum(1, 4, 6))
#calc_sum(num2=3, num1=3)

# vaihtuvanmittainen argumenttijono
# *nums -> nums muuttujaan muodostuu lista parametreista
def calc_sum_adv(*nums):
    total = 0
    calculation = "Laskutoimitus:"
    for num in nums:
        total += num
        calculation = calculation + " +" + str(num)
    print(calculation)
    return total

print(calc_sum_adv(1, 2, 3, 7))