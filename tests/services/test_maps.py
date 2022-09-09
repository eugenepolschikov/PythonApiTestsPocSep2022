import requests
import time
import allure
from helpers.api_helper import ApiHelper
from conftest import id_token
from conftest import field_uuid


@allure.feature('Maps service')
def test_get_multiple_ndvimaps():
    # url = ApiHelper.BASE_URL + 'api/v1/maps/multiple_ndvimaps/'
    url = 'https://dashboard-api-staging-4cs2xbqdra-uc.a.run.app/api/v1/maps/multiple_ndvimaps?field_ids=-MhJhmwWtt9q8nLpiC9j,-MhJhmok4vYsKcgFFiyt,-MhJhmgtgoEOlfrT0gEs,-MhJhmZTda2GdLdwOfIk,-MhJhmSF_zSTtRm1btyp,-MhJhmKp6m-CBNUy3K9q,-MhJhmC8ruaY_xm4VPze,-MhJhm4QQLohAgMCBBiq,-MhJhlwO1qP-q4ll1dHJ,-MhJhlmaEab482u9HpJp,-MhJhlceCaWTEEgWillw,-MhJhlVbbMfOwqgv9tSv,-MhJhl4pJuEqaI_92SvY,-MhJhkyfzxVFKUp4vkF-,-MhJhkrceIWGKQgMfqZl,-MhJhkjh12EHklfpAQnq,-MhJhkbwM0EoFgn1dK42,-MhJhkU-HK5J0lW9kDaQ,-MhJhkM9GMERPyrgPVYr,-MhJhkDCyeDFtiMYFUks,-MhJhk58DozJNKwBGhFh,-MhJhjx377KUFTe4-93K,-MhJhjokvDFEAdqFepr5,-MhJhjeTlXVctwvlzvsD,-MhJhjX37_5WBCcDhG4Z,-MhJhjOvhH_QczTA1JXB,-MhJhjGiy9EFZg0sSSRZ,-MhJhj8sk2oJsIRi_G15,-MhJhj0OufECHOkSBwXJ,-MhJhibVpW5pfHxIckas,-MhJhiDvabJJf44YSNjc,-MhJhi5U3dUK71YciO9o,-MhJhhyCA0-FDARJ8Y6m,-MhJhhot2d0xOZHGEBaO,-MhJhhg_ixs08ruMk2K8,-MhJhhYtCiD8SohyBgcf,-MhJhhRT9eM--JREPCZI,-MhJhhJ_q7qXyII8KvIz,-MhJhhBGbU3qhsc_h29N,-MhJhh2WePF2n-AJjG-i,-MhJhgf9UZ0uw-0yBKSd,-MhJhgTnoNHgMljSeUXf,-MhJhgLZt2EV7lWTpRWM,-MhJhgBY2FZMrV9s3gKP&'
    headers = {'user-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjNhYTE0OGNkMDcyOGUzMDNkMzI2ZGU1NjBhMzVmYjFiYTMyYTUxNDkiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQXV0b21hdGlvbiBUZXN0IFVzZXIiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY2xpbWF0ZWFpLXN0YWdpbmctZGFzaGJvYXJkIiwiYXVkIjoiY2xpbWF0ZWFpLXN0YWdpbmctZGFzaGJvYXJkIiwiYXV0aF90aW1lIjoxNjQzMDMzNDQ5LCJ1c2VyX2lkIjoiUUZ1akhQQUVZOWVrM2NaMzgxS0NZUWlSOXNtMiIsInN1YiI6IlFGdWpIUEFFWTllazNjWjM4MUtDWVFpUjlzbTIiLCJpYXQiOjE2NDMzMjMxNjYsImV4cCI6MTY0MzMyNjc2NiwiZW1haWwiOiJhdXRvbWF0aW9udGVzdGVyQGNsaW1hdGUuYWkiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiYXV0b21hdGlvbnRlc3RlckBjbGltYXRlLmFpIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.N6loX_zDr9Ttyk0j_sSg7xqpll6QyJ7gO0dbTHqrqjCxfdQyELKLy_Lfh6dsvPu3FduqP99xPXZidxuuOLY8n9Xb0qP8KVxAaiQJTXYCG0vYBvUQJmrFrbf2j184HZjFTQ_0ROyco00QCbxPfL06iebu2QVKFAFH_UpnpDDvvokXdS6NRG4uUIHh1Q-E9PREOAQDBR1oJb9DPh1x0pBMZlDUrkzkFZoQw2kDAdJPegs_fkwRiAtacCB4mXrE-hXGgZfkKa2kuNrZzpSv1LWrpbolhjvtnBwOpqQw-TAGTihqoY3nFCcEE2ZMsTb7EWjVQvV6d_Iu8HQ3z2-c69RWGQ'}
    # params = {'field_ids': [field_uuid]}
    # params = {'field_ids': '-MhJhmwWtt9q8nLpiC9j,-MhJhmok4vYsKcgFFiyt,-MhJhmgtgoEOlfrT0gEs,-MhJhmZTda2GdLdwOfIk,-MhJhmSF_zSTtRm1btyp,-MhJhmKp6m-CBNUy3K9q,-MhJhmC8ruaY_xm4VPze,-MhJhm4QQLohAgMCBBiq,-MhJhlwO1qP-q4ll1dHJ,-MhJhlmaEab482u9HpJp,-MhJhlceCaWTEEgWillw,-MhJhlVbbMfOwqgv9tSv,-MhJhl4pJuEqaI_92SvY,-MhJhkyfzxVFKUp4vkF-,-MhJhkrceIWGKQgMfqZl,-MhJhkjh12EHklfpAQnq,-MhJhkbwM0EoFgn1dK42,-MhJhkU-HK5J0lW9kDaQ,-MhJhkM9GMERPyrgPVYr,-MhJhkDCyeDFtiMYFUks,-MhJhk58DozJNKwBGhFh,-MhJhjx377KUFTe4-93K,-MhJhjokvDFEAdqFepr5,-MhJhjeTlXVctwvlzvsD,-MhJhjX37_5WBCcDhG4Z,-MhJhjOvhH_QczTA1JXB,-MhJhjGiy9EFZg0sSSRZ,-MhJhj8sk2oJsIRi_G15,-MhJhj0OufECHOkSBwXJ,-MhJhibVpW5pfHxIckas,-MhJhiDvabJJf44YSNjc,-MhJhi5U3dUK71YciO9o,-MhJhhyCA0-FDARJ8Y6m,-MhJhhot2d0xOZHGEBaO,-MhJhhg_ixs08ruMk2K8,-MhJhhYtCiD8SohyBgcf,-MhJhhRT9eM--JREPCZI,-MhJhhJ_q7qXyII8KvIz,-MhJhhBGbU3qhsc_h29N,-MhJhh2WePF2n-AJjG-i,-MhJhgf9UZ0uw-0yBKSd,-MhJhgTnoNHgMljSeUXf,-MhJhgLZt2EV7lWTpRWM,-MhJhgBY2FZMrV9s3gKP'}

    start = time.time()
    r = requests.get(url, headers=headers)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/maps/multiple_ndvimaps] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.text))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.json()))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.headers))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.url))

    assert 200 == r.status_code


@allure.feature('Maps service')
def test_get_ndvimap():
    # url = ApiHelper.BASE_URL + 'api/v1/maps/ndvimap/'
    url = 'https://dashboard-api-staging-4cs2xbqdra-uc.a.run.app/api/v1/maps/ndvimap?uuid=-MhJhmok4vYsKcgFFiyt'
    #headers = {'user-token': id_token}
    headers = {
        'user-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjNhYTE0OGNkMDcyOGUzMDNkMzI2ZGU1NjBhMzVmYjFiYTMyYTUxNDkiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQXV0b21hdGlvbiBUZXN0IFVzZXIiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY2xpbWF0ZWFpLXN0YWdpbmctZGFzaGJvYXJkIiwiYXVkIjoiY2xpbWF0ZWFpLXN0YWdpbmctZGFzaGJvYXJkIiwiYXV0aF90aW1lIjoxNjQzMDMzNDQ5LCJ1c2VyX2lkIjoiUUZ1akhQQUVZOWVrM2NaMzgxS0NZUWlSOXNtMiIsInN1YiI6IlFGdWpIUEFFWTllazNjWjM4MUtDWVFpUjlzbTIiLCJpYXQiOjE2NDMzMjMxNjYsImV4cCI6MTY0MzMyNjc2NiwiZW1haWwiOiJhdXRvbWF0aW9udGVzdGVyQGNsaW1hdGUuYWkiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiYXV0b21hdGlvbnRlc3RlckBjbGltYXRlLmFpIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.N6loX_zDr9Ttyk0j_sSg7xqpll6QyJ7gO0dbTHqrqjCxfdQyELKLy_Lfh6dsvPu3FduqP99xPXZidxuuOLY8n9Xb0qP8KVxAaiQJTXYCG0vYBvUQJmrFrbf2j184HZjFTQ_0ROyco00QCbxPfL06iebu2QVKFAFH_UpnpDDvvokXdS6NRG4uUIHh1Q-E9PREOAQDBR1oJb9DPh1x0pBMZlDUrkzkFZoQw2kDAdJPegs_fkwRiAtacCB4mXrE-hXGgZfkKa2kuNrZzpSv1LWrpbolhjvtnBwOpqQw-TAGTihqoY3nFCcEE2ZMsTb7EWjVQvV6d_Iu8HQ3z2-c69RWGQ'}
    params = {'uuid': field_uuid}

    start = time.time()
    r = requests.get(url, headers=headers)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/maps/ndvimap] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.text))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.json()))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.headers))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.url))

    assert 200 == r.status_code


@allure.feature('Maps service')
def test_get_ndvivalues():
    # url = ApiHelper.BASE_URL + 'api/v1/maps/ndvivalues/'
    url = 'https://dashboard-api-staging-4cs2xbqdra-uc.a.run.app/api/v1/maps/ndvivalues?uuid=-MhJhmok4vYsKcgFFiyt'
    # headers = {'user-token': id_token}
    headers = {
        'user-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjNhYTE0OGNkMDcyOGUzMDNkMzI2ZGU1NjBhMzVmYjFiYTMyYTUxNDkiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQXV0b21hdGlvbiBUZXN0IFVzZXIiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY2xpbWF0ZWFpLXN0YWdpbmctZGFzaGJvYXJkIiwiYXVkIjoiY2xpbWF0ZWFpLXN0YWdpbmctZGFzaGJvYXJkIiwiYXV0aF90aW1lIjoxNjQzMDMzNDQ5LCJ1c2VyX2lkIjoiUUZ1akhQQUVZOWVrM2NaMzgxS0NZUWlSOXNtMiIsInN1YiI6IlFGdWpIUEFFWTllazNjWjM4MUtDWVFpUjlzbTIiLCJpYXQiOjE2NDMzMjMxNjYsImV4cCI6MTY0MzMyNjc2NiwiZW1haWwiOiJhdXRvbWF0aW9udGVzdGVyQGNsaW1hdGUuYWkiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiYXV0b21hdGlvbnRlc3RlckBjbGltYXRlLmFpIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.N6loX_zDr9Ttyk0j_sSg7xqpll6QyJ7gO0dbTHqrqjCxfdQyELKLy_Lfh6dsvPu3FduqP99xPXZidxuuOLY8n9Xb0qP8KVxAaiQJTXYCG0vYBvUQJmrFrbf2j184HZjFTQ_0ROyco00QCbxPfL06iebu2QVKFAFH_UpnpDDvvokXdS6NRG4uUIHh1Q-E9PREOAQDBR1oJb9DPh1x0pBMZlDUrkzkFZoQw2kDAdJPegs_fkwRiAtacCB4mXrE-hXGgZfkKa2kuNrZzpSv1LWrpbolhjvtnBwOpqQw-TAGTihqoY3nFCcEE2ZMsTb7EWjVQvV6d_Iu8HQ3z2-c69RWGQ'}

    # params = {'uuid': field_uuid}

    start = time.time()
    r = requests.get(url, headers=headers)
    request_time = time.time() - start

    ApiHelper.LOGGER.info('------ TEST: Check endpoint [api/v1/maps/ndvivalues] ------')
    ApiHelper.LOGGER.info('URL: [{0}]'.format(url))
    ApiHelper.LOGGER.info('Server response status code: [{0}]'.format(r.status_code))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(request_time))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.text))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.json()))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.headers))
    ApiHelper.LOGGER.info('Server response time: [{0}] seconds'.format(r.url))

    assert 200 == r.status_code
