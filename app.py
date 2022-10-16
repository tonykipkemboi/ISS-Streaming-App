import json
from json import dumps
import urllib.request

from time import sleep
from kafka import KafkaProducer


def locate_iss(url: str) -> json:
    """
    Polls and returns current location of the ISS 
    using the Open Notify API

    Parameter:
    ----------
        url: site to query data from

    Return:
    -------
        location: json output howing current location of the ISS
    """

    response = urllib.request.urlopen(url)
    location = json.loads(response.read())

    return location


if __name__ == '__main__':
    # url to query data from
    URL = 'http://api.open-notify.org/iss-now.json'

    # setup kafka producer
    producer = KafkaProducer(bootstrap_servers=[
                             'localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

    while True:
        # Query every 5 seconds
        data = locate_iss(URL)
        print(data)
        producer.send('iss-topic', value=data)
        sleep(5)
