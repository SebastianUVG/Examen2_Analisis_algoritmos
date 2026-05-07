def ejercicio1(monto):
    # Mejor manejo
    m = int(round(monto * 100))
    
    monedas = [25, 10, 5, 1]
    resultado = {}

    for moneda in monedas:
        cantidad = m // moneda
        if cantidad > 0:
            resultado[moneda] = cantidad
            m = m % moneda  

    return resultado


# Ejemplo de uso
monto = 2.93
res = ejercicio1(monto)

print(f"Monto: Q{monto}")
print("Monedas utilizadas:")
for moneda, cantidad in res.items():
    print(f"{cantidad} moneda(s) de {moneda} centavos")