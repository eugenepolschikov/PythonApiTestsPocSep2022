import requests
import time
import allure
from helpers.api_helper import ApiHelper
from conftest import id_token
from conftest import field_uuid


@allure.feature('Crop service')
def test_stage_dates():
    url = ApiHelper.BASE_URL + 'api/v1/crop/stage_dates/' + field_uuid
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/crop/stage_dates] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code


@allure.feature('Crop service')
def test_stage_estimation():
    url = ApiHelper.BASE_URL + 'api/v1/crop/stage_estimation/' + field_uuid
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/crop/stage_dates] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))
    ApiHelper.LOGGER.info('Server response: [{0}]'.format(r.json()))

    assert 200 == r.status_code
