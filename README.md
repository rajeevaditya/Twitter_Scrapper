# Twitter_Scrapper Using snscrape and streamlit

Interative GUI using streamlit for twitter scraping 

REQUIRED SKILLS:
1.	Python scripting
2.	MongoDB
3.	Streamlit
4.	Snscrape

OVERVIEW:

I have Created a GUI using streamlit that contains the follwing  features
1. Can enter any keyword or Hashtag to be searched, 
2. select the starting date 
3. select the ending date  
4. Number of tweets needs to be scrapped.

After scraping is done, it has the following options

1.	Download data as CSV
2.	Download data as JSON
3.	Display All the Tweets scraped
4.	Upload data to DATABASE


WORKING:

Step1:
Initially I collected the Keyword, Start date, End date, and Number of tweets from the user using streamlit

Step 2:
The above details are fed to TwitterSearchScraper and TwitterHashtagScraper.
A dataframe is created to store the entire scraped data
Now we can download this scraped data in the form of CSV or JSON format 

Step3:
The database connection is established using pymongo
A new collection will be created and data is uploaded into that collection  if the user wish to upload 


HOW TO RUN TWITTER SCRAPER IN YOUR MACHINE:
open cmd:
1. > C:\Users\mypc> pip install virtualenv 
2. > C:\Users\mypc> virtualenv Raj_twitter_env
3. > C:\Users\mypc> cd Raj_twitter_env
4. > C:\Users\mypc\Raj_twitter_env> cd Scripts
5. > C:\Users\mypc\Raj_twitter_env\Scripts>activate                    # It will activate the virtual environment
6. > (Raj_twitter_env)  C:\Users\mypc\> mkdir Twitter_Scraper           #create a folder 
7. > (Raj_twitter_env)  C:\Users\mypc\> cd Twitter_Scraper              # download the above files from this repository and place inside this folder
8. > (Raj_twitter_env)  C:\Users\mypc\Twitter_Scraper> pip install -r requirements.txt       # it will install all the required modules in the environment
9. > (Raj_twitter_env)  C:\Users\mypc\Twitter_Scraper> streamlit run Twitter_Scraper.py   # Now run the app using streamlit
10. > You can now view your Streamlit app in your browser.
11.   Local URL: http://localhost:8501
12.   Network URL: http://192.168.107.230:8501
  
 After clicking on the above url you can see the app in your browser





