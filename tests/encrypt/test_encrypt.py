from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(
        TypeError, match="tipo inválido para message"
    ):
        encrypt_message(1, 2)

    with pytest.raises(
        TypeError, match="tipo inválido para key"
    ):
        encrypt_message("teste", "x")

    assert encrypt_message("teste", 8) == "etset"

    assert encrypt_message("teste", 2) == "ets_et"

    assert encrypt_message("teste", 3) == "set_et"
