from unittest.mock import Mock

import pytest

from zourmat_libpythonpro import github_api


@pytest.fixture()
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/103135243?v=4'
    resp_mock.json.return_value = {
        "login": "zourmat",
        "id": 103135243,
        "node_id": "U_kgDOBiW4Cw",
        "avatar_url": url
    }
    get_mock = mocker.patch('zourmat_libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('zourmat')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('zourmat')
    assert 'https://avatars.githubusercontent.com/u/103135243?v=4' == url
