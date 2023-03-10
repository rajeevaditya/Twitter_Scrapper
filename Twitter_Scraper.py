import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
import datetime
import pymongo
import time

# REQUIRED VARIABLES
client = pymongo.MongoClient("mongodb+srv://rajeevaditya143:electronicgeek*143@sandbox.1rcrl.mongodb.net/?retryWrites=true&w=majority")  # To connect to MONGODB
mydb = client["Twitter_Database"]    # To create a DATABASE

tweets_df = pd.DataFrame()
st.write("# Twitter Data scraping")
option = st.selectbox('How would you like the data to be searched?',('Keyword', 'Hashtag'))
word = st.text_input('Please enter a '+option, 'RRR')
start = st.date_input("Select the start date", datetime.date(2022, 1, 1),key='d1')
end = st.date_input("Select the end date", datetime.date(2023, 1, 1),key='d2')
tweet_c = st.slider('How many tweets to scrape', 0, 1000, 5)
tweets_list = []

# SCRAPE DATA USING TwitterSearchScraper
if word:
    if option=='Keyword':
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{word} + since:{start} until:{end}').get_items()):
            if i>=tweet_c:
                break
            tweets_list.append([ tweet.id, tweet.date,  tweet.content, tweet.lang, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount, tweet.source, tweet.url ])
        tweets_df = pd.DataFrame(tweets_list, columns=['ID','Date','Content', 'Language', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount','Source', 'Url'])
    else:
        for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'{word} + since:{start} until:{end}').get_items()):
            if i>tweet_c:
                break            
            tweets_list.append([ tweet.id, tweet.date,  tweet.content, tweet.lang, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount, tweet.source, tweet.url ])
        tweets_df = pd.DataFrame(tweets_list, columns=['ID','Date','Content', 'Language', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount','Source', 'Url'])
else:
    st.warning(option,' cant be empty', icon="⚠️")

# DOWNLOAD AS CSV
@st.cache # IMPORTANT: Cache the conversion to prevent computation on every rerun
def convert_df(df):    
    return df.to_csv().encode('utf-8')


if not tweets_df.empty:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        csv = convert_df(tweets_df) # CSV
        c=st.download_button(label="Download data as CSV",data=csv,file_name='Twitter_data.csv',mime='text/csv',)        
    with col2:    # JSON
        json_string = tweets_df.to_json(orient ='records')
        j=st.download_button(label="Download data as JSON",file_name="Twitter_data.json",mime="application/json",data=json_string,)

    with col3: # SHOW
        y=st.button('Show Filtered Tweets',key=2)

    with col4:
        z=st.button('Upload Tweets to Database',key=3)        

if c:
    st.success("The Scraped Data is Downloaded as .CSV file:",icon="✅")  
if j:
    st.success("The Scraped Data is Downloaded as .JSON file",icon="✅")     

if y: # DISPLAY
    st.success("Tweets Scraped Successfully:",icon="✅")
    st.write(tweets_df)

if z: # upload to DB
       # UPLOAD DATA TO DATABASE
        coll=word
        coll=coll.replace(' ','_')+'_Tweets'
        mycoll=mydb[coll]
        dict=tweets_df.to_dict('records')
        if dict:
            mycoll.insert_many(dict) 
            ts = time.time()
            mycoll.update_many({}, {"$set": {"KeyWord_or_Hashtag": word+str(ts)}}, upsert=False, array_filters=None)
            st.success('Successfully uploaded to database', icon="✅")
        else:
            st.warning('Cant upload because there are no tweets', icon="⚠️")

    


            

