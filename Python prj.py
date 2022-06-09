#Task 1a , Task 1b 

print ("----Server Status----")


import requests
#request in this script will be utilized to retrieve the data from server 
import requests as req
from pprint import pprint

from bs4 import BeautifulSoup as bs
#used for parsing the document data
from urllib.parse import urljoin


#getting the status code of server 
resp = req.get("http://testphp.vulnweb.com/listproducts.php?cat=1")
print(resp.status_code)


def get_all_forms(url):

    
    soup = bs(requests.get(url).content, "html.parser")

    return soup.find_all("form")

 
 

def get_form_details(form):

    

    #This function extracts all possible useful information about an HTML `form`

    
    details = {}

    # get the form action (target url)

    action = form.attrs.get("action").lower()

    # get the form method (POST, GET, etc.)

    method = form.attrs.get("method", "get").lower()

    # get all the input details such as type and name

    inputs = []

    for input_tag in form.find_all("input"):

        input_type = input_tag.attrs.get("type", "text")

        input_name = input_tag.attrs.get("name")

        inputs.append({"type": input_type, "name": input_name})

    # put everything to the resulting dictionary

    details["action"] = action

    details["method"] = method

    details["inputs"] = inputs

    return details

 

 

def submit_form(form_details, url, value):


      #  form_details (list): a dictionary that contain form information

      # url (str): the original URL that contain that form

        # value (str): this will be replaced to all text and search inputs

    # Returns the HTTP Response after form submission

 

    # construct the full URL (if the url provided in action is relative)

    target_url = urljoin(url, form_details["action"])

    # Gets inputs

    inputs = form_details["inputs"]

    data = {}

    for input in inputs:

        # replace all text and search values with `value`

        if input["type"] == "text" or input["type"] == "search":

            input["value"] = value

        input_name = input.get("name")

        input_value = input.get("value")

        if input_name and input_value:

            # if input name and value are not None,

            # then add them to the data of form submission

            data[input_name] = input_value

 

    if form_details["method"] == "post":

        return requests.post(target_url, data=data)

    else:

        # GET request

        return requests.get(target_url, params=data)

 

 

def scan_xss(url):

    

   ## Given a `url`, it prints all XSS vulnerable forms and returns True if any is vulnerable, False otherwise



    # get all the forms from the URL

    forms = get_all_forms(url)

    print(f"[+] Detected {len(forms)} forms on {url}.")

    js_script = "<Script>alert('hi')</scripT>"

    # returning value

    is_vulnerable = False

    # iterate over all forms

    for form in forms:

        form_details = get_form_details(form)

        content = submit_form(form_details, url, js_script).content.decode()

        if js_script in content:

            print(f"[+] XSS Detected on {url}")

            print(f"[*] Form details:")

            pprint(form_details)

            is_vulnerable = True

            # won't break because we want to print other available vulnerable forms

    return is_vulnerable

 

import http.server

if __name__ == "__main__":

    url = 'http://testphp.vulnweb.com/listproducts.php?cat=1'

    print(scan_xss(url))
    
#Task 1c , Will save Logs for the given server

import logging


def main():
    # Configure the logging system
    
    logging.basicConfig(filename ='pyproj.log',
                        level = logging.ERROR)
      
    # Variables (to make the calls that follow work)
    hostname = 'http://testphp.vulnweb.com/listproducts.php?cat=1'
    filename = 'datalog.txt'
    mode = 'r'
      
    logging.basicConfig( 
        filename = 'pyproj.log', 
        level = logging.WARNING, 
        format = '%(levelname)s:%(asctime)s:%(message)s')
    
    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode = %r', filename, mode)
    logging.debug('Got here')
      
if __name__ == '__main__':
    main()
    
print ("LogSaved Successfully")
    
    