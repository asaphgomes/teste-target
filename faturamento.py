import json
with open("faturamento.json", "r") as file:
    dados = json.load(file)

faturamentos = []

for dia in dados:
    if dia["valor"] > 0:
        faturamentos.append(dia["valor"])

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = 0
for faturamento in faturamentos:
    if faturamento > media_mensal:
        dias_acima_da_media += 1

print("Menor faturamento:", menor_faturamento)
print("Maior faturamento:", maior_faturamento)
print("Dias com faturamento acima da média:", dias_acima_da_media)