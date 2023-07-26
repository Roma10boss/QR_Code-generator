import qrcode
import cv2
from PIL import Image

# Function to create a QR code image with the provided data and save it to the specified filename
def create_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Function to read a QR code image and extract the data/message from it
def read_qr_code(filename):
    scanner = cv2.QRCodeDetector()
    img = cv2.imread(filename)
    data, _, _ = scanner.detectAndDecode(img)
    return data

# Entry point of the program
if __name__ == "__main__":
    # List of messages for the QR codes
    messages = [
        "QR code 1: Hello, this is QR code 1!",
        "QR code 2: Welcome to QR code 2!",
        "QR code 3: This is QR code 3!",
        "QR code 4: Scanning QR code 4!",
        "QR code 5: Greetings from QR code 5!",
        "QR code 6: You just scanned QR code 6!",
    ]

    # List of filenames to save the generated QR codes
    qr_filenames = ["qr_code_1.png", "qr_code_2.png", "qr_code_3.png", "qr_code_4.png", "qr_code_5.png", "qr_code_6.png"]

    # Generate and save the QR codes for each message
    for i in range(len(messages)):
        create_qr_code(messages[i], qr_filenames[i])
        print(f"QR code {i + 1} generated.")

    # Read each generated QR code and display its message
    for i, qr_filename in enumerate(qr_filenames):
        scanned_data = read_qr_code(qr_filename)
        if scanned_data:
            print(f"Scanned message from QR code {i + 1}: {scanned_data}")
            img = Image.open(qr_filename)
            img.show()  # Display the QR code using PIL
        else:
            print(f"QR code {i + 1} couldn't be read or doesn't contain valid data.")
