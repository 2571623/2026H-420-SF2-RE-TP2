from expression import Expression
from operations import Multiplication
from polynome import Polynome
import math

class Sin(Expression):
    """Expression representant sin(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return math.sin(self.u.evaluer(x))
    
    def deriver(self) -> Expression:
        return Multiplication(Cos(self.u.deriver()), self.u.deriver())
    
    def __str__(self):
        return f"sin({self.u})"

class Cos(Expression):
    """Expression representant cos(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return math.cos(self.u.evaluer(x))
    
    def deriver(self) -> Expression:
        return Multiplication(Multiplication(Polynome([-1]),Sin(self.u.deriver())), self.u.deriver())

    def __str__(self):
        return f"cos({self.u})"

class Exp(Expression):
    """Expression representant exp(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return math.exp(self.u.evaluer(x))
    
    def deriver(self) -> Expression:
        return Multiplication(Exp(self.u.deriver()), self.u.deriver())
    
    def __str__(self):
        return f"exp({self.u})"
