import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service


timeout = 3

def home():
    driver = webdriver.Chrome(
    executable_path="C:\\Users\\ssawai\\Downloads\\chromedriver_win32\\chromedriver.exe"
    )
    driver.get("http://localhost:3000")
    return driver

def login(driver,email,password):
    email_field = driver.find_element(By.XPATH, '(//input[@id="outlined-basic"])[1]')
    email_field.send_keys(email)
    # time.sleep(timeout)
    password_field = driver.find_element(By.XPATH, '(//input[@id="outlined-basic"])[2]')
    password_field.send_keys(password)
    time.sleep(timeout)
    login_button = driver.find_element(By.XPATH, '//button')
    login_button.click()


def search(driver,text):
    time.sleep(timeout)
    search_field = driver.find_element(By.XPATH, '//input')
    search_field.send_keys(text)
    time.sleep(timeout)

    # arr_elements = driver.find_elements(By.XPATH,'//div[@data-field="name" and @role="cell"]/div')
    # names = [i.text for i in arr_elements]


    arr_elements = []

    for _ in range(3):
        characters = driver.find_elements(By.XPATH, '//div[@data-field="name" and @role="cell"]/div')

        for i in characters:
            if i.text not in arr_elements:
                arr_elements.append(i.text)
        
        # arr_elements.extend([i.text for i in characters])
        # print(names)
        # arr_elements.extend(characters)

        last_element = characters[-1]
        driver.execute_script("arguments[0].scrollIntoView(true);", last_element)
        time.sleep(1)

    # names = [i.text for i in arr_elements]
    # for character in names:
    #     assert text.lower() in character.lower(), f"Search term '{text}' not found in '{character}'"

    # for _ in range(3):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(1)
    # updated_list = driver.find_elements(By.XPATH,'//div[@data-field="name" and @role="cell"]/div')
    print(arr_elements,len(arr_elements))
    return arr_elements
    # print(last_element.text)

def is_sorted(names, ascending=True):
    sorted_names = sorted(names)
    if not ascending:
        sorted_names = sorted(names, reverse=True)
    
    return names == sorted_names

def scroll_to_top(driver):
    action = ActionChains(driver)
    print("Scrolling to top")
    while True:
        for_parent_of_first = driver.find_elements(By.XPATH, "//div[@data-rowindex = '1']")
        res = driver.find_elements(By.XPATH, '//div[@data-field="name"]/div[text()]')
        action.scroll_to_element(res[0]).perform()
        if for_parent_of_first:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "1"]/div[@data-field="name"]/div[text()]')
            break
        time.sleep(2)
    time.sleep(timeout)

def sort_list(driver, char_list,flag):
    sort_button = driver.find_element(By.XPATH,'(//button[@title="Sort"])[1]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()

    all_elements = []

    for _ in range(3):
        characters = driver.find_elements(By.XPATH, '//div[@data-field="name" and @role="cell"]/div')

        for i in characters:
            if i.text not in all_elements:
                all_elements.append(i.text)

        last_element = characters[-1]
        driver.execute_script("arguments[0].scrollIntoView(true);", last_element)
        time.sleep(2)
    
    if char_list == all_elements and flag:
        print("ascending sort validated")
    elif char_list == all_elements and not flag:
        print("descending sort validated")
    else:
        print("not valid")
    # while True:
    #     elements = driver.find_elements(By.XPATH,'//div[@data-field="name" and @role="cell"]/div')
    #     top_element = elements[0]
    #     driver.execute_script("arguments[0].scrollIntoView();", top_element)
    #     all_elements.extend(elements)

    #     driver.execute_script("window.scrollTo(0, 0);")
    #     time.sleep(3)

    #     if driver.execute_script("return window.scrollY;") == 0:
    #         break
    


email= "abc@gmail.com"
password= "foasnfsda@2023"
text="Rick"
driver = home()
login(driver,email,password)
char_list = search(driver,text)
scroll_to_top(driver)
char_list.sort()
flag=True
sort_list(driver,char_list,flag)
scroll_to_top(driver)
char_list.sort(reverse=True)
sort_list(driver,char_list,not flag)
# sort_button = driver.find_element(By.XPATH,'(//button[@title="Sort"])[1]')
# clicks=0

# while clicks <3:
#     driver.implicitly_wait(5)
#     ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
#     # sort_button.click()
#     time.sleep(timeout)
#     if clicks == 0:
#         asc_result = is_sorted(char_list)
#         if asc_result:
#             print("Correctly sorted")
#         else:
#             print("Not correct")
#     elif clicks == 1:
#         desc_result = is_sorted(char_list,ascending=False)
#         if desc_result:
#             print("Correct")
#         else:
#             print("Wrong sort")
#     else:
#         print("complete")

#     clicks+=1