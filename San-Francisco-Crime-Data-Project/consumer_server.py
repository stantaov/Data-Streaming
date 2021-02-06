from kafka import KafkaConsumer
import time


class Consumer(KafkaConsumer):
    
    
    def __init__(self, topic, **kwargs):
        super().__init__(**kwargs)
        self.topic = topic
        self.consumer = KafkaConsumer(
                        bootstrap_servers="localhost:9092",
                        request_timeout_ms = 10000, 
                        auto_offset_reset="earliest", 
                        max_poll_records=10
        )
        self.consumer.subscribe(topics=self.topic)
        
    def poll_data(self):
        try:
            while True:
                messages = self.consumer.poll().values()
                for message in messages:
                    for i in message:
                        print(i.value)
        except:
            print("Error: Consumer is closed")
            self.consumer.close()       

            
def kafka_consumer():
    topic = 'test'
    consumer = Consumer(topic)
    consumer.poll_data()

if __name__=='__main__':
    kafka_consumer()