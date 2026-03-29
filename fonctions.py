from expression import Expression
from operations import Multiplication
import math

class Sin(Expression):
    """Expression representant sin(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return math.cos(self.u.evaluer(x)) * self.u.evaluer(x)
    
    def deriver(self) -> Expression:
        return Sin(Multiplication(math.cos(self.u.deriver(), self.u.deriver())))
    
    def __str__(self):
        return Expression

#Question Prof est ce que possible de faire cos et sin sans math ?

class Cos(Expression):
    """Expression representant cos(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return -math.sin(self.u.evaluer(x)) * self.u.evaluer(x)
    
    def deriver(self) -> Expression:
        return Cos(Multiplication(-math.sin(self.u.deriver(), self.u.deriver())))

    def __str__(self):
        return Expression
# Question Prof comment faire négatif dans le cos et le sin ?

class Exp(Expression):
    """Expression representant exp(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return math.exp(self.u.evaluer(x)) * self.u.evaluer(x)
    
    def deriver(self) -> Expression:
        return Exp(Multiplication(math.exp(self.u.deriver(), self.u.deriver)))
    
    def __str__(self):
        return Expression
