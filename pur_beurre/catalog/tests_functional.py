"""Functionnal test management"""
import time

from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UserTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        User.objects.create_user(username='test',
                                 password='test1234',
                                 email='test@mail.com')

    def tearDown(self):
        self.browser.quit()

    def test_login_form_submission_with_button(self):
        # Open a selenium browser & retrieve the forms elements we want to test
        self.browser.get(str(self.live_server_url) + '/login/')
        username_input = self.browser.find_element_by_id('id_username')
        password_input = self.browser.find_element_by_id('id_password')
        submission_button = self.browser.find_element_by_class_name(
                'btn-primary')

        # Fill the forms input and click the submit button
        username_input.send_keys('test')
        password_input.send_keys('test1234')
        submission_button.click()
        time.sleep(2)
        redirection_url = self.browser.current_url
        time.sleep(2)

        # Check if the after the form validation match the valid redirection
        # url
        self.assertEqual(self.live_server_url + '/login/', redirection_url)