from src.sym import Sym


class TestSym:
    """
    Test class for Sym
    """

    def sym(self, misc, eg, runs, fails):
        """
        Test for Sym class
        """
        sym = Sym()
        for x in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(x)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000
        misc.oo({"mid": mode, "div": entropy})
        return mode == "a" and 1.37 <= entropy and entropy <= 1.38
