import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
import pandas as pd


load_dotenv()

def read_google_sheet(sheet_name):
    spreadsheet_id = os.getenv('GOOGLE_SHEET_ID')

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/spreadsheets.readonly"
    ]

    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

        client = gspread.authorize(creds)

        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

        raw_data = sheet.get_all_values()

        if not raw_data or len(raw_data) <= 1:
            print("No records found in the sheet or the sheet is empty.")
            return pd.DataFrame()

        data = pd.DataFrame(raw_data[1:], columns=raw_data[0])

        return data

    except Exception as e:
        print(f"Error while fetching associated stocks from index: {e}")
        return pd.DataFrame()

def generate_personalized_images(data, folder_name, image_width, image_height, font_size, starting_point, card_tag, regards_color,
                                 name_color, value_color, vertical_spacing):
    try:
        output_folder = f"output_images/{folder_name}"
        img_path = os.getenv('IMAGE_PATH')
        os.makedirs(output_folder, exist_ok=True)

        # Load the font
        font_path = "arialbd.ttf"
        font = ImageFont.truetype(font_path, font_size)

        for index, row in data.iterrows():
            img = Image.open(img_path)
            draw = ImageDraw.Draw(img)

            text_y = image_height - starting_point

            texts = [
                ("Regards", "Regards", regards_color),
                ("Name", str(row['Name']), name_color),
            ]

            if card_tag.lower() == "address" and "Address" in row:
                texts.append(("Address", str(row['Address']), value_color))
            elif card_tag.lower() == "mobile" and "Mobile" in row:
                texts.append(("Mobile", str(row['Mobile']), value_color))

            for label, text, color in texts:
                text_bbox = draw.textbbox((0, 0), text, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_x = (image_width - text_width) / 2
                draw.text((text_x, text_y), text, fill=color, font=font)
                text_y += vertical_spacing

            mobile_number = str(row['Mobile'])
            image_filename = f"output_images/{folder_name}/{mobile_number}.jpg"
            img.save(image_filename)
            print(f"Image saved at: {image_filename}")

    except Exception as e:
        print(f"Error while creating images: {e}")