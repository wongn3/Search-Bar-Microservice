# the main search microservice itself, essentially once we have a list of what can be looked up, and what search input
# the user gives, comparison can be made (in lower cases for decapitalization of case sensitivity).

def search_availability():
    available_content = {} # this stores the database content here in the microservice (like a catalog/dictionary)

    # open and read database.txt to obtain a catalog of what contents are available for lookup
    with open("database.txt", "r") as f:
        for line in f:
            line = line.strip()     # prevent extra spaces and creation of new line (we don't need to read those)
            
            # interpret the seperate and label of the available database content title with its page link
            title, pageURL = line.split("~")
            title = title.strip()
            pageURL = pageURL.strip()

            # store and link the specific title to its specific page link
            available_content[title] = pageURL

    return available_content

def search_request():
    # open and read request.txt to access user search input, remove the space, and return it
    with open("request.txt", "r") as f:
        search_content = f.read().strip()
        return search_content
    
def comparison(search_content, available_content):
    no_match = "No matches found"   # just a variable holder that indicate unsuccessful match (just in case)...

    # the actual comparison between user search input and available search...
    # ...by looping through the titles in available_content, with a lowercase search key.
    # if there's a match, return the corresponding page URL...
    for title in available_content:
        if (search_content.lower() == title.lower()):
            return available_content[title]
        
    # ...otherwise, if the user search isn't listed in one of our database, then state there's no matches.
    return no_match

def result_response(result):
    # open and write in response.txt to send the search result back for the main program to recieve
    with open("response.txt", "w") as f:
        f.write(result)

# the calls for all functions that are used
available_content = search_availability()
search_content = search_request()
result = comparison(search_content, available_content)
result_response(result)

# ====================================================================================
# Execution Order: 
#   > run main (or tester) & enter a search
#       > ...request.txt will then be updated (with the search term)
#   > run microservice (Resulter.py)
#       > ...comparison will be made (between user-input and database)...
#       > ...response.txt will then be updated (with the result)
#   > run main (or tester), again, to obtain result (it'll be printed out)
#       > ...if successful, the redirection URL of the target-search page will be shown
#           > (in the REAL thing, the html will recieve & executed it.)
#       > ...if unsuccessful, a "no match" prompt will be shown.