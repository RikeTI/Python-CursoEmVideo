"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
acc = cont = 0
while True:
    n = int(input('Digite um número: [999 p/ parar] '))
    if n == 999:
        break
    else:
        acc += n
        cont += 1
print(f'A quantidade de números informados foi {cont}')
print(f'A soma de todos números informados foi {acc}')



