from behave import when, then
from calc import div


@when('dividir {valor_um} por {valor_dois}')
def test_divisao(context, valor_um, valor_dois):
    """
    Teste de subtracao simples
    Args:
        valor_um: float
        valor_dois: float
    
    Chamada à função div() passando os parâmetros valor_um e valor_dois
    Função sem retorno
    """
    context.result = div(valor_um, valor_dois)

@then('o resultado da divisao deve ser {resultado}')
def test_soma_result(context, resultado):
    """
    Validação de resposta da função divisao simples
    Args:
        resultado: float
    """
    assert context.result == float(resultado)

@then('deverá aparecer da divisao "{message}"')
def test_soma_fail(context, message):
    """
    """
    assert message == context.result