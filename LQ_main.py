# coding=UTF-8
'''
Created on 2022.8.08
Updated on 2022.12.12
Author: Ken Mok
'''
#coding:utf-8

import unittest

## Single test case
# MyDrug
#from hago_testcase.hago_addmydrug01 import TestAddMyDrug

from LQ_testcase.LQ_test01 import TestViewTabsAndPages

from unittest import TestLoader, TestSuite
from HTMLTestRunner import HTMLTestRunner

#from config.globalparameters import test_case_path,report_name

#test_report_file_name = './hago_testcase/test_report.txt'
test_dir = './LQ_testcase'
#report_name = './LQ_testcase/test_html_report.html'
#discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='hago_easyq0*.py') #Single File running

# Build a test set, including all .py files starting with test in the src/tests directory
#suite=unittest.defaultTestLoader.discover(test_case_path,pattern='hago_*.py')
 # Perform test
if __name__=="__main__":
    ##fb = open(report_name,'wb')

    ### Test case
    suite = unittest.TestSuite()
    #suite.addTest(TestViewTabsAndPages('testlq0001'))
    suite.addTest(TestViewTabsAndPages('testlq0002'))

    ##### Running Single test case with HTML Test Report
    #runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
    #                        open_in_browser=True, description="HTMLTestReport")
    #runner = HTMLTestRunner(log=True, verbosity=2, output='report', title=u'Test report', report_name='report', description=u'HTMLTestReport')

    ##### Running Single test case without HTML Test Report
    runner = unittest.TextTestRunner()

    ##### Running Multiple test cases in files
    #runner.run(discover)

    ##### Run Test
    runner.run(suite)

    ##### Test suite
    #runner = unittest.TextTestRunner()
    #runner = HTMLTestRunner(log=True, verbosity=2, output='report', title=u'Test report', report_name='report', description=u'HTMLTestReport')


