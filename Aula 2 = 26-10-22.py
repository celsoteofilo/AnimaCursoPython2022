nome = input("Qual e seu nome: ")
idade = int(input('Qual e sua idade: '))

dobro = idade * 2
print('Seu  nome e {} e sua idade e {}'.format(nome,idade))
print(f'O dobro da sua idade e {dobro}')

if idade >= 18:
    print("Voce e maior de idade ")


nome = input("Qual o seu nome? ")
nota_aluno = int(input("Qual a sua nota? "))

if (nota_aluno == 10):
  print(f"Você é o bixão mesmo!")