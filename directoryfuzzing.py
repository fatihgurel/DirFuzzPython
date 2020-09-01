import requests
import sys
import time
import argparse

start_time = time.time()
print("""__________                _____                        
___  ____/___  ______________(_)_____________ _        
__  /_   _  / / /__  /__  /_  /__  __ \_  __ `/        
_  __/   / /_/ /__  /__  /_  / _  / / /  /_/ /________ 
/_/      \__,_/ _____/____/_/  /_/ /_/_\__, /_(_)(_)(_)
              Fatih Gurel             /____/           """)


parser = argparse.ArgumentParser(description="I like Directory Fuzzing!")
parser.add_argument('-u','--url',required=True,help="Web Site URL")
parser.add_argument('-w','--wordlist',required=True,help="Wordlist Path")

arguments = parser.parse_args()

url = arguments.url
wordlist = arguments.wordlist
status_code_list = [200 , 301 , 302 , 404 , 405 , 406 , 502]
with open(wordlist) as file:
    for line in file:
        full_url = url + line.strip()
        response = requests.get(full_url , allow_redirects = False)
        for code in status_code_list:
            if code == response.status_code:
                print("URL: " + response.url + " Status Code: " + str(response.status_code))
        if full_url[-1:] != "/":
            full_url_new = full_url + "/"
            response1 = requests.get(full_url_new , allow_redirects = False)
            for code1 in status_code_list:
                if code1 == response1.status_code:
                    print("URL: " + response1.url + " Status Code: " + str(response1.status_code))

finish_time = time.time()
total_time = finish_time-start_time
print("Total Time: " , total_time , "seconds")