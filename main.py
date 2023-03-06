from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import uuid
import random
import time
from selenium.webdriver.common.by import By
numberID = [23,6,21,17]
loop = 5
message = ["Ngày Quốc tế Phụ nữ, chúc em những lời chúc tốt đẹp nhất, luôn xinh đẹp, hạnh phúc và vui vẻ không chỉ vào ngày 8/3 và cả những ngày khác nữa.",
           "Chúc bạn nhận được nhiều quà, nhiều hoa nhiều lời khen và lời chúc của phái nam trong ngày hôm nay. Chúc bạn gặp nhiều may mắn, hạnh phúc, niềm vui và những điều tuyệt diệu trong cuộc sống!",
           "Nhân dịp Quốc tế Phụ nữ, tôi xin được gửi tới tất cả chị em trong công ty lời cảm ơn và lời chúc chân thành nhất. Chúc các chị em luôn xinh đẹp, tươi vui và thành công trên mọi mặt trận. Happy Women’s Day!"
           ]
message1 = [" Chúc bạn một ngày 8/3 thật vui tươi, tràn ngập hạnh phúc nhé.",
            "Nhân ngày Quốc tế Phụ nữ 8/3 này, tôi chúc các bạn hạnh phúc, sức khỏe, thành công và thịnh vượng!",
            "Tất cả những gì bạn cần làm là mỉm cười. Thật tuyệt vời khi thế giới có bạn. Chúc mừng ngày Quốc tế phụ nữ."]
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def main():
     # Press ⌘F8 to toggle the breakpoint.
    for y in numberID:
        link_url = "https://events.bhsoft.co/"
        driver.get(f"{link_url}{str(y)}")
        for i in range(loop):
            name = f"{uuid.uuid4()}"
            sequence1 = random.choice(message)
            sequence2 = random.choice(message1)
            randomIndex = random.choice([0,1])
            if randomIndex == 0:
                result = sequence1+sequence2
            else:
                result = sequence2 + sequence1

            driver.find_element(By.ID,"message-form").click();
            driver.find_element(By.ID, "fullname").send_keys(name);
            driver.find_element(By.ID, "content").send_keys(result);
            driver.find_element(By.CLASS_NAME,"submitButton").click()
    time.sleep(2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
