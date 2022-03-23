import datetime as dt 
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests as rq
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="La hora actual es:"f"{dt.datetime.now()}")

        return []
class LlamadaApi(Action):
    def name(self) -> Text:
        return "action_call_bus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        r=rq.get("https://www.zaragoza.es/sede/servicio/monumento.geojson?srsname=wgs84&rows=1&fl=id,title,description,geometry")
        dispatcher.utter_message(text="El primer bus llega en : "+str(r.json()['features'][0]['properties']['title']))

        return []