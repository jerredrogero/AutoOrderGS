
class Displate:
    def __init__(self, link, size):
        self.link = link
        self.size = size

class Shipping:
    def __init__(self, first, last, address1, address2, zip, city, state, phone):
        self.first = first
        self.last = last
        self.address1 = address1
        self.address2 = address2
        self.zip = zip
        self.city = city
        self.state = state
        self.phone = phone




#Step 1: Enter Displate URL and Size:
displate1 = Displate('https://displate.com/displate/2155588', 'l')
displate2 = Displate('https://displate.com/displate/2155645', 'l')
displate3 = Displate('https://displate.com/displate/2155592', 'l')

#Step 2: Enter shipping info
info = Shipping('First', 'Last', 'Address', 'Address1', 'Zip', 'City', 'State', 'Phone')

#Step 3: Go to Automation.py and set the quanity of Displates

