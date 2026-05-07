def ejercicio2(W, valores, pesos):
    n = len(valores)
    
    # Crear lista de items con (valor, peso, ratio)
    items = []
    for i in range(n):
        ratio = valores[i] / pesos[i]
        items.append((ratio, valores[i], pesos[i]))
    
    # Ordenar por ratio descendente
    items.sort(reverse=True, key=lambda x: x[0])
    
    valor_total = 0.0
    
    for ratio, valor, peso in items:
        if W == 0:
            break
        
        if peso <= W:
            valor_total += valor
            W -= peso
        else:
            fraccion = W / peso
            valor_total += valor * fraccion
            W = 0
    
    return valor_total


# Ejemplo
valores = [60, 100, 120]
pesos = [10, 20, 30]
W = 50

print("Valor máximo:", ejercicio2(W, valores, pesos))