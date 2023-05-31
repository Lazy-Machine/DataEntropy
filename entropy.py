import math

entropy = 0.0
total = 0
classes = []
n = int(input('Quantidade de classes: '))

for i in range(n):
  classes.append(int(input(f"Valor da classe {i+1}: ")))
  total += classes[i]

for i in range(n):
  probability = classes[i] / total
  entropy -= probability * math.log2(probability)

maxEntropy = math.log2(n)

print(f'Valor Total: {total}')
print(f'Entropia dos dados: {entropy:.3f}')
print(f'Entropia máxima: {maxEntropy:.3f}')