class HousemateHelper:
    '''This is the top level class that control the entire program.
        it uses the classes Person and Item.'''

    def __init__(self):
        self.UI = UserInterface()
        self.total_money_spent = 0
        self.inventory = {'food':0,'utility':0,'toy':0}
        self.people = {}
        
    def addPurchase(self,person,item_string,quantity,cost): #Working good
        '''It saves data: name of the person, the item he bought,
            the quantity of that item and the total money he spent.'''
        self.person = Person(person,cost)
        self.people[self.person.getName()] = self.person.getMoneyspent()
        
            
        self.item = Item(item_string,quantity)
        if item_string in self.inventory:
            self.inventory[item_string] = self.inventory[item_string] + self.item.getQuantity()
       
        
    def getInventory(self,item_string):#working good
        '''it takes an item-string: food,utility or toy as input and return the current amount of that item.'''
        for key in self.inventory:
            if item_string == key:
                return self.inventory[key],self.total_money_spent 
    
    def useItem(self,item_string,num): #Working good
        '''it takes an item-string: food, utility or toy and integer num as input,
            then it removes num of that item from the inventory.'''
        for key in self.inventory:
            if item_string == key:
                self.inventory[key] = self.inventory[key] - num
    
    def personValue(self,name):#Working well
        '''it takes an string as input indicating the name of a person that has purchased something,
            and it returns how much that person needs to pay'''
        self.each = self.total_money_spent/ len(self.people) #each person should pay this  
        if name in self.people:
            for key in self.people:
                if name == key:
                    if self.people[key] < self.each: #If that person paid less than what he should pay
                        self.need_to_pay = self.each - self.people[key]
                        return self.need_to_pay #Then he need to pay this
                    else:
                        return  self.each + self.people[key]
                  
    def equalize(self):
        '''It makes sure that all the housemates spent the same amount of money.
            It also identify who need to pay to who and how much.
            It returns a list of tuples, where each tuple is of the form (A, B, x),
            where A and B are person names, and x is an
            amount of money that A should pay to B.'''
        paid = 0
        for person in self.people:
            if self.personValue(person)> 0:
                while self.personValue(person)> 0:
                    paid = paid + 1
                    self.people[person] = self.people[person] + paid
                    for other in self.people:
                        if other != person:
                            if self.people[other] > self.each:
                                self.people[other] = self.people[other] - paid

                return person, other, paid

        for key in self.people:
            print(key, self.people[key])
                              

                
            

        
    def main(self): #under contruction
        for key in self.people:
            self.total_money_spent = self.total_money_spent + self.people[key]
        self.UI.printIntro()
        while True:
            action = self.UI.actions() #Prompts the user for an action
            if action == '':
                break
            elif action == 'a':
                person,item_string,quantity,cost = input("You need to type: name,item, quantity,money spent").split(',')
                self.addPurchase(person,item_string,int(quantity),int(cost))
            elif action == 'b':
                user = input("Get inventory of what item")
                self.getInventory(user)
            elif action == 'c':
                self.useItem()
            elif action == 'd':
                self.personValue()
            elif action == 'e':
                self.equalize()
            else:
                print("Sorry!! this program does not allow that function.")
        
class Person:
    '''This class saves the person's name and the money they spent'''
    def __init__(self, name, money_spent):
        self.name = name
        self.money_spent = money_spent
        
    def getName(self):
        '''It returns the name of the person'''
        return self.name
    
    def getMoneyspent(self):
        '''It returns the money spent'''
        return self.money_spent
    
    def pay(self,num):
        '''it pays num to the specified name'''
        self.money_spent = self.money_spent + num
        
    def getPay(self,num):
        self.money_spent = self.money_spent - num
    
    

class Item:
    '''This class keeps track of the inventory'''

    def __init__(self, item, num ):
        self.item = item
        self.quantity = num

    def getItem(self):
        '''it returns the item'''
        return self.item
    
    def getQuantity(self):
        '''it return the quantity of a specified item'''
        return self.quantity
    

class UserInterface:

    def printIntro(self):#Under constr
        '''print an introduction to the program'''
        print("This is the Housemate Helper program")

    def actions(self):
        '''It prompts the user for an action to perform: addpurchase, useitem, equalize expenses...etc
            and returns a string indicating the action to perform'''

        actions = {'Add_purchase':'a','get_inventory':'b','use_item':'c','see_money-owed':'d','equalize_expenses':'e'}
        for key in actions:
            print(key,':',actions[key])
        user = input("What acction would you like to perfom? -- indicate the letter --> ")
        for key in actions:
            if user[0] == actions[key]:
                return actions[key]
    
    def printSummary(self): #Under constr
        '''print out the amount of money that a housemate need to pay to another 
            and the amount of each item that are left in the house. '''
        pass
