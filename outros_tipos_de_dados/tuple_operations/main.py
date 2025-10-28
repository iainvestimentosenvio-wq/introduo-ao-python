# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]
# convertendo shelf1_update em uma tupla:
shelf1_update_tuple = tuple(shelf1_update)
# Concatenar :
shelf1_concat = shelf1 + shelf1_update_tuple
# Contar quantas vezes "celery" aparece em shelf1_concat: (.count)
celery_count = shelf1_concat.count("celery")
# Encontrando o indice da 1º ocorrencia de "celery" em shelf1_concat: (.index)
celery_index = shelf1_concat.index("celery")
# Exibindo mensagens exigidas: 
print("Updated Shelf #1:",  shelf1_concat)
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)
