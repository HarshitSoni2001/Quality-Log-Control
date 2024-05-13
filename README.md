Steps to Run the Quality Log control:-
1. you need to make the log injestor file in which the api configuration is added and logs are been injected on basis of date and time.  save file as log_ingestor.py
2. now make the query interface,i am using flask for making it in which all the logs entries are added and render with the search template with filter logs and adding a json file also in which all logs are stored. save file as app.py
3. now make a Html template for running this interface and link the app.py with it in the same folder.
4. make another html page for search results to redirecting the search results to be appeared and save it as search_results.html

now directly run the app.py after save all files in the same folder or open http://127.0.0.1:5000/
