from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from aiokafka.structs import RecordMetadata
import json
from typing import Dict, Any
from tenacity import retry, stop_after_attempt, wait_exponential
from chat_service.app.config import settings

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
async def send_event(producer: AIOKafkaProducer, topic: str, event: Dict[str, Any]) -> RecordMetadata:
    event_json = json.dumps(event)
    fut = await producer.send_and_wait(topic, value=event_json.encode('utf-8'))
    return fut

async def get_producer():
    producer = AIOKafkaProducer(bootstrap_servers=settings.kafka_bootstrap_servers)
    await producer.start()
    return producer

async def get_consumer(topic: str):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=settings.kafka_bootstrap_servers,
        group_id="chat-group"  # Har service uchun unique
    )
    await consumer.start()
    return consumer
