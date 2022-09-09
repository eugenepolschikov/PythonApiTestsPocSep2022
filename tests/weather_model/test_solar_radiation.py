import requests
import time
import allure
from helpers.api_helper import ApiHelper
from conftest import id_token
from conftest import field_uuid
params = {'datasets': 'history,forecast'}


@allure.feature('Weather Model API')
def test_solar_radiation_daily():
    url = ApiHelper.BASE_URL + 'api/v1/weather/solar_radiation/daily/' + field_uuid
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers, params=params)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/weather/solar_radiation/daily] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code


@allure.feature('Weather Model API')
def test_solar_radiation_monthly():
    url = ApiHelper.BASE_URL + 'api/v1/weather/solar_radiation/monthly/' + field_uuid
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers, params=params)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/weather/solar_radiation/monthly] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code


@allure.feature('Weather Model API')
def test_solar_radiation_alert():
    url = ApiHelper.BASE_URL + 'api/v1/alertsettings/solar_radiation/' + field_uuid
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers, params=params)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/alertsettings/solar_radiation] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code
