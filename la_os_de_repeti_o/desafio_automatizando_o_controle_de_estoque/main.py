# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started")
for item in inventory:
    estoque_atual, estoque_minimo, quantidade_de_reabastecimento, status_de_promocao = inventory[item]
    print("Processing", item)
    while estoque_atual < estoque_minimo:
        estoque_atual += quantidade_de_reabastecimento
        inventory[item][0] = estoque_atual
    if estoque_atual > discount_threshold and not status_de_promocao:
        inventory[item][3] = True

print("Processing completed")

   