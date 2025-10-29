grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce") 
}
# Recuperando o item Bread do dicionario 
bread_details = grocery_inventory.get("Bread")
#Adicionando um novo item Cookies:
grocery_inventory.update({"Cookies":(143, "Bakery")})
print("Inventory after adding Cookies:", grocery_inventory)

grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)
#Imprimindo o que foi pedido:
print("Details of Bread:", bread_details)
