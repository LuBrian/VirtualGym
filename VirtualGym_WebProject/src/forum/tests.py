import datetime
from django.test import TestCase
from VirtualGym.models import *
from selenium import webdriver
import time
import os,sys



# This test is a UItest for FQA app
# class UITestCase(TestCase):
# 	# set up browser to firefox
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()

#     # close browser after test
#     def tearDown(self):
#         self.browser.quit()

#     # test if user can ask a question in backend FQA
#     # test if user can add an answer in backend for a question
	# def test_FQA(self):
	# 	try:
	# 		self.browser.get("http://localhost:8000/admin/")
	# 		self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
	# 		username = self.browser.find_element_by_xpath("//*[@id='id_username']")
	# 		username.send_keys("sprint4_admin@vg.ca")
	# 		password = self.browser.find_element_by_xpath("//*[@id='id_password']")
	# 		password.send_keys("admin1234")
	# 		Log_in = self.browser.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()
	# 		question = self.browser.find_element_by_xpath("//*[@id='menu-content']/li[4]/i/a").click()
	# 		addQuestion = self.browser.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li/a").click()
	# 		q = self.browser.find_element_by_xpath("//*[@id='id_Question']").send_keys("Question from backend FQA")
	# 		a = self.browser.find_element_by_xpath("//*[@id='id_Answer']").send_keys("Answer from backend FQA")
	# 		save = self.browser.find_element_by_xpath("/html/body/div/div[3]/div[1]/form/div/div/input[1]").click()
	# 		# check if new question and answer are up
	# 		self.browser.get("http://localhost:8000/QA/")
	# 		self.assertIn("http://localhost:8000/QA/", self.browser.current_url)
	# 		question = self.browser.find_element_by_xpath("//*[@id='faqAccordion']/div[7]/div[1]/h4/a").text
	# 		self.assertTrue("backend" in question)
	# 		question = self.browser.find_element_by_xpath("//*[@id='faqAccordion']/div[7]/div[1]/h4/a").click()
	# 		answer = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div/div[7]/div[2]/div/p").text
	# 		self.assertTrue("backend" in answer)
	# 		# if question and answer are up, delete this useless QA
	# 		self.browser.get("http://localhost:8000/admin/")
	# 		self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
	# 		question = self.browser.find_element_by_xpath("//*[@id='menu-content']/li[4]/i/a").click()
	# 		delQuestion = self.browser.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/form/div[2]/table/tbody/tr[1]/th/a").click()
	# 		delQuestion = self.browser.find_element_by_xpath("/html/body/div/div[3]/div[1]/form/div/div/p/a").click()
	# 		delQuestion = self.browser.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
	# 		print("FQA test passed!")
	# 	except:
	# 		print("FQA test failed! server down or no internet for now")
	# 		print("Please check or contact us! ")
	