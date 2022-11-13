# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Action server is called")
        dispatcher.utter_message(text="Hello World!")

        return []

class ApiAction(Action):

    def name(self) -> Text:
        return "action_get_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category = tracker.get_slot("category")
        print(f"category identified is : {category} ")
        url = 'https://api.nytimes.com/svc/news/v3/content/all/{category}.json'.format(category=category)
        params = {'api-key': "2hq54bvFO0yWiRdY70reBU2GmusBtnwM", 'limit': 5}
        response = requests.get(url,params).text
        json_data = json.loads(response)["results"]

        i = 0
        for data in json_data:
            i += 1
            message = f"{str(i)}. {data['title']}"
            dispatcher.utter_message(message)
        return []
