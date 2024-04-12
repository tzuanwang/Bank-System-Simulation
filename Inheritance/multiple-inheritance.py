class OperatingSystem:
    multiTasking = True
    name = 'Mac OS'

class Apple:
    website = 'www.apple.com'
    name = 'Apple'

class MacBook(OperatingSystem, Apple):
    
    def __init__(self):
        if self.multiTasking is True:
            print('This is a multi-tasking system. Visit {} for more details.'.format(self.website))
            print('Name: ', self.name) # depends on the order it inherits

macBook = MacBook()