dias_semana = ["segunda-feira", "terça-feira","quarta-feira", "quinta-feira", "sexta-feira"]
votos = {dia: 0 for dia in dias_semana}

num_colaboradores = int(input("Informe o número de colaboradores que irão votar: "))
for i in range(num_colaboradores):
    print(f"\nColaborador {i+1}:") 
    while True:
        voto = input(f"Escolha um dia da semana ({', '.join(dias_semana)}): ").strip().lower()
        if voto in dias_semana:
            votos[voto] += 1
            break
        else:
            print("Dia inválido. Tente novamente.")

    max_votos = max(votos.values())
    dias_vencedores = [dia for dia,count in votos.items() if count == max_votos]
    print("\nResultado da votação:")
    
    for dia, count in votos.items():
        print(f"{dia.capitalize()}: {count} voto(s)")
    if len(dias_vencedores) > 1:
        print(f"\nHouve um empate entre os dias: {', '.join(dias_vencedores)}")
    else:
        print(f"\nO dia escolhido foi: {dias_vencedores[0].capitalize()}")
