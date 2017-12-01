from django.test import TestCase
import datetime
from VirtualGym.models import *
from selenium import webdriver
import time
import os,sys

# this test is a UI test for User app(basiclly sign in and sign out)
# class UITestCase(TestCase):
# 	# set up browser to firefox
#     def setUp(self):
#         self.browser = webdriver.Firefox()

#     # close the browser after test
#     def tearDown(self):
#         self.browser.quit()

#     # test if user can signIn with their vg account through type
#     # in their username and password    
#     def test_signIn(self):
#     	try:
#     		self.browser.get("http://localhost:8000/signIn/")
#     		email = self.browser.find_element_by_id('email')
#     		email.send_keys('xin@vg.ca')
#     		password = self.browser.find_element_by_id('password')
#     		password.send_keys('admin1234')
#     		signIn = self.browser.find_element_by_id('signInButton').click()
#     		self.assertIn("http://localhost:8000/", self.browser.current_url)
#     	except:
#             print("Sign in test failed! server down or no internet for now")
#             print("Please check or contact us! ")

#     # test if user can sign out through navgation bar
#     def test_signOut(self):
#     	try:
#     		self.browser.get("http://localhost:8000/signIn/")
#     		self.assertIn("http://localhost:8000/signIn/", self.browser.current_url)
#     		email = self.browser.find_element_by_id('email')
#     		email.send_keys('xin@vg.ca')
#     		password = self.browser.find_element_by_id('password')
#     		password.send_keys('admin1234')
#     		signIn = self.browser.find_element_by_id('signInButton').click()
#     		self.assertIn("http://localhost:8000/", self.browser.current_url)
#     		signOut = self.browser.find_element_by_partial_link_text('Log Out').click
#     	except:
#             print("Sign out test failed! server down or no internet for now")
#             print("Please check or contact us! ")

#     # test if user can sign in through their google account
#     def test_google_SignIn(self):
#     	try:
#         	self.browser.get("http://localhost:8000/signIn/")
#         	self.assertIn("http://localhost:8000/signIn/", self.browser.current_url)
#         	Google_signIn = self.browser.find_element_by_id('googleSignIn').click()
#         	time.sleep(1)
#         	email = self.browser.find_element_by_xpath("//*[@id='identifierId']")
#         	email.send_keys("virthalgymlogintest@gmail.com")
#         	time.sleep(1)
#         	next_step = self.browser.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
#         	time.sleep(3)
#         	password = self.browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
#         	password.send_keys("virtualgym")
#         	time.sleep(1)
#         	password_step = self.browser.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
#         	time.sleep(1)
#         	self.assertIn("http://localhost:8000/", self.browser.current_url)
#     	except:
#             print("Google sign in test failed! server down or no internet for now")
#             print("Please check or contact us! ")


#     # test if moderator can login through admin page by type in
#     # their superUser username and password
#     def test_moderator_Login(self):
#     	try:
#         	self.browser.get("http://localhost:8000/admin/")
#         	self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
#         	username = self.browser.find_element_by_xpath("//*[@id='id_username']")
#         	username.send_keys("test@vg.ca")
#         	password = self.browser.find_element_by_xpath("//*[@id='id_password']")
#         	password.send_keys("admin1234")
#         	Log_in = self.browser.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()
#         	self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
#     	except:
#             print("Moderator login test failed! server down or no internet for now")
#             print("Please check or contact us! ")

#     # test if user can sign in through their facebook account
#     def test_facebook_SignIn(self):
#         try:
#             self.browser.get("http://localhost:8000/signIn/")
#             self.assertIn("http://localhost:8000/signIn/", self.browser.current_url)
#             facebook_signIn = self.browser.find_element_by_id('facebookSignIn').click()
#             time.sleep(1)
#             email = self.browser.find_element_by_xpath("//*[@id='email']")
#             email.send_keys("virthalgymlogintest@gmail.com")
#             time.sleep(1)
#             password = self.browser.find_element_by_xpath("//*[@id='pass']")
#             password.send_keys("virtualgym")
#             time.sleep(1)
#             logIn = self.browser.find_element_by_xpath("//*[@id='loginbutton']").click()
#             try:
#                 continueLogin = self.browser.find_element_by_xpath("//*[@id='u_0_x']/div[2]/div[1]/div[1]/button").click()
#             except:
#                 print("user already sign Up with this facebook account")
#                 print("Log in successful!")

#             time.sleep(3)
#             self.assertIn("http://localhost:8000/", self.browser.current_url)
#         except:
#             print("Facebook sign in test failed! server down or no internet for now")
#             print("Please check or contact us! ")

#     # test if user can sign in through their twitter account
#     def test_twitter_SignIn(self):
#     	try:
#         	self.browser.get("http://localhost:8000/signIn/")
#         	self.assertIn("http://localhost:8000/signIn/", self.browser.current_url)
#         	twitter_signIn = self.browser.find_element_by_id('twitterSignIn').click()
#         	time.sleep(1)
#         	email = self.browser.find_element_by_xpath("//*[@id='username_or_email']")
#         	email.send_keys("virthalgymlogintest@gmail.com")
#         	time.sleep(1)
#         	password = self.browser.find_element_by_xpath("//*[@id='password']")
#         	password.send_keys("virtualgym")
#         	time.sleep(1)
#         	logIn = self.browser.find_element_by_xpath("//*[@id='allow']").click()
#         	time.sleep(3)
#         	self.assertIn("http://localhost:8000/", self.browser.current_url)
#     	except:
#             print("Twitter sign in test failed! server down or no internet for now")
#             print("Please check or contact us! ")

