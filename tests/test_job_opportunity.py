
import pytest_check as check
import pytest

from tests.selectors import dnvSelectors
from tests.helper.generalHelper import generalHelper

_job_opportunities_label = 'Job opportunities'

@pytest.mark.usefixtures("setup")
class TestJob:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.tj = generalHelper()

    def test_job_opportunity(self):
        self.tj.click_link_by_text(f'About us')
        self.tj.click_link_by_text(f'{_job_opportunities_label}')
        self.tj.click_link_by_text(f'View all vacant positions')
        # move to the last opened tab and disable iframe to access it
        self.tj.switch_to.window(self.tj.window_handles[-1])
        self.tj.switch_to_frame(dnvSelectors.DNV_CAREERS_IFRAME_ID)
        self.tj.click_link_by_text(f'{_job_opportunities_label}')
        self.tj.filter_job_by_category_and_location('IT', 'Barcelona')
        self.tj.enter_job_field('engineer')
        self.tj.click_search_button()
        # check results
        results = self.tj.check_result(dnvSelectors.DNV_CAREERS_JOB_ROW)
        location = self.tj.check_result(dnvSelectors.DNV_CARRERS_JOB_ROW_LOCATION_XPATH)
        check.is_true(results == 6, f"failed to find expected number of position")
        check.is_true(location == 6, f"failed to find expected number of position in BCN")