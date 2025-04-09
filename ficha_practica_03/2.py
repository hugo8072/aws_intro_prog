controlo = 0  # Inicializa o controle

# Dicionário de opções
opcoes = {
    1: 'criar',
    2: 'actualizar',
    3: 'eliminar',
    4: 'sair'
}

# Solicita a escolha inicial
print("Escolha uma opcao:")
print(opcoes)
controlo = int(input("Escolha a opção (1-4): "))

# Loop que continua até que o usuário escolha a opção 4 (sair)
while controlo != 4:
    if controlo in opcoes:
        print(f"Você escolheu a opção: {opcoes[controlo]}")
    else:
        print("Opção inválida!")

    # Solicita novamente a opção
    controlo = int(input("Escolha a opção (1-4): "))

print("Saindo do programa.")