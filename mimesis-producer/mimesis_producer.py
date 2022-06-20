"""Produce openweathermap content to 'mimesis' kafka topic."""
import asyncio
import configparser
import os
import time
from collections import namedtuple
from kafka import KafkaProducer
from mimesis import Food
from mimesis import Text
from mimesis import Science
from mimesis import Person
import json

food = Food()
text = Text()
person = Person()


def get_food_data():
    return {
        "chef": person.first_name(),
        "chef_nationality": person.nationality(),
        "dish": food.dish(),
        "drink": food.drink(),
        "fruit": food.fruit(),
        "level": text.level(),
        "quote": text.quote(),
        "spices": food.spices(),
        "vegetable": food.vegetable()

    }


KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TOPIC_NAME = os.environ.get("TOPIC_NAME")
SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 20))



def run():
    iterator = 0
    print("Setting up faker producer at {}".format(KAFKA_BROKER_URL))
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER_URL],
        # Encode all values as JSON
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    )

    while True:        
        # adding prints for debugging in logs
        print("Sending new mimesis data iteration - {}".format(iterator))
        food_data = get_food_data()
        print(food_data)
        producer.send(TOPIC_NAME, value=food_data)
        print("New mimesis data sent")
        time.sleep(SLEEP_TIME)
        print("Waking up!")
        iterator += 1


if __name__ == "__main__":
    run()
