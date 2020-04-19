
class Displate:
    def __init__(self, link, size):
        self.link = link
        self.size = size

class Shipping:
    def __init__(self, email, phone, name, address1, address2, city, state, zip_code,):
        self.email = email
        self.name = name
        self.address1 = address1
        self.address2 = address2
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.phone = phone

#Step 1: Run "chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation" in the terminal

#Step 2: Enter Displate URL and Size:
displate1 = Displate('https://displate.com/displate/2155588', 'l')
displate2 = Displate('https://displate.com/displate/2155645', 'm')
displate3 = Displate('https://displate.com/displate/2155592', 'xl')

#Step 3: Enter shipping info below (make a copy of the code)
info = Shipping(
    'Email', 'Phone', 'Name', 'Address1', 'Address2', 'City', 'State', '12345',
)

#Step 4: Go to Automation.py and set the quantity of Displates

