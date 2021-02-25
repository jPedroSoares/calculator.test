from behave import when, then
from calc import sub


@when('subtrair {valor_um} de {valor_dois}')
def test_soma(context, valor_um, valor_dois):
    """
    Teste de subtracao simples
    Args:
        valor_um: float
        valor_dois: float
    
    Chamada à função sub() passando os parâmetros valor_um e valor_dois
    Função sem retorno
    """
    context.result = sub(valor_um, valor_dois)

@then('o resultado da subtracao deve ser {resultado}')
def test_soma_result(context, resultado):
    """
    Validação de resposta da função soma simples
    Args:
        resultado: float
    """
    assert context.result == float(resultado)

@then('deverá aparecer da subtracao "{message}"')
def test_soma_fail(context, message):
    """
    """
    assert message == context.result