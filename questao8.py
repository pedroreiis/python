def verificar_nota():
    gabarito = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'E',
        7: 'D',
        8: 'C',
        9: 'B',
        10: 'A'
    }
    total_alunos = 0
    total_acertos = []
    while True:
        total_acertos_aluno = 0
        print("\nResponda as questões da prova (A, B, C, D, E):")
        for i in range(1, 11):
            resposta = input(f"Questão {i}: ").strip().upper()
            if resposta == gabarito[i]:
                total_acertos_aluno += 1
        total_acertos.append(total_acertos_aluno)
        total_alunos += 1
        continuar = input("Outro aluno vai utilizar o sistema? (s/n): ").strip().lower()
        if continuar != 's':
            break
    maior_acerto = max(total_acertos)
    menor_acerto = min(total_acertos)
    media_notas = sum(total_acertos) / total_alunos if total_alunos > 0 else 0
    print(f"\nTotal de Alunos: {total_alunos}")
    print(f"Maior Acerto: {maior_acerto}")
    print(f"Menor Acerto: {menor_acerto}")
    print(f"Média das Notas: {media_notas:.2f}")
verificar_nota()
