import cv2
import numpy as np

# Enter the path to the image
IMAGE_PATH = "./ada.jpg" 

# Path of dice images. Dice images must be one-dimensional matrix.
# In this case (7, 7, 1)
dice_1 = cv2.cvtColor(cv2.imread("./dice/dice_1.png"), cv2.COLOR_BGR2GRAY)
dice_2 = cv2.cvtColor(cv2.imread("./dice/dice_2.png"), cv2.COLOR_BGR2GRAY)
dice_3 = cv2.cvtColor(cv2.imread("./dice/dice_3.png"), cv2.COLOR_BGR2GRAY)
dice_4 = cv2.cvtColor(cv2.imread("./dice/dice_4.png"), cv2.COLOR_BGR2GRAY)
dice_5 = cv2.cvtColor(cv2.imread("./dice/dice_5.png"), cv2.COLOR_BGR2GRAY)
dice_6 = cv2.cvtColor(cv2.imread("./dice/dice_6.png"), cv2.COLOR_BGR2GRAY)

# Dice images pixel size. All dice images are square
ratio = 7

class GetImage():
    
    def __init__(self, path, display = False):
        self.img = cv2.imread(path)
        
        if display:
            cv2.imshow("Image", self.img)

    def prep_img(self, display = False):
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        x, y = self.gray.shape[0], self.gray.shape[1]
        
        if x % ratio != 0:
            self.width = x - (x % ratio)
        else:
            self.width = x

        if y % ratio != 0:
            self.height = y - (y % ratio)
        else:
            self.height = y
            
        self.cropped = self.gray[0:self.width, 0:self.height]
        
        if display:
            cv2.imshow("Gray & Cropped Image", self.cropped)
            
        return self.cropped

class CreateDice():
    
    def __init__(self, prepared_img, save_img = False, display = True) -> None:
        self.prepared_img = prepared_img
        self.width = prepared_img.shape[0]
        self.height = prepared_img.shape[1]
        self.blank = np.zeros((self.width, self.height), np.uint8)
        self.dice_img = self.create_dice_img()
        
        if display:
            cv2.imshow("Dice Image", self.dice_img)
        if save_img:
            cv2.imwrite("Dice_Image.png", self.dice_img)

    def create_dice_img(self):
        for i in range(0, self.width, ratio):
            for j in range(0, self.height, ratio):
                temp_img = self.prepared_img[i:i+ratio, j:j+ratio]
                sum = np.sum(temp_img)
                if sum <= 2000:
                    self.blank[i:i+ratio, j:j+ratio] = dice_1
                elif 2000 < sum <= 4000:
                    self.blank[i:i+ratio, j:j+ratio] = dice_2
                elif 4000 < sum <= 6000:
                    self.blank[i:i+ratio, j:j+ratio] = dice_3
                elif 6000 < sum <= 8000:
                    self.blank[i:i+ratio, j:j+ratio] = dice_4
                elif 8000 < sum <= 10000:
                    self.blank[i:i+ratio, j:j+ratio] = dice_5
                elif 10000 < sum:
                    self.blank[i:i+ratio, j:j+ratio] = dice_6
                else:
                    print("Something went wrong!")
                    quit()
        return self.blank

if __name__ == "__main__":
    img = GetImage(IMAGE_PATH, display=True)
    prepared_img = img.prep_img(display=False)
    dice_img = CreateDice(prepared_img, save_img=False, display=True)
    cv2.waitKey(0)
    
