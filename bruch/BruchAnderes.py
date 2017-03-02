class Bruch(object):
    """
    Eine Klasse, die Brueche verwaltet (addieren, subtrahieren, multiplizieren, dividieren)

    :param int numerator: Zaehler
    :param int denominator: Nenner
    :ivar int numerator: Zaehler
    :ivar int denominator: Nenner
    """
    numerator = 1
    denominator = 1

    def __init__(self, numerator, denominator=1):
        """
        Konstruktor; initialisiert die Werte von Zaehler und Nenner

        :param numerator: int oder Bruch
        :param denominator: int
        :raise TypeError: falscher Wert
        """
        if type(numerator) is int and type(denominator) is int:
            if denominator != 0:
                self.numerator = numerator
                self.denominator = denominator
            else:
                raise ZeroDivisionError("Nenner darf nicht 0 sein!")
        elif type(numerator) is Bruch:
            self.numerator = numerator.numerator
            self.denominator = numerator.denominator
        else:
            raise TypeError("Eingegebener Wert ist keine gueltige Zahl")

    def __add__(self, other):
        """
        Addieren

        :param other: int oder Bruch
        :return: Bruch
        :raise TypeError: falscher Wert
        """
        if type(other) is int or type(other) is Bruch:
            return float(self) + other
        else:
            raise TypeError("Eingegebener Wert ist keine gueltige Zahl")

    def __iadd__(self, other):
        """
        Addieren

        :param other: int oder Bruch
        :return: Bruch
        :raise TypeError: falscher Wert
        """
        if type(other) is int or type(other) is Bruch:
            return self + other
        else:
            raise TypeError("Eingegebener Wert ist keine gueltige Zahl")

    def __radd__(self, other):
        """
        Richtiges addieren

        :param other: int oder Bruch
        :return: Bruch
        """
        if type(other) is int or type(other) is Bruch:
            return self.__add__(other)
        else:
            raise TypeError("Eingegebener Wert ist keine gueltige Zahl")

    def __sub__(self, other):
        """
        Subtrahieren

        :param other: int oder Bruch
        :return: Bruch
        :raise TypeError: falscher Wert
        """
        if type(other) is int:
            return Bruch(self.numerator - other, self.denominator)
        elif type(other) is Bruch:
            return Bruch(self.numerator - other.numerator, self.denominator)
        else:
            raise TypeError("Eingegebener Wert ist keine gueltige Zahl")

    def __isub__(self, other):
        """
        Subtrahieren

        :param other: Bruch
        :return: Bruch
        """
        return self - Bruch(other)

    def __rsub__(self, other):
        """
        Subtrahieren

        :param other: int
        :return: Bruch
        """
        if type(other) is int:
            return Bruch(self.numerator, other * self.numerator - self.denominator)

    def __mul__(self, other):
        """
        Multiplizieren

        :param other: int oder Bruch
        :return: Bruch
        :raise TypeError: falscher Wert
        """
        if type(other) is int:
            return Bruch(self.numerator * other, self.denominator)
        elif type(other) is Bruch:
            return Bruch(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            raise TypeError("Eingegebener Wert ist keine gueltige Zahl")

    def __imul__(self, other):
        """
        Multiplizieren

        :param other: int oder Bruch
        :return: Bruch
        :raise TypeError: falscher Wert
        """
        if type(other) is int:
            return self * other
        elif type(other) is Bruch:
            return self * other
        else:
            raise TypeError("Eingegebener Wert ist keine gueltige Zahl")

    def __rmul__(self, other):
        """
        Richtiges Multiplizieren

        :param other: int oder Vruch
        :return: Bruch
        """
        return self.__mul__(other)

    def __pow__(self, power, modulo=None):
        """
        Exponentialrechnung

        :param power: int
        :param modulo:
        :return:  Bruch
        :raise TypeError: falscher Wert
        """
        if type(power) is int:
            return Bruch(self.numerator ** power, self.denominator ** power)
        else:
            raise TypeError("Eingegebener Wert ist keine gueltige Zahl")

    def __str__(self):
        """
        Textuelle Bruch-Ausgabe

        :return: String
        """
        return "(" + self.numerator + "/" + self.denominator + ")"

    def __eq__(self, other):
        """
        Gleich wie

        :param other: int oder Bruch
        :return: boolean
        """
        if type(other) is int:
            if self.numerator == other:
                return True
            else:
                return False
        elif type(other) is Bruch:
            if self.numerator == other.numerator and self.denominator == other.denominator:
                return True
            else:
                return True

    def __ne__(self, other):
        """
        Nicht gleich wie

        :param other: Bruch
        :return: boolean
        """
        return not self.__eq__(other)

    def __iter__(self):
        """
        Iterable

        :return:
        """
        return(self.numerator, self.denominator).__iter__()

    def __int__(self):
        """
        Ueberschreibt int

        :return: int
        """
        return int(self.__float__())

    def __neg__(self):
        """
        Negiert den Bruch

        :return: Bruch
        """
        return Bruch(-self.numerator, self.denominator)



    def printbruch(self):
        """
        Gibt den Bruch Textuell aus
        """
        print(self.numerator + "/" + self.denominator)

    def float(self):
        """
        Ueberschreibt float()

        :return: float
        """
        return float(self.numerator / self.denominator)

    def getnumerator(self):
        return self.numerator

    def getdenominator(self):
        return self.denominator
