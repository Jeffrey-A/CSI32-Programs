
class Date:
    monthNames = ('January', 'February', 'March',
        'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December')
    def __init__(self):
        # By default: January 1, 2000
        self._month = 1
        self._day = 1
        self._year = 2000
        
    '''(a)Define a getDay function
        that returns the day as an integer.'''
    def getDay(self):
        return self._day
    
    '''(b) Define a setYear function that
        takes an integer parameter specifying the year
        and sets the value of the year attribute.'''
    def setYear(self,year):
        self._year = year

    '''(c) Define the __str__ function.
        This should return a string that represents the
        date in the format 'January 1, 2000'.'''
    def __str__(self):
        self.months = ('January', 'February', 'March',
        'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December')
        
        date = str(self.months[self._month-1])+" "+ str(self._day)+','+" "+str(self._year)
        return date
#Testing
date = Date()
date.getDay()#a
date.setYear(2000)#b
print(date)#c
        
        
        
