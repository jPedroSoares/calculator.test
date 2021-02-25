from behave import when, then
from calc import soma


@when('somar {valor_um} com {valor_dois}')
def test_soma(context, valor_um, valor_dois):
    """
    Teste de soma simples
    Args:
        valor_um: float
        valor_dois: float
    
    Chamada à função soma() passando os parâmetros valor_um e valor_dois
    Função sem retorno
    """
    context.result = soma(valor_um, valor_dois)

@then('o resultado deve ser {resultado}')
def test_soma_result(context, resultado):
    """
    Validação de resposta da função soma simples
    Args:
        resultado: float
    """
    assert context.result == float(resultado)

@then('deverá aparecer "{message}"')
def test_soma_fail(context, message):
    """
    """
    assert message == context.result