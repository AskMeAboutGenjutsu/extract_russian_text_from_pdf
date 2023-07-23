from pdf2image import convert_from_path


def pdf_to_image(pdf_path='test2.pdf', jpg_path='images/test_{}.jpg'):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image.save(jpg_path.format(i))
