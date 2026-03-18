#Inicializando o Projeto
def validar_notas(notas):
    if not notas or not isinstance(notas, list):
        return False

    for nota in notas:
        if not isinstance(nota, (int, float)):
            return False

    return True
