# coding=UTF-8
'''
Created on 2021.10.21
Updated on 2022.12.13
Author: Ken Mok
'''
# -*- coding: utf-8 -*-
# pip install PyYAML
import unittest
import os
import yaml
import time

#from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\LQ_testcase\\"

class TestMemberLogin(unittest.TestCase):

    def testmember_password_login(self,user):
        print("Member Password Log In Start")
        print(user)
        testdata = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
        login_member = testdata[user]

        login_member_username = login_member['username']
        login_member_password = login_member['pwd']

        ## Click 我的 button in Bottom Bar
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@contentDescription='我的, tab, 4 of 4']")))
        self.driver.find_element_by_xpath("//*[@contentDescription='我的, tab, 4 of 4']").click()
        time.sleep(2)

        ## Click 登录 button
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='登录']]")))
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='登录']]").click()
        time.sleep(2)

        ## Click 密码登录 button
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"密码登录")))
        self.driver.find_element_by_link_text("密码登录").click()
        time.sleep(2)

        ## Input username
        print("Input username")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.EditText")))
        self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.EditText").click()
        time.sleep(2)
        self.driver.execute_script("seetest:client.sendText(\""+ login_member_username +"\")")
        time.sleep(2)

        ## Input password
        print("Input password")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.widget.EditText")))
        self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.widget.EditText").click()
        time.sleep(2)
        self.driver.execute_script("seetest:client.sendText(\""+ login_member_password +"\")")
        time.sleep(2)

        ## Click Log-in key
        print("Click Log-in key")
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='登录']]")))
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='登录']]").click()

        time.sleep(2)
        print("Member Password Log In End")

    def testmember_vcode_login(self,user):
        print("Member Vcode Log In Start")
        print(user)
        testdata = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
        login_member = testdata[user]

        login_member_username = login_member['username']
        login_vcode = testdata['vcode']

        ## Click 我的 button in Bottom Bar
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@contentDescription='我的, tab, 4 of 4']")))
        self.driver.find_element_by_xpath("//*[@contentDescription='我的, tab, 4 of 4']").click()
        time.sleep(2)

        ## Click 登录 button
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='登录']]")))
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='登录']]").click()
        time.sleep(2)

        ## Input username
        print("Input username")
        #self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.EditText").click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@text='+86']]]")))
        #self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.EditText").send_keys(login_member_username)
        self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@text='+86']]]").click()
        time.sleep(2)
        self.driver.execute_script("seetest:client.sendText(\""+ login_member_username +"\")")
        time.sleep(2)

        ## Obtain Vcode
        print("Obtain Vcode")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='获取验证码']]")))
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='获取验证码']]").click()
        time.sleep(2)

        ## 输入验证码
        print("Input Vcode")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='请输入验证码']")))
        self.driver.find_element_by_xpath("//*[@text='请输入验证码']").click()
        time.sleep(2)

        self.driver.execute_script("seetest:client.sendText(\""+ login_vcode +"\")")
        time.sleep(2)

        ## 登录
        print("Click 登录/注册")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='登录/注册']]")))
        self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='登录/注册']]").click()
        time.sleep(2)

        print("Member Vcode Log In End")
