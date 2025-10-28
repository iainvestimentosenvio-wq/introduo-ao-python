# 1. Defina a lista inicial
vegetables = ["tomatoes", "potatoes", "onions"]
# Remover "onions"
vegetables.remove("onions")
# Imprimindo Adicionando "carrots"
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")
# Imprimindo e adicionando "cucumbers"
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")
# Colocando em ordem alfabetica:
vegetables.sort()
# Imprimindo o final pedido : 
print("Updated Vegetable Inventory:", vegetables)