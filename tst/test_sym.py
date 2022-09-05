from src.sym import Sym
from src.main import oo

def test_sym():
    
    sym = Sym()
    for i, x in ["a", "a", "a", "a" , "b", "b", "c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy)//1/1000
    oo({"mid":mode, "div":entropy})
    return mode == "a" and 1.37 <= entropy and entropy <= 1.38

