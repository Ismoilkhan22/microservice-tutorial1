from aiokafka import AIOKafkaProducer
from aiokafka.structs import RecordMetadata
import json
from typing import Dict, Any



async def send_event(producer:AIOKafkaProducer, topic:str, event:Dict[str,Any]):
    event_json = json.dumps(event)
    await producer.send_and_wait(topic, event_json.encode('utf-8'))




