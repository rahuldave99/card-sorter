class Card:
    def __init__(
            self, value, suit):
        self._value = value
        self._suit = suit

    def __str__(self):
        value = self._value
        if(self._value==1):
            value = "Ace"
        if(self._value==11):
            value = "Jack"
        if(self._value==12):
            value = "Queen"
        if(self._value==13):
            value = "King"

        return '%s of %s' % (value, self._suit)