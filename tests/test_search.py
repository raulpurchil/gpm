import pytest_check as check
import pytest

from tests.selectors import dnvSelectors
from tests.helper.generalHelper import generalHelper

_aerospace = 'aerospace'
_Aerospace = 'Aerospace'

@pytest.mark.usefixtures("setup")
class TestSearch:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ts = generalHelper()

    def test_search_browser(self):
        self.ts.click_search_header_button()
        self.ts.enter_search_field('aerospace')
        self.ts.click_search_button()
        #check results
        articles = self.ts.check_result(dnvSelectors.DNV_SEARCH_SECTION_ARTICLE)
        article_capital_letter = self.ts.check_result(dnvSelectors.DNV_SEARCH_SECTION_ARTICLE_LABEL.replace(f"{dnvSelectors.DNV_REPLACEMENT_PARAMETER}", f"{_aerospace}"))
        article_lower_case = self.ts.check_result(dnvSelectors.DNV_SEARCH_SECTION_ARTICLE_LABEL.replace(f"{dnvSelectors.DNV_REPLACEMENT_PARAMETER}", f"{_Aerospace}"))
        check.is_true(articles == 5, f"failed to find expected number of articles")
        check.is_true(article_capital_letter == 3, f"failed to find expected number of articles with the word 'aserospace' in the title")
        check.is_true(article_lower_case == 2, f"failed to find expected number of articles with the word 'Aerospace' in the title")
