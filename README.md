1. Extract the file Group27_Final_Assignment.zip

2. Run requirements.txt by using the following command
```
pip install requirements.txt
```

3. Run the Group27_Product_recommender.ipynb file

4. Run the ngrok.exe

5. Run the command on ngrok command prompt
```
ngrok http 5000
``` 

6. Copy the link mentioned in ngrok server's "Forwarding" section and paste it in Dialogflow's fulfilment URL and add  "/recommend" at the end
	example : https://d8ea-2607-fea8-c3a1-e900-48a7-d5e1-f354-c38a.ngrok.io/recommend
  
7. Make sure intent's fulfilment are enabled
5. Run the Backend.py file

7. Open the dialogflow using the following link
   https://bot.dialogflow.com/fef64af0-d8b9-4eb6-94c5-f1d5148191b2
	or
   https://dialogflow.cloud.google.com/#/agent/product-recommendation-vsdv/intents
   
8. Start your conversation with hey or mention what you are looking for.

	example : "I need a fan"
  
9. You can also ask for the link to buy the product
