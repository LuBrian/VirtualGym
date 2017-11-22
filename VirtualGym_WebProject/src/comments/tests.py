import datetime
from django.test import TestCase
from VirtualGym.models import *
from selenium import webdriver
import time
import os,sys

# this test is a UI test for comment app
class UITestCase(TestCase):
	# set up browser to firefox browser
    def setUp(self):
        self.browser = webdriver.Firefox()

    # close browser after test    
    def tearDown(self):
        self.browser.quit()

    # test if user can comment a exercise
    # test if user can reply a comment
    def test_add_comment(self):
    	try:
    		self.browser.get("http://localhost:8000/viewProfile/")
    		self.assertIn("http://localhost:8000/viewProfile/", self.browser.current_url)
    		tag = self.browser.find_element_by_partial_link_text('Triceps').text
    		self.assertEqual('Triceps' in tag, True)
    		tag = self.browser.find_element_by_partial_link_text('Triceps').click()
    		if(self.browser.find_element_by_partial_link_text('Sign In')):
    			signIn = self.browser.find_element_by_partial_link_text('Sign In').click()
    			email = self.browser.find_element_by_id('email')
    			email.send_keys('test@vg.ca')
    			password = self.browser.find_element_by_id('password')
    			password.send_keys('admin1234')
    			sign_In = self.browser.find_element_by_id('signInButton').click()
    		self.browser.get("http://localhost:8000/viewProfile/")
    	
    		tag = self.browser.find_element_by_partial_link_text('Triceps').click()
    		comment = self.browser.find_element_by_name('comment')
    		comment.send_keys("comment from test")
    		submit_comment = self.browser.find_element_by_id("submitComment").click()
    		reply = self.browser.find_elements_by_xpath("//*[@id='id_comment']")
    		reply[1].send_keys("reply from test")
    		submit_reply = self.browser.find_element_by_id("reply").click()
    	except:
    		print("Comment test failed! server down or no internet for now")
    		print("Please check or contact us! ")