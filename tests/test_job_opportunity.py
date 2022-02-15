
from selenium import webdriver
import pytest_check as check

def test_job_opportunity():
    browser = webdriver.Chrome()
    browser.get('https://www.dnvgl.com/')
    browser.find_element_by_css_selector("a[title='About us']").click()
    browser.find_element_by_css_selector("a[title='Job opportunities']").click()
    browser.find_element_by_css_selector("a[title='View all vacant positions']").click()
    # navigate to the last opened tab
    browser.switch_to.window(browser.window_handles[-1])
    browser.switch_to_frame("#icims_content_iframe")
    browser.find_element_by_css_selector("select#jsb_f_position_s").click()
    browser.find_element_by_css_selector("a[title='Job opportunities']").click()
    browser.find_element_by_css_selector("option[value='8730']").click()
    browser.find_element_by_css_selector("select#jsb_f_location_s").click()
    browser.find_element_by_css_selector("option[value='13611--Barcelona']").click()
    browser.find_element_by_css_selector("input#jsb_f_keywords_i").send_keys('engineer')
    browser.find_element_by_css_selector("input#jsb_form_submit_i").click()
    # check expected results
    results = len(browser.find_elements_by_css_selector("div.iCIMS_JobsTable div.row"))
    location = len(browser.find_elements_by_xpath("//div[contains(@class,'iCIMS_JobsTable')]//span[text()='ES-Barcelona']"))
    check.is_true(results == 6, f"failed to find expected number of position")
    check.is_true(location == 6, f"failed to find expected number of position in BCN")