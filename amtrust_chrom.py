"""
Filename:
    filename.py

Description:
    Enter description here....

Author(s):
    Jonathan Jang
    Hanbi Hanz Choi


Solomon Insurance Group
"""
import os
import re
# from selenium.webdriver import Firefox
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # chrome service
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService # chrome service
from webdriver_manager.chrome import ChromeDriverManager# chrome service
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import mysql.connector
import csv
import time
import carrier_PDF_Automation
driver =webdriver.Firefox()


def amtrust(file_path, download_path):
    # The different accounts:
    accounts_dict = {

        # "1017950001": "Creative1!", #Problem
        # "iuagency": "217-04Northern", #problem




        "IUA48995": "Bayside#5", #1
        "agt58310": "Solo2009", #2
        #"agt159800": "IuaWin2020" #3



        # NOTE:: agt157041 --> ENS LOGIN -- will not update, and Korea Processing will do manually
        # "agt157041": "Iua2018!",
        # NOTE:: M7295 is a Virgina
        # "M7295": "M7295" #problem
    }

    dict_keys = list(accounts_dict)

    table_header_list = []

    for username, password in accounts_dict.items():
        # TODO: CHANGED TO FIREFOX BECAUSE OF A REDIRECT ISSUE WITH CHROME
        # Changing the default download directory to my designated path
        #    0 means to download to the desktop,
        #    1 means to download to the default "Downloads" directory,
        #    2 means to use the directory
        # firefox_options = Options()
        # firefox_options.set_preference("browser.download.folderList", 2)
        # firefox_options.set_preference("browser.helperApps.alwaysAsk.force", False)
        # firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        # firefox_options.set_preference("browser.download.dir", download_path)
        # firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        # firefox_options.set_preference("pdfjs.disabled", True)
        


        # service = Service(r'C:\Processing_Automation\Automation\PDF_Download_Selenium_1\geckodriver.exe')
        # time.sleep(5)
        # browser = Firefox(service=service, options=firefox_options)
        # time.sleep(3)
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")

        # create instance of Chrome webdriver
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        # create instance of Firefox webdriver
        # browser = webdriver.Firefox(
        #     executable_path='C:\Processing_Automation\Automation\PDF_Download_Selenium_1\geckodriver.exe',
        #     firefox_profile=firefox_options)
        # browser.maximize_window()


        # Open website -- Amtrust
        # browser.get("https://ao.amtrustgroup.com/")

        #comment out for testing
        url = "https://ao.amtrustgroup.com/"
        browser.implicitly_wait(10)
        browser.execute_script(f"location.href='{url}';")


        time.sleep(3)

        print(f"START of loop! username: {username}")
        time.sleep(3)
        # Enter Username & Password Info
        browser.find_element(By.ID, "UsernameTextBox").send_keys(username)
        time.sleep(3)
        browser.find_element(By.ID, "PasswordTextBox").send_keys(password)
        time.sleep(3)
        browser.find_element(By.ID, "LoginButton").click()
        time.sleep(3)
        print("logging in")
        # Will sleep until the page is ready to go on to the next portion
        # check_for_element = True
        # while check_for_element:
        #     try:
        #         user_agreement = browser.find_element(By.XPATH,
        #                                               "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-user-agreement/"
        #                                               "amt-user-agreement/div/div[2]/h4").text
        #         print("test1")
        #         if "USER AGREEMENT" in user_agreement:
        #             # Checking the "I have read and agree to the Terms & Conditions" check box
        #             browser.find_element(By.XPATH,
        #                                  "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-user-agreement/"
        #                                  "amt-user-agreement/div/div[2]/div[4]/div/div[3]/div/mat-checkbox/label/span[1]").click()
        #             time.sleep(1)
        #             # Click the Accept Button
        #             browser.find_element(By.XPATH,
        #                                  "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-user-agreement/"
        #                                  "amt-user-agreement/div/div[4]/div[2]/button").click()
        #             time.sleep(2)
        #     except NoSuchElementException:
        #         try:
        #             # Looking to see if the "Recent Policy Documents" exists
        #             # browser.find_element(By.XPATH,
        #             #"/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[2]/mat-tab-group/"
        #             #"mat-tab-header/div[2]/div/div/div[3]")
        #             browser.find_element(By.ID, "mat-tab-label-0-2").click()
        #             print("Page after login is ready!")
        #             check_for_element = False
        #         except NoSuchElementException:
        #             print("test2")
        #             # check_for_element = False
        #             time.sleep(1)

        # Create new path for clicking "Recent Policy Documents" 9/8/2023
        # time.sleep(3)
        # browser.find_element(By.ID, "mat-tab-label-0-2").click()
        #
        # time.sleep(3)
        #
        # check_for_element = True
        #
        # while check_for_element:
        #     try:
        #         browser.find_element(By.XPATH,
        #                              "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[2]/"
        #                              "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/div/"
        #                              "amt-tab-body[1]/div/app-document-table/div/div[2]/mat-table/mat-header-row/mat-header-cell[1]")
        #         check_for_element = False
        #
        #     except NoSuchElementException:
        #         print("loop escape")
        #

        # Will sleep until the page is ready to go on to the next portion
        check_for_element = True
        while check_for_element:
            try:
                browser.find_element(By.XPATH,
                                     "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-user"
                                     "-agreement/"
                                     "amt-user-agreement/div/div[2]/div[4]/div/div[3]/div/mat-checkbox/label/span[1]").click()
                time.sleep(1)
                # Click the Accept Button
                browser.find_element(By.XPATH,
                                     "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-user"
                                     "-agreement/"
                                     "amt-user-agreement/div/div[4]/div[2]/button").click()
                time.sleep(2)

            except NoSuchElementException:
                try:
                    print("next page")
                    # Looking to see if the "Recent Policy Documents" exists
                    browser.find_element(By.ID, "mat-tab-label-0-2")

                    print("Page after login is ready!")
                    check_for_element = False
                except NoSuchElementException:
                    time.sleep(1)

        # Clicking the "Recent Policy Documents"
        browser.find_element(By.ID, "mat-tab-label-0-2").click()
        print("click Recent Policy")
        # driver.execute_script("document.getElementsByClassName('chat-bot_icon')[0].remove()")
        check_for_element = True
        while check_for_element:
            try:
                print("check1")

                browser.find_element(By.XPATH,
                                     "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div["
                                     "3]/mat-tab-group/div/mat-tab-body["
                                     "3]/div/app-recent-documents/amt-vertical-tab-group/amt-tab-header")
                check_for_element = False
            except NoSuchElementException:
                print("check 2")
                time.sleep(1)

        print("check escape while loop")

        num_of_type_of_activity = browser.find_elements(By.XPATH,
                                             "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app"
                                             "-home/div[3]/mat-tab-group/div/mat-tab-body["
                                             "3]/div/app-recent-documents/amt-vertical-tab-group/amt-tab-header/div"
                                             "/div/div/div")

        print(len(num_of_type_of_activity))
        for type_of_activity in range(1, len(num_of_type_of_activity) + 1):
            # Click the "type of activity"
            # print("test1 in for loop")
            name_of_activity = browser.find_element(By.XPATH,
                                                    "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/mat-tab-group/div/"
                                                    "mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/amt-tab-header/div/div/div/div[" +
                                                    str(type_of_activity) + "]")
            # print(type_of_activity)
            # driver.execute_script("arguments[1].scrollIntoView();", name_of_activity)
            # name_of_activity = WebDriverWait(driver, 10).until(
            #    EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/mat-tab-group/div/"
            #                                        "mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/amt-tab-header/div/div/div/div[0]")))
            name_of_activity.click()

            print(f"\tCurrent Type of Policy Doc Type: \t{name_of_activity.text}")

            # Skipping these three types of activities
            if "Claimant Setup" in name_of_activity.text or "Second Request Audit" in name_of_activity.text or \
                    "Partial Information Audit" in name_of_activity.text:
                pass
            else:
                # Checking for the table to load or checking to see if there are no results found
                check_for_element, check_for_results = True, False
                while check_for_element:
                    table_div = browser.find_element(By.XPATH, "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/mat-tab-group/"
                        "div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/div/amt-tab-body[" + str(type_of_activity) + "]/div/app-document-table/div/div[2]")
                    print("table check")
                    time.sleep(3)
                    if table_div.is_displayed():
                        print("Table was found")
                        check_for_element = False
                    else:
                        no_results_found = browser.find_element(By.XPATH,
                                                                "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/"
                                                                "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/div/"
                                                                "amt-tab-body[" + str(type_of_activity) + "]/div/app-document-table/div/mat-error")
                        #
                        # no_results_found = browser.find_element(By.ID,"mat-error-36")
                        time.sleep(3)
                        if no_results_found.is_displayed():
                            print("element not hidden")
                            no_results_found = "No Results found for -->" + name_of_activity.text

                            # Writing the row to the Amtrust CSV
                            pdf_download_bool = open(file_path + "00_Amtrust.csv", "a", encoding="UTF8", newline="")
                            writer = csv.writer(pdf_download_bool)
                            writer.writerow([no_results_found + "; Username: " + username])
                            pdf_download_bool.close()

                            # Writing the row to the Amtrust CSV that will be sent via email
                            pdf_download_email = open(file_path + "00_Amtrust_Email.csv", "a", encoding="UTF8",
                                                      newline="")
                            writer = csv.writer(pdf_download_email)
                            writer.writerow([no_results_found + "; Username: " + username])
                            pdf_download_email.close()

                            check_for_results = True
                            check_for_element = False
                        else:
                            print("element hidden")
                            time.sleep(1)

                # depending on the results from the while loop above, if there are no results it will pass, else it
                # will attempt download the PDF
                if check_for_results:
                    pass
                else:
                    if type_of_activity == 1 and username == list(accounts_dict.keys())[0]:
                        # Getting the header info
                        header = browser.find_elements(By.XPATH,
                                                       "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[2]/"
                                                       "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/div/"
                                                       "amt-tab-body[1]/div/app-document-table/div/div[2]/mat-table/mat-header-row/"
                                                       "mat-header-cell")
                        for head_index in range(1, len(header) + 1):
                            if head_index != 5:
                                header_text = browser.find_element(By.XPATH,
                                                                   "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[2]/"
                                                                   "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/"
                                                                   "div/amt-tab-body[" + str(
                                                                       type_of_activity) + "]/div/app-document-table/div/div[2]/"
                                                                                           "mat-table/mat-header-row/mat-header-cell[" + str(
                                                                       head_index) + "]/div/div[1]").text
                                if "File" not in header_text:
                                    table_header_list.append(header_text)
                        table_header_list += ["Username", "ScriptRunDate", "DownloadedPDF", "DatePDFDownloaded"]
                        print(f"Header Table: {table_header_list}")
                        # Taking the Header HTML Table and adding it to a list then writing to file
                        pdf_download_bool = open(file_path + "00_Amtrust.csv", "a", encoding="UTF8", newline="")

                        writer = csv.writer(pdf_download_bool)

                        writer.writerow(table_header_list)

                        pdf_download_bool.close()

                        time.sleep(3)
                        # Writing the header row to the Amtrust CSV that will be sent via email
                        pdf_download_email = open(file_path + "00_Amtrust_Email.csv", "a", encoding="UTF8",
                                                  newline="")
                        writer = csv.writer(pdf_download_email)
                        writer.writerow(table_header_list)
                        pdf_download_email.close()

                        time.sleep(4)
                        # Closing the assist help box
                        # browser.find_element_by_id("js-chat-text_close").click()
                        # time.sleep(0.5)

                    try:
                        browser.find_element(By.ID, "js-chat-text_close").click()
                        time.sleep(3)
                    except ElementNotInteractableException:
                        # print("Could not close the help chat box popup window")
                        time.sleep(3)
                    print("error88")
                    # Click the "Date Generated" twice to make sure that we are looking at the most recent docs / rows
                    for i in range(2):
                        browser.find_element(By.XPATH,
                                             "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/"
                                             "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/div/"
                                             "amt-tab-body[" + str(
                                                 type_of_activity) + "]/div/app-document-table/div/div[2]/mat-table/"
                                                                     "mat-header-row/mat-header-cell[6]/div").click()
                        print("click1")
                        time.sleep(1)

                    print("before nextpagebool")
                    next_page_bool = True
                    while next_page_bool:
                        num_body_rows = browser.find_elements(By.XPATH,
                                                              "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/"
                                                              "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/div/"
                                                              "amt-tab-body[" + str(
                                                                  type_of_activity) + "]/div/app-document-table/div/div[2]/"
                                                                                      "mat-table/mat-row")

                        print("check body rows")
                        num_body_cols = browser.find_elements(By.XPATH,
                                                              "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/"
                                                              "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/div/"
                                                              "amt-tab-body[" + str(
                                                                  type_of_activity) + "]/div/app-document-table/div/div[2]/"
                                                                                      "mat-table/mat-row[1]/mat-cell")

                        print("check body cols")
                        for each_body_row in range(1, len(num_body_rows) + 1):
                            each_row_list = []
                            agent_id = ""
                            PolicyEffectiveDate = ""
                            TransactionTypeFromSolomon = ""
                            time_pdf_download = ""
                            Automation_DownloadPhaseCompleted = "False"
                            Time_Download_PhaseComplete = ""
                            DownloadStatus_AgentCopy = ""
                            DownloadFile_AgentCopy_Location = ""
                            DownloadStatus_InsuredCopy = "False"
                            DownloadFile_InsuredCopy_Location = ""
                            Automation_ProcessPhaseCompleted = "False"
                            Time_Process_PhaseComplete = ""
                            Automation_AttachPhaseCompleted = "False"
                            Time_AttachToEpic_PhaseComplete = ""
                            # Either "Fail", "Pending", "Success"
                            AutomationStatus = "Pending"
                            TimeOf_FailOrComplete = ""
                            LogComments = ""
                            DownloadFile_Agent_Size = "0"
                            DownloadFile_Insured_Size = "0"
                            DatePDFDownloaded = ""

                            # # All of the items in the row
                            # each_body_row_text = browser.find_element_by_xpath(
                            #     "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[2]/"
                            #     "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/div/"
                            #     "amt-tab-body[" + str(type_of_activity) + "]/div/app-document-table/div/div[2]/"
                            #     "mat-table/mat-row[" + str(each_body_row) + "]").text
                            # each_row_list = each_body_row_text.split("\n")
                            # each_row_list += [username]

                            date_generated = browser.find_element(By.XPATH,
                                                                  "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/"
                                                                  "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/"
                                                                  "div/amt-tab-body[" + str(
                                                                      type_of_activity) + "]/div/app-document-table/div/div[2]/"
                                                                                          "mat-table/mat-row[" + str(
                                                                      each_body_row) + "]/mat-cell[6]").text
                            date_gen_col_year = datetime.strptime(date_generated, '%b %d, %Y').strftime("%Y")

                            if date_gen_col_year == str(datetime.now().year) or \
                                    date_gen_col_year == str(datetime.now().year - 1):
                                for each_body_col in range(1, len(num_body_cols) + 1):
                                    each_col_element = browser.find_element(By.XPATH,
                                                                            "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/"
                                                                            "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/"
                                                                            "div/amt-tab-body[" + str(
                                                                                type_of_activity) + "]/div/app-document-table/div/div[2]/"
                                                                                                    "mat-table/mat-row[" + str(
                                                                                each_body_row) + "]/mat-cell[" + str(
                                                                                each_body_col) +
                                                                            "]")
                                    if each_body_col != 5:
                                        each_row_list.append(each_col_element.text)
                                    # if each_body_col == 6:
                                    #     date_generated = each_col_element.text
                                each_row_list += [username]

                                # Check for when type_of_activity == Return Mail
                                # if "Return Mail" in name_of_activity.text and "Policy Return Mail" in each_row_list[1]:
                                #     each_row_list.insert(1, "BLANK INSURED - " + each_row_list[0])
                                if "Return Mail" in name_of_activity.text and "Policy Return Mail" in each_row_list[
                                    2] and \
                                        "" in each_row_list[1]:
                                    each_row_list[1] = "BLANK INSURED - " + each_row_list[0]
                                # print(each_row_list)
                                time.sleep(1)

                                # Perform a check to see if the download already exists (aka check the db with the row
                                check_if_exist = sql_connector_check_amtrust([each_row_list])
                                skipped_download_bool = ""
                                time.sleep(2)
                                # If True, then attempt download
                                if check_if_exist[0]:
                                    # Clicking on the PDF icon button at index 5
                                    browser.find_element(By.XPATH,
                                                         "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/"
                                                         "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/"
                                                         "div/amt-tab-body[" + str(
                                                             type_of_activity) + "]/div/app-document-table/div/div[2]/"
                                                                                 "mat-table/mat-row[" + str(
                                                             each_body_row) + "]/mat-cell[5]/mat-icon").click()
                                    print("click2")
                                    # Sleeping until the pop-up window appears
                                    while True:
                                        try:
                                            print("waiting until the window appears")
                                            browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/"
                                                                           "mat-dialog-container/div/div/app-pdf-viewer"
                                                                           "-dialog/h2")
                                            break
                                        except NoSuchElementException:
                                            print("waiting exception")
                                            time.sleep(2)
                                    time.sleep(2)

                                    # Grabbing the filename of the download
                                    print("grab file name")
                                    preset_filename = browser.find_element(By.XPATH,
                                                                           "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-pdf-viewer-dialog/h2").text
                                    time.sleep(2)
                                    print("grab finish")
                                    preset_filename = re.sub(".PDF", ".pdf", preset_filename)
                                    print("named file name")
                                    time.sleep(2)

                                    # Click to Download the PDF
                                    browser.find_element(By.XPATH,
                                                         "/html/body/div[3]/div[2]/div/mat-dialog-container/app-pdf-viewer-dialog/"
                                                         "mat-dialog-content/amt-pdf-viewer/div/ngx-extended-pdf-viewer/div/div/div/div/"
                                                         "div[2]/pdf-toolbar/div/div/div[1]/div[2]/pdf-download/pdf-shy-button/button").click()
                                    print("click3")
                                    time.sleep(2)
                                    time_pdf_download = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    print(f"Download Time: {time_pdf_download}")
                                    DatePDFDownloaded = datetime.now().strftime("%Y-%m-%d")

                                    # Checking to make sure the PDF file gets downloaded
                                    file_exists = True
                                    while file_exists:
                                        list_of_files = os.listdir(download_path)
                                        list_of_files = [os.path.join(download_path, basename.upper()) for basename in
                                                         list_of_files]
                                        if download_path + preset_filename.upper() not in list_of_files:
                                            time.sleep(1)
                                        else:
                                            file_exists = False
                                    time.sleep(3)
                                    # Closing the view PDF window
                                    browser.find_element(By.XPATH,
                                                         "/html/body/div[3]/div[2]/div/mat-dialog-container/app-pdf-viewer-dialog/"
                                                         "h2/button").click()
                                    print("click4")
                                    time.sleep(1)

                                    # Changing format of Gen Date from 'Jun 9, 2017' to '2017-06-09'
                                    #   removed --> re.sub("/", "-", each_row_list[4])
                                    gen_date = datetime.strptime(each_row_list[4], '%b %d, %Y').strftime("%Y-%m-%d")

                                    # Change filename in case of any duplicates when downloading from carrier.
                                    new_filename = re.sub(" ", "", each_row_list[2]) + "_" + \
                                                   each_row_list[0] + "GenDate=" + gen_date + "_downloadTime=" + \
                                                   re.sub(":", "-", time_pdf_download) + ".pdf"
                                    # Scrubbing the new filename for any special characters to the newly named pdf
                                    new_filename = re.sub("\\\\", "", re.sub("/", "", re.sub(":", "", re.sub("\*", "",
                                                                                                             re.sub(
                                                                                                                 "\?",
                                                                                                                 "",
                                                                                                                 re.sub(
                                                                                                                     "\"",
                                                                                                                     "",
                                                                                                                     re.sub(
                                                                                                                         "<",
                                                                                                                         "",
                                                                                                                         re.sub(
                                                                                                                             ">",
                                                                                                                             "",
                                                                                                                             new_filename))))))))
                                    new_filename = download_path + new_filename

                                    DownloadStatus_InsuredCopy = "True"
                                    DownloadFile_InsuredCopy_Location = new_filename
                                    os.rename(download_path + preset_filename, new_filename)
                                    Time_Download_PhaseComplete = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    Automation_DownloadPhaseCompleted = "True"
                                    time.sleep(1)

                                    each_row_list += [datetime.now().strftime("%Y-%m-%d"), DownloadStatus_InsuredCopy]

                                    if DownloadFile_AgentCopy_Location != "":
                                        DownloadFile_Agent_Size = str(os.stat(DownloadFile_AgentCopy_Location).st_size)
                                    if DownloadFile_InsuredCopy_Location != "":
                                        DownloadFile_Insured_Size = str(
                                            os.stat(DownloadFile_InsuredCopy_Location).st_size)

                                # Else, skip because it already exist
                                else:
                                    each_row_list += [datetime.now().strftime("%Y-%m-%d"), check_if_exist[1]]
                                    skipped_download_bool = True

                                gen_date = datetime.strptime(each_row_list[4], "%b %d, %Y").strftime("%m-%d-%Y")
                                # print(f"gen_date: {gen_date}")
                                # print(f"type --> gen_date: {type(gen_date)}")
                                print(f"\t{each_row_list}")

                                # Adding the carrier specific data to the carrier specific table in database
                                added_to_table = sql_connector_insert_amtrust([each_row_list], "amtrust_table")
                                if added_to_table[0]:
                                    # Adding the data grabbed to the database at the end of each column
                                    carrier_PDF_Automation.sql_connector_insert_master(
                                        carrier_PDF_Automation.list_to_sql_formatter(
                                            [["Amtrust", str(gen_date), each_row_list[0], PolicyEffectiveDate,
                                              each_row_list[1], each_row_list[2] + "-" + each_row_list[3],
                                              TransactionTypeFromSolomon, time_pdf_download, each_row_list[5],
                                              Automation_DownloadPhaseCompleted, Time_Download_PhaseComplete,
                                              DownloadStatus_AgentCopy, DownloadFile_AgentCopy_Location,
                                              DownloadFile_Agent_Size, DownloadStatus_InsuredCopy,
                                              DownloadFile_InsuredCopy_Location, DownloadFile_Insured_Size,
                                              Automation_ProcessPhaseCompleted, Time_Process_PhaseComplete,
                                              Automation_AttachPhaseCompleted, Time_AttachToEpic_PhaseComplete,
                                              AutomationStatus, TimeOf_FailOrComplete, LogComments]]))
                                    print("--- Added to the master_policy_table ---")

                                    temp_list = each_row_list + [DatePDFDownloaded]

                                    # Writing the row to the Amtrust CSV that will be sent via email
                                    pdf_download_email = open(file_path + "00_Amtrust_Email.csv", "a", encoding="UTF8",
                                                              newline="")
                                    writer = csv.writer(pdf_download_email)
                                    writer.writerow(temp_list)
                                    pdf_download_email.close()

                                else:
                                    print("--- Did not add to the master_policy_table because this already exists ---")

                                    # Since it did not add to the master table, must remove the file
                                    if DownloadFile_InsuredCopy_Location != "":
                                        os.remove(DownloadFile_InsuredCopy_Location)
                                        print(
                                            "--- Removed the INSURED Copy as it was already previously downloaded ---")
                                        DatePDFDownloaded = added_to_table[1]
                                    elif skipped_download_bool:
                                        print("--- Was already checked, no need to remove download ---")
                                        DatePDFDownloaded = added_to_table[1]
                                    else:
                                        print("--- Can not delete the downloaded PDF because the download "
                                              "does not exist ---")

                                # Adding the carrier specific data to the carrier specific table in database
                                each_row_list += [DatePDFDownloaded]
                                print(f"\t{each_row_list}")

                                # Writing the row to the BoolTable
                                pdf_download_bool = open(file_path + "00_Amtrust.csv", "a", encoding="UTF8", newline="")
                                writer = csv.writer(pdf_download_bool)
                                writer.writerow(each_row_list)
                                pdf_download_bool.close()
                                time.sleep(1)

                        # Once you finish with a page ... Trying to see if we can get to the next page
                        page_text = browser.find_element(By.XPATH,
                                                         "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/"
                                                         "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/div/"
                                                         "amt-tab-body[" + str(
                                                             type_of_activity) + "]/div/app-document-table/div/div[2]/"
                                                                                 "mat-paginator/div/div/div[2]/div").text
                        print(page_text)

                        # if page_text contains the same number then do not click next and break out of this while loop
                        page_text_list = page_text.split(" ")
                        time.sleep(2)

                        if page_text_list[2] != page_text_list[4]:
                            # Element to Click the next page
                            print("value check")
                            time.sleep(3)
                            print(type_of_activity)
                            button = browser.find_element(By.XPATH,
                                                          "/html/body/app-root/mat-drawer-container/mat-drawer-content/div/app-home/div[3]/"
                                                          "mat-tab-group/div/mat-tab-body[3]/div/app-recent-documents/amt-vertical-tab-group/"
                                                          "div/amt-tab-body[" + str(
                                                              type_of_activity) + "]/div/app-document-table/div/div[2]/"
                                                                                  "mat-paginator/div/div/div[2]/button[2]/span[1]")
                            print(str(button))
                            # This is the main line of issue 05.4.2023

                            browser.execute_script("arguments[0].click();", button)

                            print("click5")
                            next_page_bool = True
                        else:
                            next_page_bool = False

                        time.sleep(1)

        # Logging out of the account to go to the next user (next Amtrust Account)
        browser.find_element(By.XPATH,
                             "/html/body/app-root/app-header/amt-header/header/div[4]/amt-menu-item/div/div[1]/span[2]").click()
        time.sleep(2)
        browser.find_element(By.XPATH,
                             "/html/body/app-root/app-header/amt-header/header/div[4]/amt-menu-item/div/div[2]/ul/li").click()
        time.sleep(3)
        browser.close()

        if username == list(accounts_dict.keys())[-1] and password == list(accounts_dict.values())[-1]:
            carrier_PDF_Automation.reporting_for_processing_2("amtrust_table", file_path + "00_Amtrust_Email.csv")
            time.sleep(2)
            browser.quit()


def sql_connector_check_amtrust(insert_list):
    """

    :param insert_list:
    :param table_name:
    :return:
    """
    check_bool = [False, ""]

    db = mysql.connector.connect(
        host='ls-b0014ce1c775939bc5a023d3d923dc65c1e083fb.cdc34lpuvapw.us-east-1.rds.amazonaws.com',
        user='dbmasteruser',
        passwd='UT`sjRhNT^S?zq,I8l~$XdLtO6LTrJ0&',
        database='iua_carrier_download_auto_db'
    )

    my_cursor = db.cursor()
    for each_row in insert_list:
        # Check for if the row already exists in the database
        check_query = "SELECT * FROM amtrust_table WHERE PolicyNumber = %s AND Insured = %s AND Activity = %s AND " \
                      "DescriptionCol = %s AND GeneratedDate = %s AND Username = %s;"
        check_val = (each_row[0], each_row[1], each_row[2], each_row[3], each_row[4], each_row[5])
        my_cursor.execute(check_query, check_val)
        my_result = my_cursor.fetchall()
        row_count = my_cursor.rowcount

        # if row_count is 0 then could not find existing entry
        if row_count == 0:
            print("--- Could not find entry in Database, attempting download ---")
            check_bool[0] = True
        else:
            print("--- Found entry in Database ... Checking to see if the download was retrieved ---")
            # Grabbing the date that the item was downloaded
            check_query = "SELECT PDFDownloadBoolean FROM amtrust_table WHERE PolicyNumber = %s AND Insured = %s AND " \
                          "Activity = %s AND DescriptionCol = %s AND GeneratedDate = %s AND Username = %s;"
            check_val = (each_row[0], each_row[1], each_row[2], each_row[3], each_row[4], each_row[5])
            my_cursor.execute(check_query, check_val)
            my_result = my_cursor.fetchall()
            if "True" in my_result[0][0]:
                print("--- Download found, skipping download ---")
                check_bool[0] = False
                check_bool[1] = "True"
            else:
                print("--- Download not found, attempting download ---")
                check_bool[0] = True

        # Required to make/save the changes
        db.commit()
    db.close()
    return check_bool


def sql_connector_insert_amtrust(insert_list, table_name):
    """

    :param insert_list:
    :param table_name:
    :return:
    """
    added_to_table = [False, "None"]

    db = mysql.connector.connect(
        host='ls-b0014ce1c775939bc5a023d3d923dc65c1e083fb.cdc34lpuvapw.us-east-1.rds.amazonaws.com',
        user='dbmasteruser',
        passwd='UT`sjRhNT^S?zq,I8l~$XdLtO6LTrJ0&',
        database='iua_carrier_download_auto_db'
    )

    my_cursor = db.cursor()
    for each_row in insert_list:
        # Check for if the row already exists in the database
        check_query = "SELECT * FROM amtrust_table WHERE PolicyNumber = %s AND Insured = %s AND Activity = %s AND " \
                      "DescriptionCol = %s AND GeneratedDate = %s AND Username = %s AND PDFDownloadBoolean = %s;"
        check_val = (each_row[0], each_row[1], each_row[2], each_row[3], each_row[4], each_row[5], each_row[7])
        # Took out the "ScriptRunDate = %s AND " from the check_query
        # Took out the "each_row[6], " from check_val
        my_cursor.execute(check_query, check_val)
        my_result = my_cursor.fetchall()
        # print(f"The Result of fetch:  {my_result}")
        row_count = my_cursor.rowcount
        # print(f"row count:  {row_count}")

        # Add to the database if the result doesn't exist
        if row_count == 0:
            sql = "INSERT INTO amtrust_table (CarrierName, PolicyNumber, Insured, Activity, DescriptionCol, " \
                  "GeneratedDate, Username, ScriptRunDate, PDFDownloadBoolean) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = ("Amtrust", each_row[0], each_row[1], each_row[2], each_row[3], each_row[4], each_row[5], each_row[6],
                   each_row[7])
            my_cursor.execute(sql, val)
            added_to_table[0] = True
        else:
            print("---- ROW EXISTS; DID NOT ADD TO THE DATABASE! ----")
            added_to_table[0] = False

            # Grabbing the date that the item was downloaded
            check_query = "SELECT ScriptRunDate FROM amtrust_table WHERE PolicyNumber = %s AND Insured = %s AND " \
                          "Activity = %s AND DescriptionCol = %s AND GeneratedDate = %s AND Username = %s AND " \
                          "PDFDownloadBoolean = %s;"
            check_val = (each_row[0], each_row[1], each_row[2], each_row[3], each_row[4], each_row[5], each_row[7])
            my_cursor.execute(check_query, check_val)
            my_result = my_cursor.fetchall()
            added_to_table[1] = my_result[0][0]

        # Required to make/save the changes
        db.commit()
    db.close()
    return added_to_table


def main():
    """
    Main function to run the Epic Attachment Script

    :return:
        None
    """
    try:
        file_path, download_path = carrier_PDF_Automation.required_info("Amtrust_PDF_Download\\")
        amtrust(file_path, download_path)
    except Exception as err:
        script_name = os.path.basename(__file__)
        carrier_PDF_Automation.send_error_email(script_name + " has run into an Error", "Error Message is: \n\n" +
                                                str(err))
        print(f"\n.\n.\n.\n.\n{script_name} has an ERROR, Email has been sent!")


if __name__ == '__main__':
    main()
