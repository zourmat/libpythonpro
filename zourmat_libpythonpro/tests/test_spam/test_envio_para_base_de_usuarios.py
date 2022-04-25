from unittest.mock import Mock

import pytest

from zourmat_libpythonpro.spam.main import EnviadorDeSpam
from zourmat_libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='zourmat', email='matheusmpz@hotmail.com'),
            Usuario(nome='renzo', email='matheusmpz@hotmail.com')
        ],
        [
            Usuario(nome='zourmat', email='matheusmpz@hotmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'matheusmpz@hotmail.com',
        'Spam enviado',
        'Conferindo o spam'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='zourmat', email='matheusmpz@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@hotmail.com',
        'Spam enviado',
        'Conferindo o spam'
    )
    assert enviador.enviar.assert_called_once_with(
        'renzo@hotmail.com',
        'matheusmpz@hotmail.com',
        'Spam enviado',
        'Conferindo o spam'
    )
