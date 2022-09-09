import requests
import time
import allure
from helpers.api_helper import ApiHelper
from conftest import id_token
from delayed_assert import expect, assert_expectations
import pytest


@allure.feature('Dashboard API')
def test_permissions():
    url = ApiHelper.BASE_URL + 'api/v1/settings/permissions'
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/settings/permissions] ------')
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code


@allure.feature('Dashboard API')
def test_settings_general():
    url = ApiHelper.BASE_URL + 'api/v1/settings/general'
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/settings/general] ------')
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))
    assert 200 == r.status_code


@allure.feature('Dashboard API')
def test_fields():
    url = ApiHelper.BASE_URL + 'api/v1/fields'
    headers = {'Content-Type': 'application/json', 'user-token': id_token}

    start = time.time()
    r = requests.get(url, headers=headers)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/fields] ------')
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))
    assert 200 == r.status_code


@allure.feature('Dashboard API')
def test_mapbox_outdoors():
    url = 'https://api.mapbox.com/styles/v1/mapbox/outdoors-v11'
    headers = {'Content-Type': 'application/json'}
    params = {'access_token': ApiHelper.MBOX_KEY}

    start = time.time()
    r = requests.get(url, headers=headers, params=params)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [{0}] ------'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))
    assert 200 == r.status_code


@allure.feature('Dashboard API')
def test_mapbox_streets():
    url = 'https://api.mapbox.com/v4/mapbox.mapbox-streets-v8,mapbox.mapbox-terrain-v2.json'
    headers = {'Content-Type': 'application/json'}
    params = {'secure': '', 'access_token': ApiHelper.MBOX_KEY}

    start = time.time()
    r = requests.get(url, headers=headers, params=params)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [{0}] ------'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))
    assert 200 == r.status_code


@allure.feature('Dashboard API')
def test_mapbox_sprites():
    url_sprite_json = 'https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/sprite@2x.json'
    url_sprite_png = 'https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/sprite@2x.png'
    headers = {'Content-Type': 'application/json'}
    params = {'secure': '', 'access_token': ApiHelper.MBOX_KEY}

    start_json = time.time()
    resp_json = requests.get(url_sprite_json, headers=headers, params=params)
    request_time_json = time.time() - start_json

    start_png = time.time()
    resp_png = requests.get(url_sprite_png, headers=headers, params=params)
    request_time_png = time.time() - start_png

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [{0}] ------'.format(url_sprite_json))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(resp_json.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time_json))
    expect(200 == resp_json.status_code)

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [{0}] ------'.format(url_sprite_png))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(resp_png.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time_png))
    expect(200 == resp_json.status_code)

    assert_expectations()


@pytest.mark.skip('Need to fix')
@allure.feature('Dashboard API')
def test_multiple_ndvimaps():
    uuids = ','.join(ApiHelper.get_all_fields_uuid(id_token))
    base_url = ApiHelper.BASE_URL + 'api/v1/maps/multiple_ndvimaps'
    header = {'Content-Type': 'application/json', 'user-token': id_token}
    params = {'field_ids': uuids}
    url = base_url + '?' + '&'.join(["{}={}".format(k, v) for k, v in params.items()])

    start = time.time()
    r = requests.get(url, headers=header)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('!!!!!!!!!: {0}'.format(r.request.path_url))

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [{0}] ------'.format(r.request.url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))

    assert 200 == r.status_code
