from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config  # Importa la funzione 'config' da python-decouple

app = Flask(__name)

# Carica le variabili d'ambiente dal file .env
DATABASE_URL = config('DATABASE_URL')
SECRET_KEY = config('SECRET_KEY')
API_KEY = config('API_KEY')

# Crea il motore del database
engine = create_engine(DATABASE_URL)

# Definisci il modello dei dati
Base = declarative_base()

class WhatsAppMessage(Base):
    __tablename__ = 'whatsapp_messages'

    id = Column(Integer, primary_key=True)
    field1 = Column(String)
    field2 = Column(String)

# Crea una sessione del database
Session = sessionmaker(bind=engine)

@app.route('/api/whatsapp', methods=['POST'])
def handle_whatsapp_message():
    try:
        # Ottieni i dati dai messaggi WhatsApp
        data = request.get_json()

        # Esegui la logica del chatbot
        message = data['message']
        # Inserisci qui la tua logica del chatbot

        # Salva i dati nel database
        session = Session()
        new_entry = WhatsAppMessage(field1=message, field2="Risposta del chatbot")  # Modifica field2 con la risposta del chatbot
        session.add(new_entry)
        session.commit()
        session.close()

        return jsonify({"message": "Dati salvati nel database"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()
