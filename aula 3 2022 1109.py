print('INICIO ALULA 3')

contador =1

while (contador <=10):
    print(contador)
    contador = contador+1

# Laço for (python for = for each)

fruta = "Morango"
print(fruta)

fruta1 = "Morango"
fruta2 = "banana"
fruta3 = "pera"

#lista

frutas = ["Morango","banana","pera"]
print(frutas[2])


#criação de funções

preco = 1999.90

#Calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcular um imposto de 5% e retorna a quem pediu...
#Isso é a declaração da função (Como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... aqui é imposto a calcular.. e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

#Explicação de variável local x global
print(preco) #????
preco_produto = 100
print(preco_produto) #????