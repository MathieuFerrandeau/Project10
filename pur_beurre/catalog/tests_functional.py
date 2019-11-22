"""Functionnal test management"""
import time

from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ConnectionTest(LiveServerTestCase):

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
        time.sleep(0.5)
        redirection_url = self.browser.current_url

        # Check if the after the form validation match the valid redirection
        # url"""
        self.assertEqual(self.live_server_url + '/login/', redirection_url)

class SignUpTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_signup_form_submission_with_enter_keys(self):
        # Open a selenium browser & retrieve the forms elements we want to test
        self.browser.get(str(self.live_server_url) + '/register/')
        username_input = self.browser.find_element_by_id('id_username')
        email_input = self.browser.find_element_by_id('id_email')
        password1_input = self.browser.find_element_by_id('id_password1')
        password2_input = self.browser.find_element_by_id('id_password2')

        username_input.send_keys('test')
        email_input.send_keys('email@test.com')
        password1_input.send_keys('testpass123')
        password2_input.send_keys('testpass123')
        password2_input.send_keys(Keys.ENTER)
        time.sleep(5)
        redirection_url = self.browser.current_url

        self.assertEqual(self.live_server_url + '/',
                         redirection_url)