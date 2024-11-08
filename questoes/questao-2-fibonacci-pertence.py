n = int(input("Digite um número: "))

fibonacci = [0,1]
i=1

while fibonacci[-1] < n:
  fibonacci.append(fibonacci[-1] + fibonacci[-2])
  i+=1

if n in fibonacci:
  print("Este número pertence a sequencia fibonacci")
else:
  print("Este número não pertence a sequencia fibonacci")
