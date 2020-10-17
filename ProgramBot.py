import requests

def prob_name(k):
    """
    Seraching  the programs based on tags given by the User
    """

    tag = input("Please enter the tag : ") # Asks the User for entering the Tag
    tag.strip() # Removing extra spaces from front and end of the given tag
    tag.replace(" ","%20") # Replacing the spaces inbetween the tag 
    link= "https://codeforces.com/api/problemset.problems?tags="+tag # for finding problems based on given tags
    page = requests.get(link) # Passing the tag to Requests package
    try:
        for i in range(k,k+11):
            print("\n",f"{page.json()['result']['problems'][i]['name']}") # Prints the Problem name

            prob_contestId = page.json()['result']['problems'][i]['contestId'] # Problem contest Id 
            prob_index = page.json()['result']['problems'][i]['index'] # Problem index in the respective contest

            print("Link : ",f"https://codeforces.com/problemset/problem/{prob_contestId}/{prob_index}") # Link for the respective Problem

    except:
        print("PLEASE ENTER THE TAGS WHICH ARE AVAILABLE") # If any Errors arises
