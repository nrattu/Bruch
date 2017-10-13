from pip.cmdoptions import no_binary


class Bruch(object):
    """
    Diese Klasse erstellt Brücke zweier Zahlen
    Man kann damit alle mathemathische Operator durchführen
    Mit hilfe der Klasse kann man zwei Brüche addieren, subtrahieren, multiplizieren, dividieren.
    """
    def __init__(self, *args):
        if len(args) is 1:
            args0 = args[0]
            if isinstance(args0, Bruch):
                self.numerator = args0.numerator
                self.denominator = args0.denominator
            elif isinstance(args0, int):
                self.numerator = args0
                self.denominator = 1
            else:
                raise TypeError()
        elif len(args) is 2:
            self.numerator = args[0]
            self.denominator = args[1]

        if self.denominator is 0:
            raise ZeroDivisionError()
        elif isinstance(self.denominator, float) or isinstance(self.numerator, float):
            raise TypeError()

    def __int__(self):
        """
        Der Bruch wird in Int umgewandelt
        :return: der umgewandelte Bruch wird zurückgegeben
        """
        return int(self.numerator / self.denominator)

    def __float__(self):
       """
       Der Bruch wird in Float umgewandelt
       :return: der umgewandelte Bruch wird zurückgegeben
       """
       return float(self.numerator/self.denominator)

    def __invert__(self):
        """
        Der Nenner und der Zahler eines Bruches werden vertauscht
        :return: der Bruch wird zurückgegeben
        """
        return Bruch(self.denominator, self.numerator)

    def __pow__(self, power, modulo=None):
        """
        Diese Funktion potenziert einen Bruch.
        :param power: die Hoch zahl
        :param modulo:
        :return: der potenzierter Bruch mit der Hochzahl power wird zurückgegeben
        """
        return Bruch(self.numerator ** power, self.denominator ** power)

    def __eq__(self, other):
        """
        Self Bruch wird ist gleich
        :param other: der andere Bruch
        :return: self Bruch wird gleich gesetzt zurückgegeben.
        """
        return float(self) == float(other)

    def __str__(self):
        return "({0}{1})".format(abs(self.numerator), "/" + str(abs(self.denominator)) if self.denominator is not 1 else "")

    def __abs__(self):
        """
        Die Funtion berechnet den absoluten Wert des Bruches
        :return: der Bruch wird zurückgegeben
        """
        return abs(float(self))

    def __neg__(self):
        """

        :return:
        """
        return Bruch(-self.numerator,self.denominator)

    def __gt__(self, other):
        """
        Die Funktion prüft ob, self größer als other ist.
        :param other: der andere Bruch
        :return: wird true oder false zurückgegeben
        """
        return float(self) > float(other)

    def __lt__(self, other):
        """
        Die Funktion prüft ob, self kleiner als other ist.
        :param other: der other Bruch
        :return: wird true oder false zrückgegeben
        """
        return float(self) < float(other)

    def __ge__(self, other):
        """
        Die Funktion prüft ob, self größergleich als other ist.
        :param other: der andere Bruch
        :return: wird true oder false zurückgegeben
        """
        return float(self) >= float(other)

    def __le__(self, other):
        """
        Die Funktion prüft ob, self kleinergleich als other ist.
        :param other: der other Bruch
        :return: wird true oder false zrückgegeben
        """
        return float(self) <= float(other)

    def __iter__(self):
        return iter([self.numerator,self.denominator])
    
    def __add__(self, other):
        """
        Die Funtion addiert zwei Brüche und gibt sie zurück
        :param other: der other Bruch
        :return: der addierte Bruch Bruch wird zurückgegeben
        """
        other = Bruch(other)
        minimum = min(self, other)
        maximum = max(self, other)
        kgv = int(kgV(minimum.denominator, maximum.denominator))
        a = int(kgv / minimum.denominator)
        b = int(kgv / maximum.denominator)
        return Bruch(minimum.numerator * a + maximum.numerator * b, kgv)

    def __radd__(self, other):
            return self + other

    def __iadd__(self, other):
        return other + self

    def __sub__(self, other):
        """
        Diese Funktion subtrahiert zwie Brüche
        :param other: der other Bruch
        :return: der Subtrahierte Bruch wird zurückgegeben
        """
        return Bruch.__add__(self,-other)

    def __rsub__(self, other):
        return -self + other

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        """
        Die Funktion multipliziert zwei Brüche
        :param other: der other Bruch
        :return: der multiplizierte Bruch wird zurückgegeben
        """
        return Bruch(self.numerator * Bruch(other).numerator, self.denominator * Bruch(other).denominator)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return other * self

    def __truediv__(self, other):
        """
        Diese Funtion dividiert zwei Brüche
        Der Zähler und der Nenner des other Bruches werden vertauscht
        :param other: der other Bruch
        :return: das Ergbniss wird zurückgegeben
        """
        return self * ~Bruch(other)

    def __rtruediv__(self, other):
        return Bruch.__truediv__(other,self)

    def __itruediv__(self, other):
        return self / other

    @classmethod
    def _Bruch__makeBruch(cls,other):
        if type(other) is not int:
            raise TypeError
        else:
            return Bruch(other)

def ggT(a,b):
    """
    Diese Funktion gibt den größte gemeinsame Teiler ggT von a und b zurück.
    :param a: der erste Wert
    :param b: der zweite Wert
    :return: der ggt von a und b wird zurückgegeben
    """
    while b != 0:
        c = a % b
        a,b = b,c
    return a

def kgV(a,b):
    """
    Diese Funktion bestimmt kleinstes geimsames Vielfaches kgV von a und b
    :param a: der erste Wert
    :param b: der zweite Wert
    :return: kgV wird zurückgegeben
    """
    return (a * b) / ggT(a,b)