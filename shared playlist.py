import os
from time import sleep

playlist = {}
usuarios = []
usuario_atual = []

print(
    "----PlayList----"
    )

usuario = str(input(
    "Digite o nome do seu usuario: "
    )).strip().capitalize()
os.system("Cls")

usuarios.append(usuario)
usuario_atual.append(usuario)

musicas_por_usuario = {}

while True:
    selecao = int(input(
        f"1 - Adicionar Música\n2 - Ver PlayList\n3 - Tirar Música\n4 - Trocar Usuário\n5 - Adicionar Usuário\n6 - Sair\nUsuário atual: {usuario_atual[-1]}\nDigite: "
        ))
    os.system("Cls")

    if selecao == 4:
        print(
            "Usuários cadastrados:"
            )
        for nomes in usuarios:
            print(nomes)
        trocar_usuario = str(input(
            "Digite qual usuário deseja entrar: "
            )).strip().capitalize()
        os.system("Cls")

        if trocar_usuario not in usuarios:
            os.system("Cls")
            print(
                "Esse usuário não está cadastrado."
                )
            sleep(3)
            os.system("Cls")

        else:
            usuario_atual[0] = trocar_usuario
            os.system("Cls")
            continue

    if selecao == 5:
        os.system("Cls")
        adicionar_usuarios = str(input(
            "Digite o nome do usuário que deseja inserir: "
            )).strip().capitalize()
        os.system("Cls")

        if adicionar_usuarios not in usuarios:
            usuarios.append(adicionar_usuarios)
            print(
                f"{adicionar_usuarios} foi adicionado na lista."
                )
            os.system("Cls")

        else:
            print(
                f"Usuário {adicionar_usuarios} já está na lista."
                )
            sleep(3)
            os.system("Cls")


    if selecao == 1:
        musica = str(input(
            "Digite uma música: "
            )).capitalize().strip()
        os.system("Cls")

        # Verificar se a música já foi adicionada por outro usuário
        if musica in playlist:
            musicaigual = playlist.get(musica)
            playlist.pop(musicaigual)
            playlist.append(musica)
            print(
                "Você colocou uma música igual, e já removemos ela da playlist."
                )
            sleep(3)
            os.system("Cls")

        else:
            # Adiciona a música ao dicionário de playlist do usuário atual
            if usuario_atual[0] not in musicas_por_usuario:
                musicas_por_usuario[usuario_atual[0]] = []

            musicas_por_usuario[usuario_atual[0]].append(musica)
            playlist[musica] = usuario_atual[0]  # A música é associada ao usuário que a adicionou
            print(
                "Música adicionada à sua playlist!"
                )

    elif selecao == 3:
        os.system("Cls")
        musica_retirar = str(input(
            "Digite o nome da música para retirar: "
            )).capitalize().strip()
        os.system("Cls")

        if musica_retirar in playlist:
            usuario_que_adicionou = playlist[musica_retirar]
            musicas_por_usuario[usuario_que_adicionou].remove(musica_retirar)
            del playlist[musica_retirar]
            print(
                "Música retirada com sucesso!"
                )
        else:
            print(
                "Música não encontrada na playlist."
                )

    if selecao == 2:
        if not playlist:
            print("A playlist está vazia.")
        else:
            print("PlayList:")
            for musica, usuario in playlist.items():
                print(f"{musica} - Adicionada por: {usuario}")

    if selecao == 6:
        print(
            "Saindo..."
            )
        break
