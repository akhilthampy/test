print(r""" ______                          _         _ _       
(____  \                        | |       | (_)      
 ____)  ) ____ _____ _____  ____| |__   __| |_  ____ 
|  __  ( / ___) ___ (____ |/ ___)  _ \ / _  | |/ ___)
| |__)  ) |   | ____/ ___ ( (___| | | ( (_| | | |    
|______/|_|   |_____)_____|\____)_| |_|\____|_|_|    
                                                     
             https://github.com/akhilwrist                                               """)
import requests
c=input("enter email:- ")
url = "https://breachdirectory.p.rapidapi.com/"
querystring = {"func":"auto","term":[c]}

headers = {
    'x-rapidapi-host': "breachdirectory.p.rapidapi.com",
    'x-rapidapi-key': "e72ad64babmsh991faf2bd3d9e8cp1b1e6ajsn5c1f000514be"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
