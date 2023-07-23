import cv2
import pytesseract
import glob
from pdf_to_image import pdf_to_image

pdf_to_image()

path = 'images/*.jpg'
image_files = glob.glob(path)


def extract_text_to_txt():
    for image_name in image_files:
        image = cv2.imread(image_name)
        config = ('-l rus --oem 1 --psm 3')
        text = pytesseract.image_to_string(image, config=config)
        text_path = 'text/' + image_name.split('/')[1].split('.')[0] + '.txt'
        with open(text_path, 'w') as file:
            file.write(text)

extract_text_to_txt()


