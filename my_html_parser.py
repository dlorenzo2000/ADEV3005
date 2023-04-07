"""
Name:           Dean Lorenzo
Assignment:     Challenge 9A
Purpose:        Using Revision control on a past assignment.
Date:           Apr 7, 2023
"""

from html.parser import HTMLParser
import urllib.request

"""
This module parses the users IP address from the site
http://checkip.dyndns.org/
"""

class MyHTMLParser(HTMLParser):
    """
    This class parses HTML and inherits the HTMLParser base class.
    """
    def __init__(self):
        """
        Constructor that creates a field self.ip
        """
        super().__init__()
        self.ip = ''
    def handle_data(self, data):
        """
        This method splits the data when it finds "Current IP and then 
        strips everything else away from that string.
        """
        if "Current IP" in data:
            self.ip = data.split(":")[-1].strip()

def get_ip_address():
    """
    This function returns the ip address of the user.
    """
    parser = MyHTMLParser()
    my_url = "http://checkip.dyndns.org/"
    with urllib.request.urlopen(my_url) as response:
        html = str(response.read())

    parser.feed(html)
    return parser.ip

if __name__ == "__main__":
    """
    This block of code runs when the module is executed as the main program. It
    calls the get_ip_address() function to retrieve the user's IP address and 
    prints it to the console.
    """

    print(get_ip_address())
