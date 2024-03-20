def fibonacci(n):
  """
  Função que gera a sequência de Fibonacci até o n-ésimo termo.

  Args:
      n (int): Número de termos da sequência a serem gerados.

  Returns:
      list: Lista com os termos da sequência de Fibonacci.
  """
  if n == 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    fib_seq = [0, 1]
    for i in range(2, n):
      fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq

def main():
  """
  Função principal que verifica se um número pertence à sequência de Fibonacci.
  """
  # Número a ser verificado
  numero = int(input("Digite um número: "))

  # Gera a sequência de Fibonacci até o número informado
  fib_seq = fibonacci(numero + 1)

  # Verifica se o número pertence à sequência
  if numero in fib_seq:
    print(f"O número {numero} pertence à sequência de Fibonacci!")
  else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
  main()
