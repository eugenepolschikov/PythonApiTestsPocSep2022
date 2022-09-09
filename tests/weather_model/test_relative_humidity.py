import requests
import time
import allure
from helpers.api_helper import ApiHelper
from conftest import id_token
from conftest import field_uuid
params = {'datasets': 'history,forecast'}


@allure.feature('Weather Model API')
def test_relative_humidity_daily():
    url = ApiHelper.BASE_URL + 'api/v1/weather/relative_humidity/daily/' + field_uuid
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers, params=params)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/weather/relative_humidity/daily] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code


@allure.feature('Weather Model API')
def test_relative_humidity_monthly():
    url = ApiHelper.BASE_URL + 'api/v1/weather/relative_humidity/monthly/' + field_uuid
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers, params=params)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/weather/relative_humidity/monthly] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code


@allure.feature('Weather Model API')
def test_relative_humidity_alert():
    url = ApiHelper.BASE_URL + 'api/v1/alertsettings/relative_humidity/' + field_uuid
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers, params=params)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/alertsettings/relative_humidity] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code
