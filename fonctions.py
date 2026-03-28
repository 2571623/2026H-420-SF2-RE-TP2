from expression import Expression


class Sin(Expression):
    """Expression representant sin(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return Cos(self.u.evaluer(x)) * self.u.evaluer(x)
    
    def deriver(self) -> Expression:
        return Sin(Cos(self.u.deriver(), self.u.deriver()))


class Cos(Expression):
    """Expression representant cos(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    pass


class Exp(Expression):
    """Expression representant exp(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    pass
