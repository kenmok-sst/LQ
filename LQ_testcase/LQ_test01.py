# coding=UTF-8
'''
Created on 2021.10.21
Updated on 2023.05.12
Author: Ken Mok
'''
# -*- coding: utf-8 -*-
# pip install PyYAML
import unittest
import os
import yaml
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from LQ_testcase.LQ_login import TestMemberLogin

test_dir = "./LQ_testcase/"
CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/LQ_testcase/"

class TestViewTabsAndPages(unittest.TestCase):

    def setUp(self):
        conf = yaml.load(open(CONF_PATH + 'config.yml'), Loader=yaml.FullLoader)
        """
        desired_caps={}
        desired_caps['platformName'] = conf['platformName']
        desired_caps['platformVersion'] = conf['platformVersion']
        desired_caps['deviceName'] = conf['deviceName']
        desired_caps['udid'] = conf['udid']
        desired_caps['appPackage'] = conf['appPackage']
        desired_caps['appActivity'] = conf['appActivity']
        self.driver = webdriver.Remote(conf['driver'], desired_caps)
            """
        options = UiAutomator2Options()
        options.platform_name = conf['platformName']
        options.device_name = conf['deviceName']
        options.udid = conf['udid']
        options.app_package = conf['appPackage']
        options.app_activity = conf['appActivity']
        self.driver = webdriver.Remote(conf['driver'], options=options)




    def testlq0001(self):
        try:
            print("\nLQ0001 View Tabs and Pages start")

            testdata = yaml.load(open(CONF_PATH + 'test_data.yml'), Loader=yaml.FullLoader)
            login_member = testdata['login_dev_normal_user_04']

            login_member_username = login_member['username']
            login_member_password = login_member['pwd']

            # Wait 6 seconds for Introduction page
            time.sleep(10)
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='同意並接受']]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.view.ViewGroup']]]]/*/*[@text and ./parent::*[@class='android.view.ViewGroup']])[2]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='同意']]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='密碼登錄']]").click()

            # Input username
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.EditText").send_keys(login_member_username)

            # Input password
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.EditText").send_keys(login_member_password)

            # Click Log-in Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='登錄']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='登錄']]").click()
            time.sleep(18)
            '''
            # Tabs in top of page
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='足球']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='足球']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='篮球']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='篮球']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='主播']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='主播']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='微头条']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='微头条']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='视频']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='视频']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='锦囊']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='锦囊']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='活动']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='活动']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]").click()
            time.sleep(2)
            '''
            '''
            # All of the latest Ace
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[1]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[1]").click()

            time.sleep(5)

            # Click 推荐 to go back to Home
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]").click()
            time.sleep(2)

            # All of the Hot Live
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[2]")))
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[2]").click()
            time.sleep(5)

            # Click Back icon to go back to Home
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='󰅁']")))
            self.driver.find_element_by_xpath("//*[@text='󰅁']").click()
            self.driver.find_element(By.LINK_TEXT, "󰅁").click()
            time.sleep(2)
            '''

            # Click 推荐 to go back to Home
            #WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]")))
            #self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]").click()
            #time.sleep(2)

            ### Click any item searched by text
            text = '1111六六六'
            self.driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("'+text+'").instance(0));').click()
            time.sleep(2)
            #self.driver.execute_script("mobile: scroll", {'strategy': '-android uiautomator', 'selector': 'text("'+text+'")'})
            #seetest NOK
            #self.driver.execute_script("seetest:client.swipeWhileNotFound2(\"Down\", 200, 2000, \"NATIVE\", \"xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+text+"']]\", 0, 1000, 10, true)")
            time.sleep(4)

        except TimeoutException:
            print("LQ0001 View Tabs and Pages Timeout Exception")
            assert(False)
        except Exception:
            print("LQ0001 View Tabs and Pages Exception")
            assert(False)
        finally:
            print("LQ0001 View Tabs and Pages finish")

    def testlq0002(self):
        try:
            print("\nLQ0002 Log in")

            testdata = yaml.load(open(CONF_PATH + 'test_data.yml'), Loader=yaml.FullLoader)
            login_member = 'login_dev_normal_user_04'

            #login_member_username = login_member['username']
            #login_member_password = login_member['pwd']

            # Wait 6 seconds for Introduction page
            time.sleep(10)
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='同意並接受']]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup'] and (./preceding-sibling::* | ./following-sibling::*)[@class='android.view.ViewGroup']]]]/*/*[@text and ./parent::*[@class='android.view.ViewGroup']])[2]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@class='android.view.ViewGroup' and ./*[@text='同意']]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[8]").click()

            # Log in as user02
            TestMemberLogin.testmember_password_login(self,login_member)
            time.sleep(6)

        except TimeoutException:
            print("LQ0002 Log in Timeout Exception")
            assert(False)
        except Exception:
            print("LQ0002 Log in Exception")
            assert(False)
        finally:
            print("LQ0002 Log in finish")

    def testlq0003(self):
        try:
            print("\nLQ0003 Log in")

            # Wait 6 seconds for Introduction page
            time.sleep(6)

            # Log in as user02
            TestMemberLogin.testmember_vcode_login(self,'login_dev_normal_user_02')
            time.sleep(6)

        except TimeoutException:
            print("LQ0003 Log in Timeout Exception")
            assert(False)
        except Exception:
            print("LQ0003 Log in Exception")
            assert(False)
        finally:
            print("LQ0003 Log in finish")



    def tearDown(self):
        self.driver.quit()