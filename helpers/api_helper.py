import requests
import allure
import logging
import configparser
from random import randrange


class ApiHelper:
    LOGGER = logging.getLogger(__name__)
    parser = configparser.ConfigParser()
    parser.read('pytest.ini')

    EMAIL = parser.get('env', 'email')
    PASSWORD = parser.get('env', 'password')
    BASE_URL = parser.get('env', 'base_url')
    MBOX_KEY = parser.get('env', 'mapbox_token')

    @staticmethod
    @allure.step('Get Id Token')
    def get_id_token():
        url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword'
        key = ApiHelper.parser.get('env', 'googleapis_key')

        r = requests.post(url, params={'key': key}, data={"email": ApiHelper.EMAIL, "password": ApiHelper.PASSWORD,
                                                          "returnSecureToken": 'true'})
        ApiHelper.LOGGER.info('------ GET ID TOKEN ------')
        ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
        assert 200 == r.status_code
        token = r.json()['idToken']
        ApiHelper.LOGGER.info('Token: {0}'.format(token))
        assert len(token) != 0

        return token

    @staticmethod
    @allure.step('Get Random Field UUID')
    def get_random_field_uuid(id_token):
        url = ApiHelper.BASE_URL + 'api/v1/fields/'
        headers = {'Content-Type': 'application/json', 'user-token': id_token}

        r = requests.get(url, headers=headers)

        assert 200 == r.status_code

        data = r.json()
        random_index = randrange(0, len(data['data']) - 1)
        uuid = data['data'][random_index]['uuid']

        ApiHelper.LOGGER.info('FIELD UUID: {0}'.format(uuid))

        return uuid

    @staticmethod
    @allure.step('Get All Fields UUID')
    def get_all_fields_uuid(id_token):
        url = ApiHelper.BASE_URL + 'api/v1/fields/'
        headers = {'Content-Type': 'application/json', 'user-token': id_token}
        uuids = []

        r = requests.get(url, headers=headers)

        assert 200 == r.status_code

        uuid_data = r.json()['data']

        for uuid in uuid_data:
            uuids.append(uuid['uuid'])

        uuids.reverse()

        return uuids
