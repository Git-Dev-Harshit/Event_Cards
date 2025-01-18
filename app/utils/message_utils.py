import os
import requests, json
from app.utils.logger import logger

def create_payload(folder_name, template_id, message):
    try:
        hostname = os.getenv("HOSTNAME")

        payload = {
            "token": os.getenv("TOKEN"),
            "application": os.getenv("APPLICATION_NO"),
            "template_id": template_id,
            "data": []
        }

        folder_path = os.path.join("output_images", folder_name)

        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"):
                number = filename.split(".")[0]
                formatted_number = "91" + number

                media_url = f"{hostname}/{folder_name}/{filename}"

                entry = {
                    "number": formatted_number,
                    "media": media_url,
                    "template_message": [
                        message,
                    ],
                    "language": "en"
                }

                payload["data"].append(entry)

        return payload

    except Exception as e:
        logger.error(f"Error while creating payload: {e}")

def send_whatsapp_message(payload):
    try:
        api_url = os.getenv("API_URL")

        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            logger.info("Message sent successfully!")
            return response.json()
        else:
            logger.info(f"Failed to send message. Status code: {response.status_code}")
            logger.info("Response:", response.text)
            return None

    except Exception as e:
        logger.error(f"Error while sending message: {e}")

