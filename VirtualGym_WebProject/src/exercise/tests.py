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
       
            name = self.browser.find_element_by_id('name')
            name.send_keys("this is a test name")
            video =    self.browser.find_element_by_id('id_exerciseVideos')
                # need absolute path here
                # assume there is a video called "2017_04_03_13_12_34.mp4" under file_path
            pwd = os.getcwd()
            father_path=str(os.path.abspath(os.path.dirname(pwd)+os.path.sep+"."))
            file_path = father_path+("/media_cdn/superxin@vg.ca/2017_04_03_13_12_34.mp4")
            video.send_keys(file_path)
            description = self.browser.find_element_by_id('id_exerciseDescription')
            description.send_keys("this is a test description")
            tag = self.browser.find_element_by_id('id_exerciseTag_4').click()
            tag_text = self.browser.find_element_by_id('id_exTag')
            tag_text.send_keys("tagText")
            submit_ex = self.browser.find_element_by_id("submitExercise").click()
        except:
            print("Test failed! server down or no internet for now")
            print("Please check or contact us! ")


    # test if user can view accepted exercise list
    def test_view_exercise(self):
        try:
            self.browser.get("http://localhost:8000/viewProfile/")
            self.assertIn("http://localhost:8000/viewProfile/", self.browser.current_url)
            tag = self.browser.find_element_by_partial_link_text('   Biceps   tagText ').text
            self.assertEqual('Biceps' in tag, True)
            tag = self.browser.find_element_by_partial_link_text('Biceps').click()
            title = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/h3").text
            self.assertEqual("Detail of Exercise" in title, True)
            tagTest = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/div[1]/div/p").text
            self.assertEqual("Biceps" in tagTest, True)
        except:
            print("Test failed! server down or no internet for now")
            print("Please check or contact us! ")

    # test if moderator can view exercise list
    def test_moderator_view_exercise_list(self):
        try:
            self.browser.get("http://localhost:8000/admin/")
            self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
            username = self.browser.find_element_by_xpath("//*[@id='id_username']")
            username.send_keys("test@vg.ca")
            password = self.browser.find_element_by_xpath("//*[@id='id_password']")
            password.send_keys("admin1234")
            Log_in = self.browser.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()
            exercise = self.browser.find_element_by_xpath("//*[@id='content-main']/div[3]/table/tbody/tr/th/a").click()
            self.assertIn("http://localhost:8000/admin/exercise/exercise/",self.browser.current_url)
        except:
            print("Test failed! server down or no internet for now")
            print("Please check or contact us! ")


    # test if moderator can accept an exercise
    def test_moderator_accept_exercise(self):
        try:
            self.browser.get("http://localhost:8000/admin/")
            self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
            username = self.browser.find_element_by_xpath("//*[@id='id_username']")
            username.send_keys("test@vg.ca")
            password = self.browser.find_element_by_xpath("//*[@id='id_password']")
            password.send_keys("admin1234")
            Log_in = self.browser.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()
            exercise = self.browser.find_element_by_xpath("//*[@id='content-main']/div[3]/table/tbody/tr/th/a").click()
            self.assertIn("http://localhost:8000/admin/exercise/exercise/",self.browser.current_url)
            xinsexe = self.browser.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/th/a").click()
            accept_box = self.browser.find_element_by_xpath("//*[@id='exercise_form']/div/fieldset/div[3]/div/label").click()
            save = self.browser.find_element_by_xpath("//*[@id='exercise_form']/div/div/input[1]").click()
            xinsexe = self.browser.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/th/a").click()
            box = self.browser.find_element_by_xpath("//*[@id='id_exerciseApproved']")
            if_checked = box.is_selected()
            self.assertTrue(if_checked == True)
        except:
            print("Test failed! server down or no internet for now")
            print("Please check or contact us! ")

    # test if moderator can reject an exercise
    def test_moderator_reject_exercise(self):
        try:
            self.browser.get("http://localhost:8000/admin/")
            self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
            username = self.browser.find_element_by_xpath("//*[@id='id_username']")
            username.send_keys("test@vg.ca")
            password = self.browser.find_element_by_xpath("//*[@id='id_password']")
            password.send_keys("admin1234")
            Log_in = self.browser.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()
            exercise = self.browser.find_element_by_xpath("//*[@id='content-main']/div[3]/table/tbody/tr/th/a").click()
            self.assertIn("http://localhost:8000/admin/exercise/exercise/",self.browser.current_url)
            xinsexe = self.browser.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/td[1]/input").click()
            drop_down = self.browser.find_element_by_xpath("//*[@id='changelist-form']/div[1]/label/select").click()
            reject = self.browser.find_element_by_xpath("//*[@id='changelist-form']/div[1]/label/select/option[3]").click()
            go = self.browser.find_element_by_xpath("//*[@id='changelist-form']/div[1]/button").click()
        except:
            print("Test failed! server down or no internet for now")
            print("Please check or contact us! ")
    	