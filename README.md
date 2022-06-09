# CIS30Final

_________________________________________________________________________________________________________________________________________________________

                                                        CIS-30C Final Project 
_________________________________________________________________________________________________________________________________________________________



_________________________________________________________________________________________________________________________________________________________

                                                               Description 
__________________________________________________________________________________________________________________________________________________________
 

    This script utilizes 7 different python modules , Requests, pprint,urljoin, BeautifulSoup, and Logging module. The Requests module will retrieve the 
    data from the Http server(s) , PPrint is simply utilized to make my output legible. Beautiful Soup is used to parse my data and urlib.parse as well.
    My script begins by getting the status code of my server , to ensure that the server can connect properly . The next portion of the code will test for
    vulnerabilities, specifically XSS vulnerability. The next function will extrat HTML info and then target the url. The details will be extracted and         placed in the resulting dictionary. The script will perform a san for XSS vulnerability , and output will display form and true or false statement.
    The last portion of the script will save the server logs to my system as a text file. 
                             
                             ____________________________________________________________________________
                             
                                                               How to Use 
                             ____________________________________________________________________________
                  
                  Place the full url link where it is requested , there are arrows pointing at wach place there are 3 in total . 
           The script will then run and scan that server and test its connectivity , whether it is vulnerable to XSS and save log to device. 
