# coding=UTF-8
'''
Created on 2021.10.21
Updated on 2022.12.12
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

#from appium.options.android import UiAutomator2Options
#from appium.webdriver.common.appiumby import AppiumBy

from LQ_testcase.LQ_login import TestMemberLogin

test_dir = "./Automation Test/LQ_testcase/"
CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\LQ_testcase\\"

class TestViewTabsAndPages(unittest.TestCase):

    def setUp(self):
        conf = yaml.load(open(CONF_PATH + 'config.yml'), Loader=yaml.FullLoader)
        desired_caps={}
        desired_caps['platformName'] = conf['platformName']
        desired_caps['platformVersion'] = conf['platformVersion']
        desired_caps['deviceName'] = conf['deviceName']
        desired_caps['udid'] = conf['udid']
        desired_caps['appPackage'] = conf['appPackage']
        desired_caps['appActivity'] = conf['appActivity']
        self.driver = webdriver.Remote(conf['driver'], desired_caps)

    def testlq0001(self):
        try:
            print("\nLQ0001 View Tabs and Pages start")
            # Log in user06

            # Wait 6 seconds for Introduction page
            #WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@text='跳过 4 s']]]]")))
            #self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@text='跳过 4 s']]]]").click()
            time.sleep(6)

            # Tabs in top of page
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='足球']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='足球']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='篮球']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='篮球']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='微头条']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='微头条']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='视频']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='视频']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='锦囊']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='锦囊']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='活动']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='活动']]").click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]").click()
            time.sleep(2)

            # All of the latest Ace
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[1]")))
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[1]").click()

            time.sleep(5)

            # Click 推荐 to go back to Home
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]").click()
            time.sleep(2)

            # All of the Hot Live
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[2]")))
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[2]").click()
            time.sleep(5)

            # Click Back icon to go back to Home
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='󰅁']")))
            self.driver.find_element_by_xpath("//*[@text='󰅁']").click()
            time.sleep(2)

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

            # Wait 6 seconds for Introduction page
            time.sleep(6)

            # Log in as user02
            TestMemberLogin.testmember_password_login(self,'login_dev_normal_user_02')
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