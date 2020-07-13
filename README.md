# what_that_text_means
*analyze conversations form a chat messaging app*
<img src="/jpg/image.jpeg">

​
# Overview
*Analyze conversations form a chat messaging app (like slack or whatsapp).* 
The purpose of the analysis is to extract sentiment metrics people interactions.
We are going to create an api service for this purpose. In our current case, the chat service will call our api
endpoints and it's our task to create those endpoints for:
​
- A) Store the data in a `mongodb atlas` database
- B) Do the analysis of the data inside `mongodb atlas`
​
## Project Goals

- Write an API in `flask` just to store chat messages in a mongodb database.
- Extract sentiment from chat messages and perform a report over a whole conversation
- Recommend friends to a user based on the contents from chat `documents` using a recommender system with `NLP` analysis.
- Deploy the service with docker to heroku and store messages in a cloud database.
l this endpoints:
​
### User endpoints
​
- (GET) `/user/create/<username>`
​
  - **Purpose:** Create a user and save into DB
  - **Params:** `username` the user name
  - **Returns:** `user_id`
​
### Chat endpoints
​
- (GET) `/chat/create`
  - **Purpose:** Create a conversation to load messages on it. You can use a `jupyter notebook` to test it using the requests module.
  - **Params:** An array of users ids `[user_id]`
  - **Returns:** `conversation_id`
- (GET) `/chat/<conversation_id>/adduser`
  - **Purpose:** Add a user to a chat conversation
  - **Params:** `user_id`
  - **Returns:** `conversation_id`
- (POST) `/chat/<conversation_id>/addmessage`
  - **Purpose:** Add a message to a conversation. Important: Before adding the chat message to the database, check that the incoming user is part of this conversation. If not, raise an exception.
  - **Params:**
    - `conversation_id`: Chat to store message
    - `user_id`: the user that writes the message
    - `text`: Message text
  - **Returns:** `message_id`
- (GET) `/chat/<conversation_id>/list`
  - **Purpose:** Get all messages from `conversation_id`
  - **Returns:** json array with all messages from this `conversation_id`
​
### Sentiment analysis and recommender
​
- (GET) `/chat/<conversation_id>/sentiment`
  - **Purpose:** Analyze messages from `chat_id`. Use `NLTK` sentiment analysis package for this task
  - **Returns:** json with all sentiments from messages in the chat
​
- (GET) `/user/<user_id>/recommend`
  - **Purpose:** Recommend friend to this user based on chat contents
  - **Returns:** json array with top 3 similar users
​
## References and links
​
- [https://flask.palletsprojects.com/]
- [https://www.getpostman.com/]
- [https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_one]
- [https://api.mongodb.com/python/current/tutorial.html]
- [https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram]
​
NLP & Text Sentiment Analysis:
​
- [https://www.nltk.org/]
- [https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386]
- [https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk]
​
Heroku & Docker
​
- [<https://docs.docker.com/engine/reference/builder/]>
- [<https://runnable.com/docker/python/dockerize-your-python-application]>
- [<https://devcenter.heroku.com/articles/container-registry-and-runtime]>
- [<https://devcenter.heroku.com/categories/deploying-with-docker]>
​
Mongodb Atlas
​
- [<https://www.mongodb.com/cloud/atlas]>
