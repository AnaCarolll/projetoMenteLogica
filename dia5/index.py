#estrutura de repetição -> loops
#repetir n vezes
#nde n, a gente pode definir
# o n é uma cndição

frutas = ['maçã', 'banana', 'uva', 'pera']

#fot itm_individual in listas;
# bloco repetido N vezes


for frutas in frutas:
    print(frutas)



estojoDeCanetinhas = ['preta', 'amarela', 'branca', 'rosa', 'lilas']
#canetinha -> item que vai guardar oque você esta preenchendo da lista
#estojoDeCanetinhas -> lista que você esta pegando os itens
for canetinha in estojoDeCanetinhas:
    if canetinha == 'lilas':
        print(f'encontrei a canetinha lilas')
        print(f"Pintando a tampa da {canetinha}")
    print(canetinha)