from processamento import validar_notas, calcular_media

alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):

    nome = input("Digite o nome do aluno: ")

    qtd_notas = int(input("Quantas notas esse aluno tem? "))

    notas = []

    for i in range(qtd_notas):

        nota = float(input("Digite a nota: "))
        notas.append(nota)

    alunos.append((nome, notas))

top_aluno = ""
maior_media = 0

arquivo = open("resultado.txt", "w")

arquivo.write("RELATORIO DE NOTAS\n\n")

for aluno in alunos:

    nome = aluno[0]
    notas = aluno[1]

    if validar_notas(notas) == False:
        print(nome, "nao possui notas validas")
        arquivo.write(nome + " - sem notas validas\n")
        continue

    media = calcular_media(notas)

    situacao = "Aprovado"

    if media < 7:
        situacao = "Recuperacao"

    print(nome, "media:", media)

    arquivo.write(nome + " - media: " + str(media) + " - " + situacao + "\n")

    if media > maior_media:
        maior_media = media
        top_aluno = nome


arquivo.write("\nTop Student: " + top_aluno)

arquivo.close()