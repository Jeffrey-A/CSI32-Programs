from math import gcd

class Fraction:

    def __init__(self, numerator=0, denominator=1):
        self.nu = numerator #Jeff added this
        self.de = denominator #Jeff added this
        if denominator == 0: # fraction is undefined
            self._numer = 0
            self._denom = 0
        else:
            factor = gcd( abs(numerator), abs(denominator) )
            if denominator < 0: # want to divide through by negated factor
                factor = -factor
            self._numer = numerator // factor
            self._denom = denominator // factor
    #...................................................
    #Jeffrey Almanzar        
    #...................................................
    '''Exercise 6.10: The syntax −x for an object x is supported by that class’s __neg__
        method. Implement such a method for the Fraction class that returns a new fraction
        that is the negation of the original.'''
    def __neg__(self): 
        return str(-self.nu) + '/' + str(self.de)
    
    '''Exercise 6.11: Add an invert method to the Fraction class that returns a new fraction that
        is the reciprocal of the original.'''
    def invert(self):
        return str(self.de) + '/' + str(self.nu)

    #Testing at the bottom
    #....................................................



    ######## Arithmetic Methods ########
    def __add__(self, other):
        return Fraction(self._numer * other._denom + self._denom * other._numer,
                self._denom * other._denom)

    def __sub__(self, other):
        return Fraction(self._numer * other._denom - self._denom * other._numer,
            self._denom * other._denom)
    def __mul__(self, other):
        return Fraction(self._numer * other._numer, self._denom * other._denom)

    def __div__(self, other):
        return Fraction(self._numer * other._denom, self._denom * other._numer)

    ######## Comparison Methods ########
    def __lt__(self, other):
        return self._numer * other._denom < self._denom * other._numer

    def __eq__(self, other):
        return self._numer == other._numer and self._denom == other._denom

    ######## Type Conversion Methods ########
    def __float__(self):
        return float(self._numer) / self._denom

    def __int__(self):
        return int(float(self)) # convert to float, then truncate

    def __str__(self):
        if self._denom == 0:
            return 'Undefined'
        elif self._denom == 1:
            return str(self._numer)
        else:
            return str(self._numer) + '/' + str(self._denom)

#Testing
a = Fraction(20,4)
print('................')
print('Original 20/4')
print('................')
print(a.__neg__(),'Negation')
print(a.invert(),'Reciprocal')
