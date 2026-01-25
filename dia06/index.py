# listas (array) e tuplas
# interligads com os loops - estruturas de repetição

carros = ['palio', 'gol', 'celta', 'uno']
for carro in carros:
    print(carro)

#tuplas -> listas imutáveis
#tuplas são listas que não podem ser alteradas

frutas = ('maçã', 'banana', 'uva', 'pera')
frutas.append('laranja')  # Isso vai gerar um erro, pois tuplas são imutáveis
print(frutas)
# for fruta in frutas:
#     print(fruta)

# frutas[0] = 'laranja' -> isso não é possível em tuplas
# frutas.append('laranja') -> isso não é possível em tuplas
# frutas.remove('banana') -> isso não é possível em tuplas
# frutas.pop() -> isso não é possível em tuplas
# frutas.sort() -> isso não é possível em tuplas
# frutas.reverse() -> isso não é possível em tuplas

for fruta in frutas:
    print(fruta)


#tuplas são usadas quando queremos garantir que os dados não serão alterados
