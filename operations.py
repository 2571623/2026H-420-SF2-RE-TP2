from expression import Expression


class Addition(Expression):
    """Expression representant u + v."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u: Expression, v: Expression):
        self.u = u
        self.v = v

    def evaluer(self, x: float) -> float:
        return self.u.evaluer(x) + self.v.evaluer(x)
    
    def deriver(self) -> "Expression":
        return Addition(self.u.deriver(), self.v.deriver())
    
    def __str__(self) -> str:
        return f"({self.u} + {self.v})"


class Multiplication(Expression):
    """Expression representant u * v."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u: Expression, v: Expression):
        self.u = u
        self.v = v
    
    def evaluer(self, x: float) -> float:
        return self.u.evaluer(x) * self.v.evaluer(x)
    
    def deriver(self) -> "Expression":
        return Multiplication(self.u.deriver(), self.v.deriver())

    def __str__(self) -> str:
        return f"({self.u} * {self.v})"