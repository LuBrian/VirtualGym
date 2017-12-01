import datetime
from django.test import TestCase
from VirtualGym.models import *
from selenium import webdriver
import time
import os,sys

# this test is a UI test for comment app
# class UITestCase(TestCase):
# 	# set up browser to firefox browser
#     def setUp(self):
#         self.browser = webdriver.Firefox()

#     close browser after test    
#     def tearDown(self):
#         self.browser.quit()

#     # test if user can comment a exercise
#     # test if user can reply a comment
#     def test_add_comment(self):
#         try:
#             self.browser.get("http://localhost:8000/viewProfile/")
#             self.assertIn("http://localhost:8000/viewProfile/", self.browser.current_url)
#             title = self.browser.find_element_by_partial_link_text('test').text
#             self.assertEqual('test' in title, True)
#             title = self.browser.find_element_by_partial_link_text('test').click()
#             # signIn = self.browser.find_elements_by_xpath("/html/body/div/div[3]/div/div[3]/form/a").click()
#             if(self.browser.find_element_by_partial_link_text('Sign In')):
#                 signIn = self.browser.find_element_by_partial_link_text('Sign In').click()
#                 email = self.browser.find_element_by_id('email')
#                 email.send_keys('sprint4_test@vg.ca')
#                 password = self.browser.find_element_by_id('password')
#                 password.send_keys('123')
#                 sign_In = self.browser.find_element_by_id('signInButton').click()
#                 check = self.browser.find_element_by_id("detail_title").text
#                 self.assertEqual('test' in check, True)
        	
        		
#             comment = self.browser.find_element_by_name('comment')
#             comment.send_keys("comment from test")
#             comment.click()
#             submit_comment = self.browser.find_element_by_id("submitComment").click()
#             reply = self.browser.find_elements_by_xpath("//*[@id='reply_click']")
#             reply[0].click()
#             reply = self.browser.find_elements_by_xpath("//*[@id='id_comment']")
#             reply[1].send_keys("reply from test")
#             submit_reply = self.browser.find_element_by_id("reply").click()
#             print("Comment test passed!")
#         except:
#             print("Comment test failed! server down or no internet for now")
#             print("Please check or contact us! ")