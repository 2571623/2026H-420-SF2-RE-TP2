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
        for i, a in enumerate(self.coefficients):
            if i == 0:
                self.coefficients[i] = 0
            else:
                self.coefficients[i] = a * i
        return Polynome(self.coefficients)
    
    def __str__(self) -> str:
        fct_deriver = []
        for i, a in enumerate(self.coefficients):
            if a != 0:
                if i == 0:
                    fct_deriver.append(f" + {a}")
                elif i == 1:
                    fct_deriver.append(f" + {a}x")
                else:
                    fct_deriver.append(f" + {a}x^{i}")
        return fct_deriver[-1:]