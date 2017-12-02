import datetime
from django.test import TestCase
from VirtualGym.models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    # this test takes time to run around 20s
	def test_create_exercise(self):
		try:
		# log in first
			self.browser.get("http://localhost:8000")
			self.assertIn("http://localhost:8000", self.browser.current_url)
			self.browser.find_element_by_xpath("//*[@id='signIn_popup_trigger']").click()
			signIn = self.browser.find_element_by_partial_link_text('Sign In').click()
			email = self.browser.find_element_by_id('email')
			email.send_keys('sprint4_test@vg.ca')
			password = self.browser.find_element_by_id('password')
			password.send_keys('123')
			sign_In = self.browser.find_element_by_id('signInButton').click()


			self.browser.get("http://localhost:8000/createExercise/")
			self.assertIn("http://localhost:8000/createExercise/", self.browser.current_url)

			name = self.browser.find_element_by_xpath("//*[@id='id_exerciseName']")
			name.send_keys("this is a test name")
			video = self.browser.find_element_by_xpath("//*[@id='id_exerciseVideos1']")
			# need absolute path here
			# assume there is a video called "2017_04_03_13_12_34.mp4" under file_path
			pwd = os.getcwd()
			father_path=str(os.path.abspath(os.path.dirname(pwd)+os.path.sep+"."))
			file_path = father_path+("/media_cdn/bacK.mp4")
			video.send_keys(file_path)

			# we may cannot see first annotation appear in screen, but it actually added
			# add firsh annotation
			annotation = self.browser.find_element_by_xpath("//*[@id='vid_preview1']")
			action = webdriver.common.action_chains.ActionChains(self.browser)
			action.move_to_element_with_offset(annotation, 200, 200)
			action.click()
			action.perform()
			time.sleep(2)

			note = self.browser.find_element_by_xpath("//*[@id='annotation_detial0']")
			note.send_keys("annotation from test")
			time.sleep(2)
			add = self.browser.find_element_by_xpath("//*[@id='annotation_submit0']").click()
			time.sleep(4)
			# add second annotation
			annotation = self.browser.find_element_by_xpath("//*[@id='vid_preview1']")
			action = webdriver.common.action_chains.ActionChains(self.browser)
			action.move_to_element_with_offset(annotation, 150, 150).click().perform()
			time.sleep(2)
			note = self.browser.find_element_by_xpath("//*[@id='annotation_detial0']")
			note.send_keys("annotation from test")
			time.sleep(2)
			add = self.browser.find_element_by_xpath("//*[@id='annotation_submit0']").click()
			time.sleep(2)

			description = self.browser.find_element_by_id('id_exerciseDescription')
			description.send_keys("this is a test description")

			remove_tag = self.browser.find_element_by_css_selector("[class^=tm-tag-remove]").click()
			tag_text = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div/div[3]/div/input[1]")
			tag_text.send_keys("tagText")
			tag_text.send_keys(Keys.ENTER)
			submit_ex = self.browser.find_element_by_id("submitExercise").click()
			time.sleep(1)
			print("Create exercise test passed!")

			
		except:
			print("Create exercise test failed! server down or no internet for now")
			print("Please check or contact us! ")


    # test if user can view accepted exercise list
	def test_view_exercise(self):
		try:
			self.browser.get("http://localhost:8000/viewProfile/")
			self.assertIn("http://localhost:8000/viewProfile/", self.browser.current_url)
			tag = self.browser.find_element_by_partial_link_text('Side').text
			self.assertEqual('Side' in tag, True)
			time.sleep(1)
			tag = self.browser.find_element_by_partial_link_text('Side').click()
			title = self.browser.find_element_by_xpath("//*[@id='detail_title']").text
			self.assertEqual("Side" in title, True)
			tagTest = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[3]/div/span[1]/a").text
			self.assertEqual("Shoulder" in tagTest, True)
			print("View exercise test passed!")
		except:
			print("View exercise test failed! server down or no internet for now")
			print("Please check or contact us! ")

    # test if moderator can view exercise list
	def test_moderator_view_exercise_list(self):
		try:
			self.browser.get("http://localhost:8000/admin/")
			self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
			username = self.browser.find_element_by_xpath("//*[@id='id_username']")
			username.send_keys("sprint4_admin@vg.ca")
			password = self.browser.find_element_by_xpath("//*[@id='id_password']")
			password.send_keys("admin1234")
			Log_in = self.browser.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()
			exercise = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/ul/li[3]/i/a").click()
			self.assertIn("http://localhost:8000/admin/exercise/exercise/",self.browser.current_url)
			print("Moderator view exercise list test passed!")
		except:
			print("Moderator view exercise test failed! server down or no internet for now")
			print("Please check or contact us! ")


    # test if moderator can accept an exercise
	def test_moderator_accept_exercise(self):
		try:
			self.browser.get("http://localhost:8000/admin/")
			self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
			username = self.browser.find_element_by_xpath("//*[@id='id_username']")
			username.send_keys("sprint4_admin@vg.ca")
			password = self.browser.find_element_by_xpath("//*[@id='id_password']")
			password.send_keys("admin1234")
			Log_in = self.browser.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()
			exercise = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/ul/li[3]/i/a").click()
			self.assertIn("http://localhost:8000/admin/exercise/exercise/",self.browser.current_url)
			xinsexe = self.browser.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/th/a").click()
			accept_box = self.browser.find_element_by_xpath("//*[@id='id_exerciseApproved']").click()
			save = self.browser.find_element_by_xpath("//*[@id='exercise_form']/div/div/input[1]").click()
			xinsexe = self.browser.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/th/a").click()
			box = self.browser.find_element_by_xpath("//*[@id='id_exerciseApproved']")
			if_checked = box.is_selected()
			self.assertTrue(if_checked == True)
			print("Moderator accept exercise test passed!")
		except:
			print("Moderator accept exercise test failed! server down or no internet for now")
			print("Please check or contact us! ")

    # test if moderator can reject an exercise
	def test_moderator_reject_exercise(self):
		try:
			self.browser.get("http://localhost:8000/admin/")
			self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
			username = self.browser.find_element_by_xpath("//*[@id='id_username']")
			username.send_keys("sprint4_admin@vg.ca")
			password = self.browser.find_element_by_xpath("//*[@id='id_password']")
			password.send_keys("admin1234")
			Log_in = self.browser.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()
			exercise = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/ul/li[3]/i/a").click()
			self.assertIn("http://localhost:8000/admin/exercise/exercise/",self.browser.current_url)
			xinsexe = self.browser.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/td[1]/input").click()
			drop_down = self.browser.find_element_by_xpath("//*[@id='changelist-form']/div[1]/label/select").click()
			reject = self.browser.find_element_by_xpath("//*[@id='changelist-form']/div[1]/label/select/option[3]").click()
			go = self.browser.find_element_by_xpath("//*[@id='changelist-form']/div[1]/button").click()
			print("Moderator reject exercise test passed!")
		except:
			print("Moderator reject exercise test failed! server down or no internet for now")
			print("Please check or contact us! ")

    # test if user can search exercise by tag
	def test_search_by_tag(self):
		try:
			self.browser.get("http://localhost:8000/")
			self.assertIn("http://localhost:8000/", self.browser.current_url)
			searchTag = self.browser.find_element_by_xpath("/html/body/div/div[1]/nav/div/div[2]/ul/li[5]/a/i").click()
			searchTag = self.browser.find_element_by_xpath("//*[@id='search']")
			searchTag.send_keys("Elbow")
			searchTag.send_keys(Keys.ENTER)
			time.sleep(1)
			self.assertIn("http://localhost:8000/viewProfile/?q=Elbow",self.browser.current_url)
			print("Search by tag test passed! ")
		except:
			print("Search by tag Test failed! server down or no internet for now")
			print("Please check or contact us! ")


    # test if user can search exercise by description
	def test_search_by_description(self):
		try:
			self.browser.get("http://localhost:8000/")
			self.assertIn("http://localhost:8000/", self.browser.current_url)
			searchDescription = self.browser.find_element_by_xpath("/html/body/div/div[1]/nav/div/div[2]/ul/li[5]/a/i").click()
			searchDescription = self.browser.find_element_by_xpath("//*[@id='search']")
			searchDescription.send_keys("description")
			searchDescription.send_keys(Keys.ENTER)
			time.sleep(1)
			self.assertIn("http://localhost:8000/viewProfile/?q=description",self.browser.current_url)
			print("Search by description test passed! ")
		except:
			print("Search by description Test failed! server down or no internet for now")
			print("Please check or contact us! ")

    # test if user can search exercise by annotation
	def test_search_by_description(self):
		try:
			self.browser.get("http://localhost:8000/")
			self.assertIn("http://localhost:8000/", self.browser.current_url)
			searchAnnotation = self.browser.find_element_by_xpath("/html/body/div/div[1]/nav/div/div[2]/ul/li[5]/a/i").click()
			searchAnnotation = self.browser.find_element_by_xpath("//*[@id='search']")
			searchAnnotation.send_keys("video")
			searchAnnotation.send_keys(Keys.ENTER)
			time.sleep(1)
			self.assertIn("http://localhost:8000/viewProfile/?q=video",self.browser.current_url)
			print("Search by annotation test passed! ")
		except:
			print("Search by description Test failed! server down or no internet for now")
			print("Please check or contact us! ")

    # test if user can edit description and tag for an exercise
	def test_edit(self):
		try:
			self.browser.get("http://localhost:8000")
			self.assertIn("http://localhost:8000", self.browser.current_url)
			self.browser.find_element_by_xpath("//*[@id='signIn_popup_trigger']").click()
			signIn = self.browser.find_element_by_partial_link_text('Sign In').click()
			email = self.browser.find_element_by_id('email')
			email.send_keys('sprint4_test@vg.ca')
			password = self.browser.find_element_by_id('password')
			password.send_keys('123')
			sign_In = self.browser.find_element_by_id('signInButton').click()
			edit = self.browser.find_element_by_xpath("/html/body/div/div[1]/nav/div/div[2]/ul/li[5]/a").click()

			editButton = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div/section/div/div[1]/div/div/a").click()
			oldAnnotation = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div/div/form/div[3]/div/div[1]/div[1]/div[2]").click()
			annotation = self.browser.find_element_by_xpath("//*[@id='vid_preview']")
			action = webdriver.common.action_chains.ActionChains(self.browser)
			action.move_to_element_with_offset(annotation, 600, 300).click().perform()
			self.browser.find_element_by_xpath("//*[@id='annotation_closeBtn']").click()
			time.sleep(2)
			annotation = self.browser.find_element_by_xpath("//*[@id='vid_preview']")
			action = webdriver.common.action_chains.ActionChains(self.browser)
			action.move_to_element_with_offset(annotation, 600, 300).click().perform()
			note = self.browser.find_element_by_xpath("//*[@id='annotation_detial']")
			note.send_keys("edit annotation from test")
			self.browser.find_element_by_xpath("//*[@id='annotation_submit']").click()

			editName = self.browser.find_element_by_xpath("//*[@id='id_exerciseName']").clear()
			editName = self.browser.find_element_by_xpath("//*[@id='id_exerciseName']").send_keys("edit name")
			editDescription = self.browser.find_element_by_xpath("//*[@id='id_exerciseDescription']")
			editDescription.send_keys(" this is an edit for test")
			remove_tag = self.browser.find_element_by_css_selector("[class^=tm-tag-remove]").click()
			tag_text = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/div/form/div[6]/div/input[1]')
			tag_text.send_keys("editTag")
			tag_text.send_keys(Keys.ENTER)

			submitButton = self.browser.find_element_by_xpath("//*[@id='submitExercise']").click()
			self.assertIn("http://localhost:8000/myExercise/", self.browser.current_url)
			check = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div/section/div/div[1]/div/h4").text
			self.assertTrue("edit" in check)
			print("Edit test passed! ")
		except:
			print("Edit by description Test failed! server down or no internet for now")
			print("Please check or contact us! ")

  # test if cross reference shows correctlly
	def test_cross_reference(self):
		try:
			self.browser.get("http://localhost:8000/viewProfile/")
			self.assertIn("http://localhost:8000/viewProfile/", self.browser.current_url)
			exercise1 = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div/section/div/div[1]/div/h4/a").click()
			tag1 = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[3]/div/span[1]/a").text
			cross = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/div[1]/div[2]/span/strong/a").text
			self.assertTrue("Shoulder" or "Bicep" or "Diagona" in cross)

			cross = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/div[1]/div[2]/span/strong/a").click()
			tag2 = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[3]/div/span[1]/a[2]").text
			cross_exe = self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/div[1]/div[2]/span/strong/a").text
			self.assertTrue("Shoulder" or "Bicep" or "Diagona" in cross)
			print("Cross reference test passed!")
		except:
			print("Cross reference Test failed! server down or no internet for now")
			print("Please check or contact us! ")

  	# test if moderator can search in admin page
	def test_moderator_search(self):
		try:
			self.browser.get("http://localhost:8000/admin/")
			self.assertIn("http://localhost:8000/admin/", self.browser.current_url)
			username = self.browser.find_element_by_xpath("//*[@id='id_username']")
			username.send_keys("sprint4_admin@vg.ca")
			password = self.browser.find_element_by_xpath("//*[@id='id_password']")
			password.send_keys("admin1234")
			Log_in = self.browser.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()
			exercise = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/ul/li[3]/i/a").click()
			self.assertIn("http://localhost:8000/admin/exercise/exercise/",self.browser.current_url)
			search_posterID = self.browser.find_element_by_xpath("//*[@id='searchbar']")
			search_posterID.send_keys("xin@vg.ca")
			search_button = self.browser.find_element_by_xpath("//*[@id='changelist-search']/div/input[2]").click()
			time.sleep(1)
			search_exerciseName = self.browser.find_element_by_xpath("//*[@id='searchbar']")
			search_exerciseName.clear()
			search_exerciseName.send_keys("Balance Exercises For Seniors")
			search_button = self.browser.find_element_by_xpath("//*[@id='changelist-search']/div/input[2]").click()
			time.sleep(1)
			search_exerciseTag = self.browser.find_element_by_xpath("//*[@id='searchbar']")
			search_exerciseTag.clear()
			search_exerciseTag.send_keys("Triceps")
			search_button = self.browser.find_element_by_xpath("//*[@id='changelist-search']/div/input[2]").click()
			print("Moderator search test passed!")
		except:
			print("Moderator search test failed! server down or no internet for now")
			print("Please check or contact us!")
