from tests.selectors import dnvSelectors


class generalHelper():
    textbox_username_id = "user"
    textbox_password_id = "pass"
    button_login_xpath = "//input[@value='Log In']"
    get_error_text_xpath = "//p[@class='error']"

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def _isXpath(locator):
        if ("/" in locator[:2]):
            return True
        return False

    def enter_search_field(self, word_to_search):
        self.driver.find_element_by_css_selector(dnvSelectors.DNV_SEARCH_HEADER_INPUT).send_keys(word_to_search)

    def enter_job_field(self, job_to_search):
        self.driver.find_element_by_css_selector(dnvSelectors.DNV_CAREERS_SEARCH_INPUT).send_keys(job_to_search)

    def click_search_header_button(self):
        self.driver.find_element_by_css_selector(dnvSelectors.DNV_SEARCH_HEADER_BUTTON).click()

    def click_search_button(self):
        self.driver.find_element_by_css_selector(dnvSelectors.DNV_SEARCH_SUBMIT_BUTTON).click()

    def click_link_by_text(self, text):
        self.driver.find_element_by_css_selector(dnvSelectors.DNV_TITLE_LINK.replace(f"{dnvSelectors.DNV_REPLACEMENT_PARAMETER}", f"{text}")).click()

    def filter_job_by_category_and_location(self, category, location):
        self.driver.find_element_by_css_selector(dnvSelectors.DNV_CAREERS_CATEGORY_FILTER).click()
        self.driver.find_element_by_css_selector(dnvSelectors.DNV_CAREERS_FILTER_OPTION.replace(f"{dnvSelectors.DNV_REPLACEMENT_PARAMETER}", f"{category}")).click()
        self.driver.find_element_by_css_selector(dnvSelectors.DNV_CAREERS_LOCATION_FILTER).click()
        self.driver.find_element_by_css_selector(dnvSelectors.DNV_CAREERS_FILTER_OPTION.replace(f"{dnvSelectors.DNV_REPLACEMENT_PARAMETER}", f"{location}")).click()

    def check_result(self, selector):
        if generalHelper._isXpath(selector):
            count_selector = len(self.driver.find_element_by_xpath(selector))
        else:
            count_selector = len(self.driver.find_element_by_css_selector(selector))
        return count_selector

