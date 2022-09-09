from helpers.api_helper import ApiHelper

id_token = ApiHelper.get_id_token()
field_uuid = ApiHelper.get_random_field_uuid(id_token)
