def ejercicio2(W, valores, pesos):
    items = []
    for i in range(len(valores)):
        ratio = valores[i] / pesos[i]
        items.append((ratio, valores[i], pesos[i]))

    items.sort(reverse=True)

    valor_total = 0.0

    print(f"\nCapacidad inicial: {W}")
    print("Items ordenados por valor/peso:", items)

    for ratio, valor, peso in items:
        print(f"\nEvaluando item (valor={valor}, peso={peso}, ratio={ratio:.2f})")

        if W == 0:
            break

        if peso <= W:
            print("Se toma completo")
            valor_total += valor
            W -= peso
        else:
            print("Se toma fracción")
            fraccion = W / peso
            valor_total += valor * fraccion
            W = 0

        print(f"Valor acumulado: {valor_total}")
        print(f"Capacidad restante: {W}")

    return valor_total

print('Ejemplo 1:\n')
ejercicio2(50, [60,100,120], [10,20,30])
print('\nEjemplo 2:\n')
ejercicio2(60, [100,120,60], [20,30,10])
print('\nEjemplo 3:\n')
ejercicio2(15, [10,5,15], [5,3,9])