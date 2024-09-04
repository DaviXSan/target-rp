# Definir a string para verificar
texto = input("Digite uma string: ")
contagem_a = 0

# Contar a ocorrência da letra 'a' (maiúscula ou minúscula)
for caractere in texto:
    if caractere.lower() == 'a':
        contagem_a += 1

# Exibir o resultado
if contagem_a > 0:
    print(f"A letra 'a' (maiúscula ou minúscula) aparece {contagem_a} vezes.")
else:
    print("A letra 'a' (maiúscula ou minúscula) não aparece na string.")
