def copy_file(command: str) -> None:
    partes = command.split()
    arquivo_origem = partes[1]
    arquivo_destino = partes[2]

    if arquivo_origem == arquivo_destino:
        return

    with open(arquivo_origem, "r") as f1, open(arquivo_destino, "w") as f2:
        conteudo = f1.read()
        f2.write(conteudo)
