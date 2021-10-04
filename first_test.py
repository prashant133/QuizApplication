import pytest

@pytest.mark.parametrize("email,password",[("dsrprasant@gmail.com,123"),("xyq@gmail.com,qwe")])
def test_method(email,password):
    assert email == "dsrprasant@gmail.com"