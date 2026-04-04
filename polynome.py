from expression import Expression

class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    def __init__(self, coefficients):
        self.coefficients = list(coefficients)

    def evaluer(self, x: float) -> float:
        self.x = x
        resultat = 0
        for i, a in enumerate(self.coefficients):
            resultat += a * ( x**i)
        return resultat

    def deriver(self) -> "Expression":
        fct_deriver = []
        for i, a in enumerate(self.coefficients):
            if i == 0:
                continue
            else:
                fct_deriver.append(a * i)
        return Polynome(fct_deriver)
    
    def __str__(self) -> str:
        termes = []
        for i, a in enumerate(self.coefficients):
            if a != 0:
                if i == 0:
                    termes.append(f"{a}")
                elif i == 1:
                    termes.append(f"{a}x")
                else:
                    termes.append(f"{a}x^{i}")
        return " + ".join(termes).replace("+ -", "- ")
