# autor: Michel
# data: 06/05/2026

# possivel sólução para o exercício 7, utilizando as regras de controle de fluxo (if, elif, else), loops (for), e f-strings para formatação de saída.


cargas = [15, 80, -5, 120, 550, 30, 10]

for indice, peso in enumerate(cargas):
    # Regra 3: Alerta de Excesso (Break)
    if peso > 500:
        print(f"ALERTA: Carga com excesso de peso detectada no ID {indice}. Interrompendo sistema...")
        break
    
    # Regra 2: Cargas Inválidas (Continue)
    if peso < 0:
        continue
    
    # Regra 4: Classificação
    if peso < 20:
        categoria = "Leve"
    elif peso <= 100:
        categoria = "Padrão"
    else:
        categoria = "Pesada"
    
    # Regra 5: Relatório com f-string
    print(f"Carga {indice}: {peso}kg - Classificação: {categoria}")
