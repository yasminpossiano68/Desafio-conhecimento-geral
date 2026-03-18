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