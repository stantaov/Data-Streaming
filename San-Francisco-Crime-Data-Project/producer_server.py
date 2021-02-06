from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    # This function gets data from a json file and reads it line by line
    def generate_data(self):
        with open(self.input_file) as f:
            json_data = json.load(f)
            for line in json_data:
                message = self.dict_to_binary(line)
                #print(line)
                self.send(self.topic,value=message)
                time.sleep(1)


    # This function returns the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf8')

