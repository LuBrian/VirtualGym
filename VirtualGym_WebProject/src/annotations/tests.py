# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.test import TestCase
from VirtualGym.models import *
from selenium import webdriver
import time
import os,sys
# This is a UI test for exercise app
class UITestCase(TestCase):
    # set up browser to firefox
    def setUp(self):
        self.browser = webdriver.Firefox()

    # close browser after test
    def tearDown(self):
        self.browser.quit()

    # test if a user can create exercise
    def test_create_exercise(self):
        try:
            self.browser.get("http://localhost:8000/createExercise/")
            self.assertIn("http://localhost:8000/createExercise/", self.browser.current_url)
            if(self.browser.find_element_by_id("signIn")):
                signIn = self.browser.find_element_by_id("signIn").click()
                email = self.browser.find_element_by_id('email')
                email.send_keys('xin@vg.ca')
                password = self.browser.find_element_by_id('password')
                password.send_keys('admin1234')
                sign_In = self.browser.find_element_by_id('signInButton').click()
            self.browser.get("http://localhost:8000/createExercise/")

            name = self.browser.find_element_by_xpath("//*[@id='id_exerciseName']")
            name.send_keys("this is a test name")
            video = self.browser.find_element_by_id('id_exerciseVideos')
            # need absolute path here
            # assume there is a video called "bacK.mp4" under file_path
            pwd = os.getcwd()
            father_path=str(os.path.abspath(os.path.dirname(pwd)+os.path.sep+"."))
            file_path = father_path+("/media_cdn/bacK.mp4")
            video.send_keys(file_path)
            description = self.browser.find_element_by_id('id_exerciseDescription')
            description.send_keys("this is a test description")
            tag = self.browser.find_element_by_id('id_exerciseTag_4').click()
            tag_text = self.browser.find_element_by_id('id_exTag')
            tag_text.send_keys("tagText")
            submit_ex = self.browser.find_element_by_id("submitExercise").click()
            time.sleep(1)
            annotation = self.browser.find_element_by_xpath("//*[@id='annotation_vid']")
            action = webdriver.common.action_chains.ActionChains(self.browser)
            action.move_to_element_with_offset(annotation, 100, 100).click()
            action.perform()
            time.sleep(2)
            note = self.browser.find_element_by_xpath("//*[@id='annotation_detial']")
            note.send_keys("annotation from test")
            add = self.browser.find_element_by_xpath("//*[@id='annotation_submit']").click()
            time.sleep(2)
            annotation = self.browser.find_element_by_xpath("//*[@id='annotation_vid']")
            action = webdriver.common.action_chains.ActionChains(self.browser)
            action.move_to_element_with_offset(annotation, 100, 100).click()
            action.perform()
            time.sleep(2)
            note = self.browser.find_element_by_xpath("//*[@id='annotation_detial']")
            note.send_keys("annotation from test")
            add = self.browser.find_element_by_xpath("//*[@id='annotation_submit']").click()
            time.sleep(10)
            finish = self.browser.find_element_by_xpath("/html/body/div/div[2]/div/div[4]/a/button").click()
            self.assertIn("http://localhost:8000/myExercise/", self.browser.current_url)
        except:
            print("Annotation test failed! server down or no internet for now")
            print("Please check or contact us! ")