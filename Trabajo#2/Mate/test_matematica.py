from matematica import esprimo

def test_esprimo():
    assert esprimo(3)==True
    assert esprimo(9)==False
    assert esprimo(11)==True
    