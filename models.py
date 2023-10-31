from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WhatsAppMessage(Base):
    __tablename__ = 'whatsapp_messages'  # Il nome della tabella nel database

    id = Column(Integer, primary_key=True)
    message = Column(String)  # Campo per memorizzare il messaggio WhatsApp ricevuto
    response = Column(String)  # Campo per memorizzare la risposta del chatbot

    def __init__(self, message, response):
        self.message = message
        self.response = response

    def __repr__(self):
        return f"<WhatsAppMessage(id={self.id}, message='{self.message}', response='{self.response}')>"
