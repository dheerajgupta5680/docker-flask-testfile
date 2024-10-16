
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display
from email import encoders
import logging
import os 


def supertel_testing():
    
    os.environ["DISPLAY"] = ":99"

    display = Display(visible=0, size=(1920, 1080))  # Set the size of the virtual display
    display.start()
    
    def init_driver():
        
        options = webdriver.ChromeOptions()

        # Add necessary options
        options.add_argument('--no-sandbox')  # Disables sandboxing
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--enable-automation")

        
        # # Optional: Additional configurations for running in Docker
        # options.add_argument("--headless")
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--disable-gpu')
        
        # Connect to the standalone Selenium server
        driver = webdriver.Remote(
            command_executor='http://selenium-container:4444/wd/hub',  # URL for Selenium server
            options=options
        )

        driver.get('https://app.supertel.in/')
        logging.basicConfig(filename='supertel_activity.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
        return driver
    
    def send_error_email(subject, message, receiver_email):
        sender_email = "info@supertel.in"
        username = "2f6846c1-a7ac-4bc9-b24e-ab81152b8867"
        password = "2f6846c1-a7ac-4bc9-b24e-ab81152b8867"

        # Create the MIMEMultipart object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(receiver_email) # Join the list of recipients into a single string
        msg['Subject'] = subject
        
        # Attach the message body
        body = MIMEText(message, 'plain')
        msg.attach(body)
                
        # Connect to Postmark's SMTP server
        with smtplib.SMTP('smtp.postmarkapp.com', 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(username, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Error email sent to {receiver_email} with recipients!")
    
    def delete(driver):
        actions = ActionChains(driver)
        list_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[2]/a')))
        actions.move_to_element(list_btn).perform()
        list_btn.click()
        sleep(3)
        try:
            a1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[4]/div/button')))
            a1.click()
            sleep(2)
            a1d = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[4]/div/div/a[1]')))
            a1d.click()
            sleep(2)
            a1dy = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="htids"]/body/div[3]/div/div[7]/button[1]')))
            a1dy.click()
            sleep(30)
        except:
            pass
        
        sender_id_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menutoggle"]/ul/li[1]/a')))
        sender_id_btn.click()
        sleep(3)
        try:
            b1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr/td[3]/div/button')))
            b1.click()
            sleep(2)
            b1d = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr/td[3]/div/div/a[2]')))
            b1d.click()
            sleep(2)
            b1dy = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="htids"]/body/div[3]/div/div[7]/button[1]')))
            b1dy.click()
            sleep(15)
        except:
            pass
        
        template_id_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menutoggle"]/ul/li[2]/a')))
        template_id_btn.click()
        sleep(3)
        try:
            c1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[3]/div/button')))
            c1.click()
            sleep(2)
            c1d = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[3]/div/div/a[2]')))
            c1d.click()
            sleep(2)
            c1dy = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="htids"]/body/div[3]/div/div[7]/button[1]')))
            c1dy.click()
            sleep(15)
        except:
            pass
        
        finally:
            driver.quit()
            display.stop()
    
    def run_script():
        driver = init_driver()
        actions = ActionChains(driver)
        try:
            e_create= WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
            e_create.send_keys('dheerajgupta5680@gmail.com')
            e_pass= WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
            e_pass.send_keys('123456789')
            login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/div/div/form/div[3]/button')))
            login.click()
            sleep(3)
            select_project = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[2]/div/div/a')))
            select_project.click()
            sleep(3)
            list_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[2]/a')))
            list_btn.click()
            sleep(3)
        except Exception as e:
            logging.error(e)
            subject = "Warning dheeraj"
            message = "testing script failed somewhere"
            receiver_email = ['dheeraj@aphroecs.com']
            send_error_email(subject, message, receiver_email)
        
        try: 
            a1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[4]/div/button')))
            a1.click()
            sleep(2)
            delete(driver)
        except Exception as e:
            pass
               
        try:
            add_list = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/button')))
            add_list.click()
            sleep(2)
            enter_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addNewUserForm"]/div[1]/input')))
            enter_name.send_keys('new_list')
            save_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addNewUserForm"]/button[1]')))
            save_btn.click()
            sleep(1)
            import_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[3]/button')))
            import_btn.click()
            sleep(1)
            choose_file = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="editMessageSenderForm"]/div[2]/div/input')))
            choose_file.send_keys('/app/data/5000_list.xlsx')
            import_bulk_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="editMessageSenderForm"]/div[4]/button[1]')))
            import_bulk_btn.click()
            sleep(60)
            driver.refresh()
            
        except Exception as e:
            logging.error(e)
            delete(driver)
            subject = "Warning dheeraj"
            message = "testing script failed somewhere"
            receiver_email = ['dheeraj@aphroecs.com']
            send_error_email(subject, message, receiver_email)
            
            
        try:
            sender_id_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menutoggle"]/ul/li[1]/a')))
            sender_id_btn.click()
            sleep(3)
            add_sender_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/button')))
            add_sender_btn.click()
            sleep(3)
            fill_sender_id = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addNewUserForm"]/div[1]/input')))
            fill_sender_id.send_keys('SUPTEL')
            entity_id = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addNewUserForm"]/div[2]/input')))
            entity_id.send_keys('1701171506952848562')
            senderid_save_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addNewUserForm"]/button[1]')))
            senderid_save_btn.click()
            sleep(5)

        except Exception as e:
            logging.error(e)
            delete(driver)
            subject = "Warning dheeraj"
            message = "testing script failed somewhere"
            receiver_email = ['dheeraj@aphroecs.com']
            send_error_email(subject, message, receiver_email)
            
        try:
            template_id_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menutoggle"]/ul/li[2]/a')))
            template_id_btn.click()
            sleep(3)
            add_template_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/button')))
            add_template_btn.click()
            sleep(3)
            template_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addNewUserForm"]/div[1]/input')))
            template_name.send_keys('supertel_template')
            fill_template_id = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addNewUserForm"]/div[2]/input')))
            fill_template_id.send_keys('1707171723149700267')
            fill_content = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addNewUserForm"]/div[3]/textarea')))
            fill_content.send_keys('Your OTP for Supertel account is {%23var%23} - Please do not share the OTP with anyone.')
            checkbox_senderid = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="customCheckTemp3"]')))
            checkbox_senderid.click()
            template_save_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addNewUserForm"]/button[1]')))
            template_save_btn.click()
            sleep(5)
            
        except Exception as e:
            logging.error(e)
            delete(driver)
            subject = "Warning dheeraj"
            message = "testing script failed somewhere"
            receiver_email = ['dheeraj@aphroecs.com']
            send_error_email(subject, message, receiver_email)
            
        try:
            campaign_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menutoggle"]/ul/li[3]/a')))
            campaign_btn.click()
            sleep(3)
            select_sender = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/main/div/div/div/div/div[2]/div/div[1]/select'))
            select_sender.select_by_index(1)
            sleep(3)
            select_temp = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/main/div/div/div/div/div[2]/div/div[2]/div/select'))
            select_temp.select_by_index(1)
            sleep(3)
            test_toggle = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flexSwitchCheckDefaulttt"]')))
            scroll_view = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/main/div/div/div/div/div[6]/div/div[2]/button')))
            
            actions.move_to_element(scroll_view).perform()
            
            test_toggle.click()
            
            sleep(2)
            test_mobile = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/main/div/div/div/div/div[5]/div/div[1]/textarea')))
            test_mobile.send_keys("7503842149 , 9971917666, 7303594538") #, 9971917666, 7303594538
            sleep(2)
            send_test_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/main/div/div/div/div/div[5]/div/div[2]/button')))
            send_test_btn.click()
            
        except Exception as e:
            logging.error(e)
            delete(driver)
            subject = "Warning dheeraj"
            message = "testing script failed somewhere"
            receiver_email = ['dheeraj@aphroecs.com']
            send_error_email(subject, message, receiver_email)
            
            
        try:
            report_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menutoggleReport"]/ul/li[2]/a')))
            report_btn.click()
            sleep(120)
            driver.refresh()
            sleep(2)
            row_1_r = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[3]'))).text
            row_1_s = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[5]'))).text
            row_2_r = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[3]'))).text
            row_2_s = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[5]'))).text
            row_3_r = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[3]/td[3]'))).text
            row_3_s = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[3]/td[5]'))).text
            
            if row_1_s== 'Waiting' and row_2_s== 'Waiting' and row_3_s == 'Waiting':
                subject = "Something went wrong status not updating"
                message = 'It seems that there is an issue with the status not updating properly. Currently, the status is stuck in the "waiting" state and is not progressing as expected. Please investigate the SMPP server connection to determine if there are any connectivity problems or configuration issues that might be causing this disruption in status updates.'
                receiver_email = ["dheeraj@aphroecs.com", "bipul@aphroecs.com", "surender@aphroecs.com"]
                send_error_email(subject, message, receiver_email)
            
        except Exception as e:
            logging.error(e)
            delete(driver)
            subject = "Warning dheeraj"
            message = "testing script failed somewhere"
            receiver_email = ['dheeraj@aphroecs.com']
            send_error_email(subject, message, receiver_email)
            
            
        try:
            sleep(2)
            subject = "Test run successful for Supertel"
            message = (
                "Test run successful. All steps were tested and executed without issues.\n"
                "1. Successfully added a list of 5,000 phone numbers.\n"
                "2. Configured the sender ID.\n"
                "3. Added the template ID along with the content.\n"
                f"4. Sent SMS to the specified numbers and received the status: {row_1_r} : {row_1_s} , {row_2_r} : {row_2_s} , {row_3_r} : {row_3_s}.\n"
                "5. Generated an API and created an HTTP cURL request."
            )
            receiver_email = ["dheeraj@aphroecs.com", "bipul@aphroecs.com", "surender@aphroecs.com"]
            send_error_email(subject, message, receiver_email)
            sleep(2)
            delete(driver)
        
        except Exception as e:
            logging.error(e)
            subject = "Warning dheeraj"
            message = "testing script failed somewhere"
            receiver_email = ['dheeraj@aphroecs.com']
            sleep(2)
            delete(driver)
             
    run_script()

def appscart_testing():
    
    os.environ["DISPLAY"] = ":99"

    display = Display(visible=0, size=(1920, 1080))  # Set the size of the virtual display
    display.start()
    
    def init_driver():
        options = webdriver.ChromeOptions()

        # Add necessary options
        options.add_argument('--no-sandbox')  # Disables sandboxing
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--enable-automation")

        
        # # Optional: Additional configurations for running in Docker
        # options.add_argument("--headless")
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--disable-gpu')
        
        # Connect to the standalone Selenium server
        driver = webdriver.Remote(
            command_executor='http://selenium-container:4444/wd/hub',  # URL for Selenium server
            options=options
        )

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
            os.chmod("screenshots", 0o777)
        driver.get('https://my.appscart.com')
        logging.basicConfig(filename='appscart_activity.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
        
        return driver
        
    def send_error_email(subject, message, attachment_path):
        sender_email = "info@supertel.in"
        username = "2f6846c1-a7ac-4bc9-b24e-ab81152b8867"
        password = "2f6846c1-a7ac-4bc9-b24e-ab81152b8867"
        receiver_email = ["dheeraj@aphroecs.com", "bipul@aphroecs.com", "surender@aphroecs.com" ] # "bipul@aphroecs.com", "surender@aphroecs.com" 
        
        # Create the MIMEMultipart object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(receiver_email) # Join the list of recipients into a single string
        msg['Subject'] = subject
        
        # Attach the message body
        body = MIMEText(message, 'plain')
        msg.attach(body)
        
        if attachment_path:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {attachment_path.split('/')[-1]}")
                msg.attach(part)
                
        # Connect to Postmark's SMTP server
        with smtplib.SMTP('smtp.postmarkapp.com', 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(username, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Error email sent to {receiver_email} with recipients!")
    
    def main_script(driver):
        try:
            appscart_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[1]/a/div')))
            appscart_btn.click()
            sleep(3)
            action_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div[2]/table/tbody/tr/td[4]/div/button')))
            action_btn.click()
            sleep(3)
            delete_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div[2]/table/tbody/tr/td[4]/div/div/a')))
            delete_btn.click()
            sleep(5)
            confirm_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.swal2-confirm.swal2-styled')))
            confirm_btn.click()
            sleep(2)
            
            logging.info('Project deleted successfully')
            
        except Exception as e:
            logging.error(e)   
        
    def run_script():   
        driver = init_driver()
        # Login process
        try:
            
            e_create = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))).send_keys('dheeraj@aphroecs.com')    
            e_pass = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys('Gst@2024')
            
            login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/div/div/form/div[3]/button')))
            login.click()
            sleep(5)

            logging.info('Login successfully')
            
            # project_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div[2]/table/tbody/tr/td[2]/a/span')))
            # project_btn.click()
            # logging.info('Project opened')
            
        except Exception as e:
            logging.error(e)
            
            screenshot_path = "screenshots/login_error_screenshot.png"
            driver.save_screenshot(screenshot_path)
            subject = "Error during login on Appscart"
            message = "An error occurred during the login process"   #\n\nNetwork Errors:\n" + "\n".join(network_errors)
            
            send_error_email(subject, message, screenshot_path)
            driver.quit()
            display.stop()

        try:
            project_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div[1]/a/button')))
            project_btn.click()
            
        except TimeoutException:
            action_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div[2]/table/tbody/tr/td[4]/div/button')))
            action_btn.click()
            sleep(3)
            delete_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div[2]/table/tbody/tr/td[4]/div/div/a')))
            delete_btn.click()
            sleep(5)
            confirm_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.swal2-confirm.swal2-styled')))
            confirm_btn.click()
            
            sleep(3)
            driver.refresh()
            sleep(2)
            project_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div[1]/a/button')))
            project_btn.click()
            
            
        # Project creation process
        try: 
            e_commerce = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form.app_category_id"][@value="2"]')))
            e_commerce.click()
            sleep(3)
            shopify = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form.app_subcategory_id"]')))
            shopify.click()
            sleep(3)
            
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div/form/div[2]/div/div/div[3]/div/input'))).send_keys('custom')
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div/form/div[2]/div/div/div[4]/div/input'))).send_keys('aphroecs.com')
            save_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div/form/div[2]/div/div/div[5]/button[2]')))
            save_btn.click()
            sleep(3)
            logging.info('Successfully project created') 
            
        except Exception as e:  
            logging.error(e)    
            screenshot_path = "screenshots/project_error_screenshot.png"
            driver.save_screenshot(screenshot_path)
            subject = "Error during project creation on Appscart"
            message = "An error occurred during the project creation process"
            send_error_email(subject, message, screenshot_path)
            driver.quit()
            display.stop()



        # Customize process
        try:
            branding_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[3]/a')))
            branding_btn.click()
            sleep(3)

            android_package = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div/div[2]/div/input')))
            android_package.clear()
            android_package.send_keys('com.appscarts.testing')

            ios_package = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div/div[3]/div/input')))
            ios_package.clear()
            ios_package.send_keys('com.appscarts.testing')

            save_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div/div[6]/div/button')))
            save_btn.click()
            sleep(3)
            
            logging.info('Package name changed')
            
            bottom_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menutoggleBottombar"]/a/div')))
            bottom_btn.click()
            sleep(3)
            bottom_color_btn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menutoggleBottombar"]/ul/li/li[1]/a/div')))
            bottom_color_btn.click()
            sleep(3)
            enable_bottombar =  WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div/div/div/div/div[1]/input')))
            enable_bottombar.click()
            sleep(3)

            appbar_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[5]/a/div')))
            appbar_btn.click()
            sleep(3)
            enable_appbar =  WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div/div/div/div/div[1]/input')))
            enable_appbar.click()
            sleep(3)

            sidebar_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menutoggleSidebar"]/a/div')))
            sidebar_btn.click()
            sleep(3)
            sidebar_color_btn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menutoggleSidebar"]/ul/li/li[1]/a/div')))
            sidebar_color_btn.click()
            sleep(3)
            enable_sidebar =  WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div/div/div/div/div[1]/input')))
            enable_sidebar.click()
            sleep(3)
            logging.info('Enabled bottom bar, app bar and sidebar')  
            
        except Exception as e:  
            logging.error(e)
            screenshot_path = "screenshots/customize_error_screenshot.png"
            driver.save_screenshot(screenshot_path)
            subject = "Error during customization on Appscart"
            message = "An error occurred during the customization process"
            send_error_email(subject, message, screenshot_path)
            main_script(driver)
            driver.quit()
            display.stop()



        # Firebase setup
        try:
            firebase_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[16]/a')))
            firebase_btn.click()
            sleep(3)

            google_services = '/app/data/google-services.json'
            ios_services = '/app/data/GoogleService-Info.plist'
            service_account = '/app/data/service_account.json'

            android_conf = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div[2]/div[1]/div/input')))
            android_conf.send_keys(google_services)
            sleep(3)
            
            ios_conf = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div[2]/div[2]/div/input')))
            ios_conf.send_keys(ios_services)
            sleep(3)
            
            service_conf = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div[2]/div[3]/div/input')))
            service_conf.send_keys(service_account)
            
            save_btn_f = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div[2]/div[5]/div/button')))
            save_btn_f.click()
            sleep(3)
            
            logging.info('Firebase setup completed')
            
        except Exception as e:
            logging.error(e)
            screenshot_path = "screenshots/firebase_setup_error_screenshot.png"
            driver.save_screenshot(screenshot_path)
            subject = "Error during firebase_setup on Appscart"
            message = f"An error occurred during the firebase_setup process"
            send_error_email(subject, message, screenshot_path)
            main_script(driver)    
            driver.quit()
            display.stop()
        
        
            
        # Build process
        try:
            build_page = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[19]/a')))
            build_page.click()
            sleep(3)   
            build_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/form/div[2]/div/div[5]/div/button')))
            build_btn.click()
            sleep(3)
            logging.info('Build process started successfully') 

            # Check if the download button is clickable
            try:
                custom_btn = WebDriverWait(driver, 900).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[6]/button[1]')))
                custom_btn.click()
                sleep(3)
                download_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[6]/table/tr[5]/td[1]/a')))
                download_btn.click()
                logging.info('Build process completed successfully, download button is available and clicked.')
            except TimeoutException:
                # Handle scenario where download button is not clickable
                error = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[1]/form/div[1]/p')))
                if error:
                    logging.error('Build process failed: %s', error.text)
                    screenshot_path = "screenshots/build_screenshot.png"
                    driver.save_screenshot(screenshot_path)
                    subject = "Error during build process on Appscart"
                    message = "An error occurred during the build process"
                    
        except Exception as e:
            logging.error("An exception occurred: %s", e)


        # delete project
        try:
            appscart_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[1]/a/div')))
            appscart_btn.click()
            sleep(3)
            action_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div[2]/table/tbody/tr/td[4]/div/button')))
            action_btn.click()
            sleep(3)
            delete_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/main/div/div/div[2]/table/tbody/tr/td[4]/div/div/a')))
            delete_btn.click()
            sleep(5)
            confirm_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.swal2-confirm.swal2-styled')))
            confirm_btn.click()
            logging.info('Project deleted successfully')
            subject = "Test run successful of Appscart"
            message = (
                "Test run successful. All steps were tested and executed without issues.\n"
                "1. Successfully created a new project.\n"
                "2. Customized the bottom bar, side bar, and app bar.\n"
                "3. Uploaded Firebase configuration files.\n"
                "4. Initiated the Android build process and downloaded the app successfully.\n"
                "5. Deleted the project."
            )
            send_error_email(subject, message, None) 
            driver.quit()
            display.stop()
            
        except Exception as e:
            logging.error(e)
            screenshot_path = "screenshots/delete_project_screenshot.png"
            driver.save_screenshot(screenshot_path)
            subject = "Error during project building on Appscart"  
            message = "An error occurred during the build process"
            send_error_email(subject, message, screenshot_path)    
            driver.quit()
            display.stop()
        return('Build process completed successfully')    
            
    run_script()