from kafka import KafkaProducer
import json
from data import get_food_data
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    for i in range(10):
        food_data = get_food_data()
        print(food_data)
        producer.send("food_data", value=food_data)
        time.sleep(30)

    producer.close()
