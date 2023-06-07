def timetable() :
    import selenium.webdriver.support.select
    import time
    import re
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    from bs4 import BeautifulSoup
    url = "https://cas.unikl.edu.my/cas-web/login?service=http%3A%2F%2Fonline1.unikl.edu.my%2Fj_spring_cas_security_check%3Fspring-security-redirect%3D%2Ftimetable.htm"

    userid = open('userid.txt','r')
    passid = open('passid.txt','r')

    opt = Options()
    opt.add_argument("-headless")

# with webdriver.Firefox(options=opt) as driver:
    try :
        driver = webdriver.Firefox(options=opt)
        driver.get(url)

        uname = driver.find_element(By.ID, "username")
        uname.send_keys(userid.read())
        passw = driver.find_element(By.ID, "password")
        passw.send_keys(passid.read())
        driver.find_element(By.NAME, "submit2").click()

        userid.close()
        passid.close()
# driver.quit()

# driver = webdriver.Firefox(options=opt)
        driver.get("https://online1.unikl.edu.my/timetable.htm")

        se = Select(driver.find_element(By.ID, "selSemester"))
        se.select_by_value('2022/2023-2')
# driver.find_element(By.VALUE, "View").click()

# time.sleep(5)

# driver.get("https://online1.unikl.edu.my/timetable.htm")

        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

#.find_element(By.XPATH, "//input[@id='passwd-id']")
        '''
        rawData = soup.find('table', id="timetable")
        rawTable = rawData.find('tbody')

        timetable = {}

        for rawTT in rawTable
        '''


        rawData = soup.find('table', id="timetable")

#rawTable = rawData.find('tbody').get_text(strip=True)
        rawTable = rawData.find('tbody')

        counter = 0

        for row in rawTable.find_all('tr') :
            if counter == 0 :
                print("\n++++++++++++++++++++++++++++++\n                        MONDAY\n++++++++++++++++++++++++++++++")
            elif counter == 1 :
                print("\n++++++++++++++++++++++++++++++\n                       TUESDAY\n++++++++++++++++++++++++++++++")
            elif counter == 2:
                print("\n++++++++++++++++++++++++++++++\n                     WEDNESDAY\n++++++++++++++++++++++++++++++")
            elif counter == 3 :
                print("\n++++++++++++++++++++++++++++++\n                      THURSDAY\n++++++++++++++++++++++++++++++")
            elif counter == 4 :
                print("\n++++++++++++++++++++++++++++++\n                        FRIDAY\n++++++++++++++++++++++++++++++")
            else :
                break

            timeStamp = 8

            for row2 in row.find_all('td', class_="inputBgColor") :
                timeStr = str(timeStamp)
                if row2.get_text(strip=True) == None :
                    pass
                else :
                    print(timeStr+":30\n"+row2.get_text(strip=True)+"\n..............................")
                    timeStamp+=1

            counter+=1

    except :
        print("Error occured!\nTips : Type 'unikllogin username password' to insert your credentials if you don't have yet.")

    driver.quit()


def login() :
    import sys

    userid = sys.argv[1]
    passid = sys.argv[2]

    useridText = open('userid.txt','w')
    useridText.write(userid)
    useridText.close()

    passidText = open('passid.txt','w')
    passidText.write(passid)
    passidText.close()


if __name__ == "__main__":
    timetable()
