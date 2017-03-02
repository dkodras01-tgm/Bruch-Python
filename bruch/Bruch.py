from __future__ import division, print_function, unicode_literals

class Bruch(object):
    """
    Eine Klasse, die Brueche verwaltet (addieren, subtrahieren, multiplizieren, dividieren)

    :param int numerator: Zaehler
    :param int denominator: Nenner
    :ivar int numerator: Zaehler
    :ivar int denominator: Nenner
    """
    def __iter__(self):
        """
        Klasse iterierbar machen
        """
        return (self.zaehler,self.nenner).__iter__()
    def __init__(self, zaehler=0,nenner=1):
        """
        Konstruktor; initialisiert die Werte von Zaehler und Nenner

        :param numerator: int oder Bruch
        :param denominator: int
        :raise TypeError: falscher Wert
        """
        if isinstance(zaehler, Bruch):
            self.zaehler,self.nenner=zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('incompatible type:'+type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('incompatible type:'+type(nenner).__name__) 
        if nenner==0:
            raise ZeroDivisionError
        self.zaehler=zaehler
        self.nenner=nenner

    def __float__(self):
        """
        ueberschreibt float()

        :return: float
        """
        return self.zaehler/self.nenner

    def __int__(self):
        """
        ueberschreibt int()

        :return: int
        """
        return int(self.__float__())    

    def __neg__(self):
        """
        Negieren

        :return: Bruch
        """
        return Bruch(-self.zaehler,self.nenner)

    def __radd__(self,zaehler):
        """
        richtige Version von add

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler)

    def __add__(self,zaehler):
        """
        addieren

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2,n2=zaehler
        elif type(zaehler) is int:
            z2,n2=zaehler,1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' + Bruch()')        
        nennerNeu=self.nenner*n2
        zaehlerNeu=z2*self.nenner+n2*self.zaehler
        return Bruch(zaehlerNeu,nennerNeu)

    def __complex__(self):
        """
        ueberschreibt complex()

        :return: complex
        """
        return complex(self.__float__())

    def __rsub__(self,left):
        """
        richtige Version von subtrahieren

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2=left        
            nennerNeu=self.nenner
            zaehlerNeu=z2*self.nenner-self.zaehler
            return Bruch(zaehlerNeu,nennerNeu)
        else:
            raise TypeError('incompatible types:'+type(left).__name__+' - Bruch()')
            

    def __sub__(self,zaehler):
        """
        subtrahieren

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler*-1)

    def __rmul__(self,zaehler):
        """
        richtige Version von Multiplizieren

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__mul__(zaehler)

    def __mul__(self,zaehler):
        """
        multiplizieren

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2,n2=zaehler
        elif type(zaehler) is int:
            z2,n2=zaehler,1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' * Bruch()')
        z2*=self.zaehler
        n2*=self.nenner
        return Bruch(z2,n2)

    def __pow__(self,p):
        """
        Ein Bruch, der im Exponenten wieder den selben Bruch hat

        :raise TypeError: incompatible types
        :param int p: power
        :return: Bruch
        """
        if type(p) is int:
            return Bruch(self.zaehler**p,self.nenner**p)
        else:
            raise TypeError('incompatible types:'+type(p).__name__+' should be an int')
             

    def __rdiv__(self, other):
        """
        division

        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__rtruediv__(other)

    def __rtruediv__(self,left):
        """
        richtige Version von dividieren

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2=left*self.nenner
            if self.zaehler==0:
                raise ZeroDivisionError
            return Bruch(z2,self.zaehler)        
        else:
            raise TypeError('incompatible types:'+type(left).__name__+' / Bruch()')
        

    def __div__(self, other):
        """
        division 2.0

        :param other: int or Bruch
        :return: Bruch
        """
        return self.__truediv__(other)
    def __truediv__(self,zaehler):
        """
        division 3.0

        :raise TypeError: incompatible types
        :param zaehler: Bruch or int
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2,n2=zaehler
        elif type(zaehler) is int:
            z2,n2=zaehler,1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' / Bruch()')
        if z2==0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2,z2))    

    def __invert__(self):
        """
        Bruch invertieren

        :return: Bruch
        """
        return Bruch(self.nenner,self.zaehler)
        

    def __repr__(self):
        """
        representation vom Bruch object

        :return str: the representation
        """
        # Vor der Ausgabe wird gekuerzt!
        shorten=Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler//=shorten
        self.nenner//=shorten
        # Nenner stehts positiv
        if self.nenner<0:
            self.nenner*=-1
            self.zaehler*=-1
            
        if self.nenner==1:
            return "(%d)" % self.zaehler
            #return "({:d})".format(self.zaehler)
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __makeBruch(other):
        """
        Bruch erstellen

        :raise TypeError: incompatible types
        :param other: Bruch or int
        :return: Bruch
        """
        '''create a Bruch from int or return the reference'''
        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b=Bruch(other,1)
            return b
        else:
            raise TypeError('incompatible types:'+type(other).__name__+' not an int nor a Bruch')

    def __eq__ (self, other):
        """
        equal

        :param Bruch other: other Bruch
        :return: boolean
        """
        other=Bruch.__makeBruch(other)
        return self.zaehler*other.nenner == other.zaehler*self.nenner

    def __ne__ (self, other):
        """
        not equal

        :param Bruch other: other Bruch
        :return: boolean
        """
        return not self.__eq__(other)

    def __gt__ (self, other):
        """
        groesser als

        :param Bruch other: other Bruch
        :return: boolean
        """
        other=Bruch.__makeBruch(other)
        return self.zaehler*other.nenner > other.zaehler*self.nenner

    def __lt__ (self, other):
        """
        kleiner als

        :param Bruch other: other Bruch
        :return: boolean
        """
        other=Bruch.__makeBruch(other)
        return self.zaehler*other.nenner < other.zaehler*self.nenner

    def __ge__ (self, other):
        """
        groesser gleich

        :param Bruch other: other Bruch
        :return: boolean
        """
        other=Bruch.__makeBruch(other)
        return self.zaehler*other.nenner >= other.zaehler*self.nenner

    def __le__ (self, other):
        """
        kleiner gleich

        :param Bruch other: other Bruch
        :return: boolean
        """
        other=Bruch.__makeBruch(other)
        return self.zaehler*other.nenner <= other.zaehler*self.nenner

    def __abs__(self):
        """
        abs(Bruch)

        :return: positive Bruch
        """
        return Bruch(abs(self.zaehler),abs(self.nenner))

    def __iadd__(self,other):
        """
        intern addieren

        :param Bruch other: Bruch
        :return: self
        """
        other=Bruch.__makeBruch(other)
        self=self+other
        return self

    def __isub__(self,other):
        """
        intern subtrahieren

        :param Bruch other: Bruch
        :return: self
        """
        other=Bruch.__makeBruch(other)
        self=self-other
        return self

    def __imul__(self,other):
        """
        intern multiplizieren

        :param Bruch other: other Bruch
        :return: self
        """
        other=Bruch.__makeBruch(other)
        self=self*other
        return self

    def __idiv__(self, other):
        """
        intern division 2

        :param Bruch other: other Bruch
        :return: self
        """
        return self.__itruediv__(other)

    def __itruediv__(self,other):
        """
        intern division 3

        :param Bruch other: other Bruch
        :return: self
        """
        other=Bruch.__makeBruch(other)
        self=self/other
        return self

    @classmethod
    def gcd(cls,x,y):
        """
        euclid's algorithm
        :param int x: first value
        :param int y: second value
        :return: greatest common divisor
        """
        x,y=abs(x),abs(y) # positive Werte!!
        if x<y: x,y=y,x
        #Berechnung 
        while y != 0:
            x,y = y,x%y
        return x