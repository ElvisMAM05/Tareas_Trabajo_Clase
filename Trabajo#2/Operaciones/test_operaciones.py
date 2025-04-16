from Operaciones.operaciones import suma,resta,div,mult

def test_suma():
    assert suma(4,3)==7

def test_resta():
    assert resta(4,3)==1

def test_div():
    assert div(4,3)==1.3333333333333333

def test_mult():
    assert mult(4,3)==12