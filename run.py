import requests
import json
import os

# Add Your Token In The Header 
header = {'Authorization' : 'Token 30ee4e1d076f5fa61c4f8eba048f734decccb4de',
# To get the API Token Key visit "https://secretmessage.pythonanywhere.com/" , if you don't have one.
}

# Creating Message
def message_create():
    # This is the default url, you can leave it just as it is.
    url = "https://secretmessage.pythonanywhere.com/api/message-create/"
    
    # Getting data input to create the message
    body = input("--> Enter Your Message: ")
    os.system("clear")
    # Password must be created, otherwise it won't create the message
    password = input("--> Create a Password: ") 
    os.system("clear")
    
    data = {
        "body" : body,
        "file" : None,
        "password" : password
      }
    
    # This must be a "POST" request
    # Making request through post method by adding API Token and adding the data, to Create a Message.
    response = requests.post(url,headers = header,data = data)
    
    # Using json module to get the data in a Clean and Formatted way.
    object = json.loads(response.text)
    print(json.dumps(object,indent = 3,ensure_ascii = False))
    print("\nYour Message is Created!!!")

# Message History
def message_history():
    # This is the default url, you can leave it just as it is.
    url = "https://secretmessage.pythonanywhere.com/api/message-history/"
    
    # This must be a "GET" request
    # Making request through get method by adding API Token, to Show the History of your Messages.
    response = requests.get(url, headers = header)

    # Using json module to get the data in a Clean and Formatted way.
    object = json.loads(response.text) 
    print(json.dumps(object,indent=3,ensure_ascii=False))

# Showing message
def show_message():
    # Getting the input of particular link of a Message.
    link = input("--> Enter the Message Link: ")
    
    # The default message link doesn't has a word "/api" which is required to make request using API.(In browser the link doesn't require any word "/api".)
    # This adds the word "/api" automatically,so you don't have to worry and just paste the message link as it is.
    url = link[0:40]+"/api"+link[40:]
    
    os.system("clear")
    
    # It'll try to view the message by getting the "Password" of the message, if the message belongs to other person.
    try:
        password = input("--> Enter the Password: ")
        os.system("clear")
        data = {"password" : password} 
        # Must be a "POST" request
        response= requests.post(url, headers = header,data = data)
        
    # It'll view the message without having to enter the password, if the message belongs to yourself.
    except:
        # Must be a "POST" request
        response= requests.post(url, headers = header)
    
    # Using json module to get the data in a Clean and Formatted way.
    object = json.loads(response.text) 
    print(json.dumps(object,indent=3,ensure_ascii=False))

if __name__ == "__main__":
    # Running the function through while loop, inorder to execute it again and again.
    while True:
        print("---> 1.Create Message\n")
        print("---> 2.Show Message\n")
        print("---> 3.Message History\n")
        
        choice = input("\n-> Enter Your Choice: ")
        os.system("clear")
        
        if choice == "1":
            message_create()
            exit()
        elif choice == "2":
            show_message()
            exit()
        elif choice == "3":
            message_history()
            exit()
        else:
            print("\n<---------- Invalid Choice!!! ---------->\n\n")
   
      