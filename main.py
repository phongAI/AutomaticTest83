from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import uuid
import cv2
import pytesseract
import requests
import random
import time
from selenium.webdriver.common.by import By
numberID = [23]
loop = 1000
message = [" Ngày Quốc tế Phụ nữ, chúc em những lời chúc tốt đẹp nhất, luôn xinh đẹp, hạnh phúc và vui vẻ không chỉ vào ngày 8/3 và cả những ngày khác nữa.",
           " Chúc bạn nhận được nhiều quà, nhiều hoa nhiều lời khen và lời chúc của phái nam trong ngày hôm nay. Chúc bạn gặp nhiều may mắn, hạnh phúc, niềm vui và những điều tuyệt diệu trong cuộc sống!",
           " Nhân dịp Quốc tế Phụ nữ, tôi xin được gửi tới tất cả chị em trong công ty lời cảm ơn và lời chúc chân thành nhất. Chúc các chị em luôn xinh đẹp, tươi vui và thành công trên mọi mặt trận. Happy Women’s Day!",
           " Chúc bạn một ngày 8/3 thật vui tươi, tràn ngập hạnh phúc nhé.",
           " Nhân ngày Quốc tế Phụ nữ 8/3 này, tôi chúc các bạn hạnh phúc, sức khỏe, thành công và thịnh vượng!",
           " Tất cả những gì bạn cần làm là mỉm cười. Thật tuyệt vời khi thế giới có bạn. Chúc mừng ngày Quốc tế phụ nữ.",
           " Nhân ngày Quốc tế Phụ nữ 8/3, chúc bạn nhận được nhiều quà, nhiều hoa và nhiều lời chúc tốt đẹp từ mọi người xung quanh.",
           " Chúc các chị em phụ nữ trong cơ quan mãi luôn duyên dáng, xinh đẹp và hạnh phúc bên những người thân yêu trong ngày đặc biệt này.",
           " Chúc bạn có một ngày 8/3 tận hưởng niềm hạnh phúc trọn vẹn bên gia đình và những người thân yêu.",
           " Chúc bạn ngày 8/3 an vui, gặp nhiều may mắn, hạnh phúc và những điều tuyệt vời trong cuộc sống!"
           ]
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def getInfo():
    img = cv2.imread("image.png")
    # img = cv2.resize(img, None, fx=2, fy=2)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adaptive = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 20)
    # print((pytesseract.image_to_string(img)).strip())
    # print((pytesseract.image_to_string(gray)).strip())
    print((pytesseract.image_to_string(adaptive)).strip())

def main():
     # Press ⌘F8 to toggle the breakpoint.
    for y in numberID:
        link_url = "https://events.bhsoft.co/"
        driver.get(f"{link_url}{str(y)}")
        for (index,i) in enumerate(range(loop)):
            name = f"{uuid.uuid4()}"
            result = random.choice(message)
            driver.find_element(By.ID,"message-form").click();
            time.sleep(0.2)
            link_element = driver.find_element(By.XPATH, '//div[contains(@id,"message-form-detail")]/form/div[3]/img')
            link = link_element.get_attribute("src")
            # Save image
            link_element.screenshot(f"Images/image{index}.png")
            driver.refresh()
            # getInfo()
            #
            # driver.find_element(By.ID, "fullname").send_keys(name);
            # driver.find_element(By.ID, "content").send_keys(result);

            # driver.find_element(By.CLASS_NAME,"submitButton").click()
    time.sleep(1)
    driver.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
