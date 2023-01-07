import sqlite3
from time import sleep
import database #database.py 필요
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.support.ui import Select
def isCheckDB():
    try:
            con = sqlite3.connect("./db/db.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM main WHERE login == ?;", ("O",))
            check = cur.fetchone()
            con.close()
            if check == None:
                print("계정 등록이 되어 있지 않습니다. 3초뒤 계정 등록 절차로 이동합니다.")
                sleep(3)
                database.SaveAccount() #db 에 패이스북 계정 등록
            else:
                print("계정이 정상적으로 등록 되어있습니다.\n3초뒤 페메 도배 페이지로 이동 합니다.")
                sleep(3)
                main()
    except Exception as e:
        return print("오류 발생")


def MessengerSpam(content,cnt):
        try:
            cnt = int(cnt)
            con = sqlite3.connect("./db/db.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM main WHERE login == ?;", ("O",))
            check = cur.fetchone()
            con.close()
            user = check[0]
            pw = check[1]
            options = webdriver.ChromeOptions()
            #options.add_argument("headless")
            options.add_argument("--start-maximized")
            client = webdriver.Chrome(executable_path=CM().install(), options=options)
            client.set_window_size(1920,1080)
            client.get("https://ko-kr.facebook.com/")
            
            send_em = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="email"]')))
            send_em.send_keys(user)

            sleep(0.3)

            send_pw = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="pass"]')))
            send_pw.send_keys(pw)

            sleep(0.3)

            WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'))).click()

            print(f"Login as {user}")

            sleep(3)

            client.get("https://www.facebook.com/messages/t/")
          

            sleep(3)

            for i in range(1,cnt+1):
                people = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, f'//*[@id="jsc_c_w"]/div/div/div/div/div[2]/div/div[{i}]/div')))
                people.click()

                print("클릭완료")

                sleep(0.4)

                test123 = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')))
                test123.send_keys(content)

                print("작성 완료")
                
                sleep(5)

                send =  WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/span[2]/div')))
                send.click()


            
                print("전송 완료")
                sleep(3)

            input("도배 성공!\n{} 명".format(cnt))
        
        except Exception as e:
            print(e)
            return print("오류가 발생 되었습니다!")




def main():
    content_  = input("보내실 말을 작성 해 주세요 : ")
    cnt_  = int(input("보내실 명수를 적어주세요 (최대 10명) : "))

    if cnt_ > 10:
        input("10명 초과로 인하여 프로그램 종료")
    else:
         SpamRUN = MessengerSpam(content_,cnt_)

if __name__ == "__main__":
    isCheckDB()
