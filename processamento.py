def validar_notas(notas):
    if not notas or not isinstance(notas, list):
        return False

    for nota in notas:
        if not isinstance(nota, (int, float)):
            return False

    return True


def calcular_media(notas):
    return sum(notas) / len(notas)


def alunos_recuperacao(alunos):
    recuperacao = []

    for nome, notas in alunos:
        if validar_notas(notas):
            media = calcular_media(notas)
            if media < 7:
                recuperacao.append((nome, media))

    return recuperacao

def top_student(alunos):
    melhor = None
    maior_media = 0

    for nome, notas in alunos:
        if validar_notas(notas):
            media = calcular_media(notas)
            if media > maior_media:
                maior_media = media
                melhor = (nome, media)

    return melhor


def gerar_relatorio(alunos, recuperacao, top):
    with open("resultado.txt", "w") as arquivo:
        arquivo.write("RELATÓRIO DE DESEMPENHO\n\n")

        arquivo.write("Todos os alunos:\n")
        for nome, notas in alunos:
            if validar_notas(notas):
                media = calcular_media(notas)
                arquivo.write(f"{nome} - Média: {media:.2f}\n")

        arquivo.write("\nAlunos em Recuperação:\n")
        for nome, media in recuperacao:
            arquivo.write(f"{nome} - Média: {media:.2f}\n")

        arquivo.write("\nTop Student:\n")
        if top:
            arquivo.write(f"{top[0]} - Média: {top[1]:.2f}\n")