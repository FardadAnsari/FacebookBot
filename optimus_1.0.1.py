from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep, strftime
from random import randint
import pandas as pd



def read_excel():

    df=pd.read_excel(r'C:\Users\Saba ICT Co\Desktop\pages_id.xlsx')

    shops_name = df['Unnamed: 0']
    shop_ids = df['Unnamed: 1']

    r=shops_name
    t=shop_ids

    return(r,t)


def read_excel():
    
    df = pd.read_excel(r'C:\Users\Saba ICT Co\Desktop\comments.xlsx')

    list_user = []
    list_passwords = []

    list_user = df['Unnamed: 0']
    list_passwords = df['Unnamed: 1']

    x=list_user
    y=list_passwords

    return (x,y)







def kindle_interaction():

    option = Options()
    option.add_argument('--disable-infobars')
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_argument('--headless')

    
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })


    chromedriver_path = 'C:/chromedriver.exe'
    my_webdriver = webdriver.Chrome(chrome_options=option, executable_path=chromedriver_path)



    return my_webdriver



def facebook_fun1(shops_list,account_user,account_pass,comments,my_webdriver):



    print("Hi there, This is optimus V.1.0.1")
    sleep(randint(2, 6))
    
    
    my_webdriver.get("https://mbasic.facebook.com/")
    sleep(randint(2,5))
    print("The page is loading for facebook.....")
    sleep(randint(3,5))
    
    print("Optimus is in Log in page : ...")
    sleep(randint(2,4))
    
    username = my_webdriver.find_element_by_name("email")
    username.send_keys(account_user)
    sleep(randint(2, 6))
    print("Email has been entered.")
    sleep(randint(2, 5))
    password = my_webdriver.find_element_by_name("pass")
    password.send_keys(account_pass)
    print("Password has been entered.")
    sleep(randint(2, 6))
    

    print("I am getting ready for log into your account : ...Loading...")
    login = my_webdriver.find_element_by_name("login")
    login.click()

    print("Great,I'm in")
    print('Optimus plays role as ' + str(account_user)+'.....')
    sleep(12)

   
    OK = my_webdriver.find_element_by_partial_link_text("Now")
    OK.click()
    print("Optimus asked for Notification option , Not Now has been Chosed.")

    
    current_url=my_webdriver.current_url
    sleep(3)
    print("Clicking on Home Button")

    if current_url=='https://mbasic.facebook.com/gettingstarted/?_rdr':
        next_button=my_webdriver.find_element_by_link_text('Next')
        next_button.click()

    else:
        sleep(randint(8,10))
        home_button=my_webdriver.find_element_by_link_text('Home')
        home_button.click()
        print("Let's first have interaction with your own page ...")
        sleep(randint(6,9))
        for time in range(0, 3):
            sleep(4)
            my_webdriver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            print("Scrolling Down to see more posts ")
            sleep(3)
            morebutton = my_webdriver.find_element_by_partial_link_text('tories')
            sleep(2)
            morebutton.click()
            sleep(randint(2, 6))
        print("Optimus has skipped some posts....")

# Interaction with normal post
    for step in range(0,5):
        print("Found something from your feed...")
        fullstory = my_webdriver.find_elements_by_link_text('Full Story')
        fullstory[step].click()
        print("Clicked on Full story")
        sleep(3)
        like = my_webdriver.find_element_by_link_text('Like')
        like.click()
        print("Optimus liked it")
        sleep(randint(2, 5))
        my_webdriver.back()
        sleep(3)
        my_webdriver.back()
        sleep((randint(2, 5)))
        print("Start again I will like and share some of your posts again")

    sleep(randint(14,20))



# interaction with shops' posts
# should add script for checking comments here for each shop

    for i in range(0,len(shops_list)):
        my_webdriver.get('https://mbasic.facebook.com/'+shops_list[i])
        print('Optimus is in '+ str(shops_list[i]) + '!')
        sleep(randint(10,14))
        first_post=my_webdriver.find_element_by_link_text("Full Story")
        first_post.click()
        print('I am start interacting with ' + shops_list[i]+ ' first post !')
        sleep(randint(5,8))
        like=my_webdriver.find_element_by_link_text("Like")
        color=like.get_attribute('style')
        if len(color)==0:
            print("It has not been liked ... So I liked it...")
            like.click()
        else:
            print("It has been liked...So would got for next takeaway....")
            sleep(randint(4,5))
            my_webdriver.back()
            continue
        sleep(randint(4,7))
        comment_aria = my_webdriver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[5]').text
        text_all = comment_aria.splitlines()
        comment_box=my_webdriver.find_element_by_name("comment_text")
        while True:
            print("I want to leave comment....")
            x=randint(0,len(comments)-1)
            new_comment=comments[x]
            if new_comment not in text_all:
                comment_box.send_keys(comments[x])
                my_webdriver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[4]/form[1]/table/tbody/tr/td[2]/div/input").click()
                print("I left comment ...\n" + str(comments[x])+ "\n was my comment")
                break
            else: continue


        sleep((randint(2,5)))
    print('Operation is up with '+ str(account_user))
    print("Logged Out from "+ str(account_user))
    print("--------------------------------------")
    my_webdriver.close()

##-------------------------Main--PART-------------------------------------------------------------------------------------



#from optimus import facebook_fun1
#from optimus import kindle_interaction
from random import randint
from time import sleep
import pandas as pd







def read_excel(path):
    files = pd.read_excel(path)
    return files

my_df = read_excel('c:\MYLIST.xlsx')

My_comments=pd.read_excel('c:\COM.xlsx')

comments=My_comments['Comments'].tolist()

shops_name = my_df["Shops' name"].tolist()

shops_id = my_df["Facebook Ids"].tolist()

#comments=my_df["Comments"].tolist()

user = my_df['User'].tolist()

password = my_df['Pass'].tolist()

comments=comments[0:100]

user=user[0:6]

password=password[0:6]

for i in range(0,len(user)-1):
    my_surf=kindle_interaction()
    sleep(10)
    facebook_fun1(shops_id,user[i],password[i],comments,my_surf)
    sleep(10)

print("All the intractions has been done, you can close this tab now.GoodBye")

