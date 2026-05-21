# this is just for testing (getting a search input and sending it over to the microservice through a txt write)

task = input("Which task you wanna test? [1 = Search | 2 = Result]: ") # (just splitting the two up, for clearner demonstration).

if task == "1":
    # get user input... a title to search up
    # note: to do a genre search, just type "#: _your genere goes here_" [check database.txt for available genres to test]
    user_search = input("Very Fancy Search Bar: ")

    # write down user input in request.txt, for resulter.py (the microservice) to read.
    with open("request.txt", "w") as f:
        f.write(user_search)

if task == "2":
    # if a result is sent back (by microservice to the response.txt), tester reads it.
    with open("response.txt", "r") as f:
        returned_result = f.read()

    # for terminal showcase sake, result will be printed back.
    print("Based on your search: ", returned_result)

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

# P.S. DO NOT TOUCH THE DATABASE! (unless adding content options)