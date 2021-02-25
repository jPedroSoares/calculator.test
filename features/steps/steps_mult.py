from behave import when, then
from calc import mult


@when('multiplicar {valor_um} de {valor_dois}')
def test_soma(context, valor_um, valor_dois):
    """
    Teste de multiplicação simples
    Args:
        valor_um: float
        valor_dois: float
    
    Chamada à função mult() passando os parâmetros valor_um e valor_dois
    Função sem retorno
    """
    context.result = mult(valor_um, valor_dois)

@then('o resultado da multiplicacao deve ser {resultado}')
def test_soma_result(context, resultado):
    """
    Validação de resposta da função multiplicação simples
    Args:
        resultado: float
    """
    assert context.result == float(resultado)

@then('deverá aparecer da multiplicacao "{message}"')
def test_soma_fail(context, message):
    """
    """
    assert message == context.result