import requests
import json
import pandas as pd

url = "Unknown" 
userID = ""
userPSW = ""

class Stack:
    def __init__(self):
        self.url = "Unknown"
        self.userID = "xx"
        self.userPSW = "yy"
        self.token_url = "Unknown"
        self.json_user = "zz"
        
stack_ret = Stack()


def get_token(): #(url_var, json_var):
    print("Get token", end =" ") 
    response = requests.post(url=stack_ret.token_url, json=stack_ret.json_user)
    if (response.status_code != 200):
        print(response.json())
        return None
    else:        
        json_obj = response.json()
        jresp = json_obj['data']
        token = jresp['token']
        #print(token)
        bearer = "Bearer " + token
        header = {"Authorization": bearer}
        return header
        
        
def get_stack(stack_name):
    df = pd.read_csv ("certificates.csv")
    last_row = df.shape[0]

    for row in range(0, last_row):
        ttype = df.iloc[row,1] 
        stack = df.iloc[row,0]
        if(stack == stack_name and ttype == "service"):
            stack_ret.url = df.iloc[row,2]
            stack_ret.userID = df.iloc[row,3]
            stack_ret.userPSW = df.iloc[row,4]   
    if(stack_ret.url != "Unknown"):    
        print(stack_ret.url + " User/Client: " + stack_ret.userID)
        stack_ret.token_url = stack_ret.url + "/auth/login"
        stack_ret.json_user = {"email": stack_ret.userID, "password": stack_ret.userPSW}
    else:
        print("Couldn't find stack from certificates.csv")
        sys.exit(1)           
    return stack_ret    


