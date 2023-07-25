import pytest
import re


from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_acme_bank_login(page :Page):

    #Arrange
    page.goto("https://demo.applitools.com")

    #Act
    page.locator("id=username").fill('andy')
    page.locator("id=password").fill('i<3pandas')
    page.locator('id=log-in').click()

    #Assert
    expect(page.locator('div.logo-w')).to_be_visible()
    