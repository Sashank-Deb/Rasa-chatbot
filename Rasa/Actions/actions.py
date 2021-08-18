# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_carousels"
    
    def run(self, dispatcher: CollectingDispatcher , tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    # {
                    #     "title": "Carousel 1",
                    #     "subtitle": "$10",
                    #     "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqhmyBRCngkU_OKSL6gBQxCSH-cufgmZwb2w&usqp=CAU",
                    #     "buttons": [ 
                    #         {
                    #         "title": "Happy",
                    #         "payload": "Happy",
                    #         "type": "postback"
                    #         },
                    #         {
                    #         "title": "sad",
                    #         "payload": "sad",
                    #         "type": "postback"
                    #         }
                    #     ]
                    # },
                    {
                        "title": "VIT Chennai",
                        "subtitle": "College Website",
                        "image_url": "https://images.shiksha.com/mediadata/images/1509948169phpMDRDaE.jpeg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://vit.ac.in/",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []