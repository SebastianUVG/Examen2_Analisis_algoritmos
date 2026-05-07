def ejercicio1(monto):
    m = int(round(monto * 100))
    monedas = [25, 10, 5, 1]
    resultado = {}

    print(f"\nResolviendo cambio para Q{monto}")
    print(f"Total en centavos: {m}")

    for moneda in monedas:
        cantidad = m // moneda
        print(f"\nEvaluando moneda de {moneda}:")
        print(f"Se pueden usar {cantidad} monedas")

        if cantidad > 0:
            resultado[moneda] = cantidad
            m = m % moneda
            print(f"Nuevo restante: {m}")

    print("\nResultado final:", resultado)
    return resultado

# Ejemplo de uso
print('Ejemplo 1:\n')
ejercicio1(2.93)
print('Ejemplo 2:\n')
ejercicio1(4.87)
print('Ejemplo 3:\n')
ejercicio1(0.99)