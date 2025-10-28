meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
# Criando lista principal:
deli_dept = [meat, cheese, condiment]
# Imprimindo deli_dept como esta:
print("Initial Deli List:", deli_dept)
# Adicionando item sazonal: 
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
# Se meat posicao 2 nao estiver 100 que fique 100:
if meat[2] < 100:
    meat[2] = 100
# Se deli_dept nao tiver seasonal_meat adicionar :
if seasonal_meat not in deli_dept:
    deli_dept.append(seasonal_meat)
if condiment in deli_dept:
    deli_dept.remove(condiment)
deli_dept.sort()

print("Updated Deli List:", deli_dept)
    
 