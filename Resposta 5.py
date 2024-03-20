def inverter_string(string):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""
    
    # Loop através da string de trás para frente
    for i in range(len(string) - 1, -1, -1):
        # Concatena cada caractere à string invertida
        string_invertida += string[i]
    
    # Retorna a string invertida
    return string_invertida

# Exemplo de uso
string_original = "Olá, mundo!"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
