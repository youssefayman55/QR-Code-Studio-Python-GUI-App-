# QR-Code-Studio-Python-GUI-App-
A modern desktop application built with Python that allows users to generate, manage, and read QR codes using an interactive GUI built with Tkinter.

📌 Project Description

QR Code Studio is a full-featured QR tool that includes:

🔹 QR Code Generator

🔹 QR Code Gallery Manager

🔹 QR Code Reader (Decoder)

🔹 File download & saving system

🔹 Modern tab-based GUI

It is built using Python and provides a simple interface for working with QR codes visually.

🛠️ Tech Stack :

1- Python 🐍

2- Tkinter (GUI) 🖥️

3- qrcode 📦

4- Pillow (PIL) 🖼️

5- pyzbar 📷

📦 Installation:

Install required libraries:

pip install qrcode pillow pyzbar

▶️ How to Run:

1- Save the script as main.py

2- Run it using:
   python main.py

🎯 Features : 

1- 🏗️ QR Code Generator

2- Create QR codes from URLs or text

3- Customize size and border

4- Live preview before saving

5- Download QR code as PNG

🖼️ Gallery System:

1- Save generated QR codes

2- View saved QR codes

3- Delete unwanted items

4- Download from gallery anytime

📷 QR Code Reader:

1- Upload QR image

2- Automatically decode content

3- Display decoded text instantly

💻 Code Overview

The project is structured using OOP:

class QRApp:
    def __init__(self, root):
        ...
Main Modules:

generate_qr() → Creates QR codes

save_to_gallery() → Stores QR images

read_qr() → Decodes QR images

gallery_*() → Manages saved QR codes

📂 Project Structure: 
QR-Code-Studio/

│

├── main.py

├── README.md

└── requirements.txt

📸 UI Overview: 

Tab 1: Generate QR Codes

Tab 2: Gallery Manager

Tab 3: QR Reader

💡 Future Improvements: 

1- 🌐 Web version using Streamlit

2- ☁️ Cloud save for QR gallery

3- 🎨 Custom QR design (logos, colors)

4- 📱 Mobile version (Kivy)

5- 🔐 Encrypted QR codes

⚠️ Notes :

1- Make sure all required libraries are installed

2- pyzbar may require additional system dependencies depending on OS

3- Works best with PNG images

👨‍💻 Author:

Youssef Ayman

Python & AI Developer 🚀
