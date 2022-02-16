import pytest
from selenium import webdriver
from tests.selectors import dnvSelectors
driver = None


@pytest.fixture(autouse=True)
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get(dnvSelectors.DNV_URI)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
