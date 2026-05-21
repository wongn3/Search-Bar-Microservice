#This is for the Search Bar Microservice

## 1. Desription

This is a microservice that provides a simple search bar function for websites by comparing a user's search input.
The Result testers has 2 different calls.

a. Search will act like the search bar and allow for user input. The user can type what they want and hit enter to
submit their search.   
b. Result will display the results of the search. Given the user input. It will show results that match.

Note: There is a "No Match Found" result if no results match.

------------------------------------------------------------------------------------

## 2. How to run the microservice

1. Open the Input Tester and run it in the terminal.
2. Select the search option for the test.
3. Type what you want to search by and hit enter to confirm
4. Run the microservice (Resulter.py) in the terminal 
5. Run the Input Tester again and run it in the terminal
6. Result will print in the terminal.
python History_MS.py

------------------------------------------------------------------------------------

## 3. Request 

To request data from this microservice, another program will need to update the request.txt file with words or phrase
you want to use as the search result

A program can send this request by writing to the text file like this: 

user_search = input("Very Fancy Search Bar: ")
  
with open("request.txt", "w") as f:
        f.write(user_search)

------------------------------------------------------------------------------------

## 4. Recieve

After sending a request, the microservice will respond by updating the response.txt with the search results.

The microsservice will do this by doing something like this: 

with open("response.txt", "w") as f:
        f.write(result)

------------------------------------------------------------------------------------

## 5. Sequence UML
<img width="3750" height="2325" alt="CS361 Search MS Prototype 1 UML" src="https://github.com/user-attachments/assets/ca4395a5-a72d-488b-b3de-4fa774310152" />

