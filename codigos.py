#resolução em python
# 1)
INDICE = 13
SOMA = 0 
K = 0
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print(SOMA)

# 2)
def pertence_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Informe um número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

# 3)
import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

faturamento = dados['faturamento_diario']

faturamento_filtrado = [dia for dia in faturamento if dia != 0]

menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)
media_faturamento = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_media = len([dia for dia in faturamento_filtrado if dia > media_faturamento])

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias acima da média: {dias_acima_media}")

# 4)
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")

# 5)
def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")
