# Dicionario de itens:
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50) 
}
# Verificando e atualizando os precos :
price_of_eggs = grocery_inventory["Eggs"][1]
if price_of_eggs > 5.00:
    print("Eggs are too expensive, reducing the price by $1.")
    price_of_eggs = price_of_eggs - 1.00
    grocery_inventory["Eggs"] = (
    grocery_inventory["Eggs"][0],
    price_of_eggs,
    grocery_inventory["Eggs"][2],
)
else:
    print("The price of Eggs is reasonable.")
# Adicionando Tomatoes a grocery_inventory:
grocery_inventory ["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)
# Gerenciando o Estoque
estoque_milk = grocery_inventory["Milk"][2]
if estoque_milk < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    estoque_milk = estoque_milk + 20
    grocery_inventory["Milk"] = (
    grocery_inventory["Milk"][0],
    grocery_inventory["Milk"][1],
    estoque_milk,
)
else:
    print("Milk has sufficient stock.")
# Removendo item com base no valor 
preco_de_apples = grocery_inventory["Apples"][1]
if preco_de_apples > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
# Impressao final 
print("Updated inventory:", grocery_inventory)
    