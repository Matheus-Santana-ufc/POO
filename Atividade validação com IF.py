import math

escolher_verificacao = input('Digite 1 para verificar triângulo, 2 para verificar quadrilátero ou 3 para receber as coordenadas de um determinado tipo de triângulo : ')
if escolher_verificacao == '1':
    x1 = float(input('Digite a coordenada de x1: '))
    y1 = float(input('Digite a coordenada de y1: '))
    x2 = float(input('Digite a coordenada de x2: '))
    y2 = float(input('Digite a coordenada de y2: '))
    x3 = float(input('Digite a coordenada de x3: '))
    y3 = float(input('Digite a coordenada de y3: '))

    lado1 = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 ))
    lado2 = int(math.sqrt((x3 - x1)**2 + (y3 - y1)**2 ))
    lado3 = int(math.sqrt((x3 - x2)**2 + (y3 - y2)**2 ))

    if lado1 == lado2 and lado1 == lado3:
        print('É um triângulo Equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('É um triangulo Isósceles')
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print('É um triângulo Escaleno')
    else:
        print('Não é um triângulo')
elif escolher_verificacao == '2': 
    x1 = float(input('Digite a coordenada de x1: '))
    y1 = float(input('Digite a coordenada de y1: '))
    x2 = float(input('Digite a coordenada de x2: '))
    y2 = float(input('Digite a coordenada de y2: '))
    x3 = float(input('Digite a coordenada de x3: '))
    y3 = float(input('Digite a coordenada de y3: '))
    x4 = float(input('Digite a coordenada de x4: '))
    y4 = float(input('Digite a coordenada de y4: '))

    lado1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    lado2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    lado3 = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
    lado4 = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)
    if lado1 == lado2 and lado1 == lado3 and lado1 == lado4:
        print('É um Quadrado')
    elif lado1 != lado2 and lado1 == lado3 and lado2 == lado4:
        print('É um Retângulo')
    else: 
        print('Não é um quadrilátero verificável')

elif escolher_verificacao == '3':
    triangulo = input('Digite o tipo de triangulo[Equilátero,Escaleno,Isósceles]: ').lower()
    if triangulo == 'equilátero':
        print('x1,y1:(0,0)\nx2,y2:(0,8)\nx3,y3:(7,4)')
    elif triangulo == 'isósceles':
        print('x1,y1:(0,0)\nx2,y2:(4,0)\nx3,y3:(2,3)')
    elif triangulo == 'escaleno':
        print('x1,y1:(0,0)\nx2,y2:(1,5)\nx3,y3:(6,0)')
    else:
        print('Escolha uma opção válida')

else:
    print('Escolha uma opção válida')