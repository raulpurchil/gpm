from selenium import webdriver
import pytest_check as check

def test_search():
    browser = webdriver.Chrome()
    browser.get('https://www.dnvgl.com/')
    browser.find_element_by_css_selector("button.the-header__panel-toggle--search").click()
    browser.find_element_by_css_selector("input#search-input").send_keys('aerospace')
    browser.find_element_by_css_selector("label[for=search-submit]").click()
    # check expected results
    articles = len(browser.find_elements_by_css_selector("article.post-listed"))
    article_capital_letter = len(browser.find_elements_by_xpath("//h2[contains(text(),'Aerospace')]"))
    article_lower_case = len(browser.find_elements_by_xpath("//h2[contains(text(),'aerospace')]"))
    check.is_true(articles == 5, f"failed to find expected number of articles")
    check.is_true(article_capital_letter == 3, f"failed to find expected number of articles with the word 'aserospace' in the title")
    check.is_true(article_lower_case == 2, f"failed to find expected number of articles with the word 'Aerospace' in the title")
