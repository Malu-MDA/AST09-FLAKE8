
def realizar_login(usuario, senha, forcar_erro):
    if not usuario or senha is None or forcar_erro:
        print("Falha no login")
        return False

    print(
        "Iniciando o processo de login no sistema com "
        "credenciais validas e aguardando o tempo de "
        "resposta do servidor..."
    )
    return True


def test_verificar_login_valido():
    token_sessao = "abc123xyz"  # noqa: F841
    assert realizar_login(True, "123456", False)
