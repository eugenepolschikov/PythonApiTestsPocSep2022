import requests
import time
import allure
from helpers.api_helper import ApiHelper
from conftest import id_token


@allure.feature('Decision tools service')
def test_get_labels():
    url = ApiHelper.BASE_URL + 'api/v1/decision_tools/settings/{field_id}'
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/labels] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code
