# text recognition
import cv2
import pytesseract


class Main:
    def get_text_by_image(self,image_path):
        im = cv2.imread(image_path)
        # configurations
        config = ('-l eng --oem 1 --psm 3')
        # pytesseract
        text = pytesseract.image_to_string(im, config=config)
        return text

    def write_to_file(self,text,index):
        with open('results/res'+index+'.txt', 'w') as f:
            f.write(text)
        f.close()

    def __init__(self):
        self.pytesseract = pytesseract.pytesseract
        self.pytesseract.tesseract_cmd = 'tesseract installation/tesseract.exe'
        imgs_paths = ['resources/img/img1.jpg','resources/img/img2.jpg','resources/img/img3.png']
        for i in range(len(imgs_paths)):
            text = self.get_text_by_image(imgs_paths[i])
            print(text)
            self.write_to_file(text,str(i+1))


m = Main()