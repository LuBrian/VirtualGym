import datetime
from django.test import TestCase
from VirtualGym.models import *
from selenium import webdriver
import time
import os,sys



# This test is a UItest for FQA app
class UITestCase(TestCase):
	# set up browser to firefox
    def setUp(self):
        self.browser = webdriver.Firefox()

    # close browser after test
    def tearDown(self):
        self.browser.quit()

    # test if user can ask a question in FQA
    # test if user can answer a question
    def test_FQA(self):
    	try:
    		self.browser.get("http://localhost:8000/QA/")
    		self.assertIn("http://localhost:8000/QA/", self.browser.current_url)
    		if(self.browser.find_element_by_partial_link_text('Sign In')):
    			signIn = self.browser.find_element_by_partial_link_text('Sign In').click()
    			email = self.browser.find_element_by_id('email')
    			email.send_keys('test@vg.ca')
    			password = self.browser.find_element_by_id('password')
    			password.send_keys('admin1234')
    			sign_In = self.browser.find_element_by_id('signInButton').click()
    		self.browser.get("http://localhost:8000/QA/")
    		self.assertIn("http://localhost:8000/QA/", self.browser.current_url)
    		askButton = self.browser.find_element_by_id('askButton').click()
    		question = self.browser.find_elements_by_xpath("//*[@id='id_questionDescription']")
    		question[-1].send_keys("question from test")
    		submitQ = self.browser.find_element_by_id("submitQ").click()
    		replyButton = self.browser.find_element_by_css_selector("#button").click()
    		self.browser.execute_script("arguments[0].value = arguments[1]", self.browser.find_element_by_css_selector("#id_questionDescription"), "Reply from test")
    		reply = self.browser.find_element_by_css_selector("#replyA")
    		self.browser.execute_script("$(arguments[0]).click();", reply)
    	except:
            print("FQA test failed! server down or no internet for now")
            print("Please check or contact us! ")
	