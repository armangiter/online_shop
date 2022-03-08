import json
from requests import post
from django.contrib.auth.mixins import UserPassesTestMixin


def send_otp_code(phone, code):
    pass
    # data = {
    #     "op": "pattern",
    #     "user": "",
    #     "pass": "",
    #     "fromNum": "3000505",
    #     "toNum": phone,
    #     "patternCode": "yrvco2gken",
    #     "inputData": [
    #         {
    #             "code": code
    #         }
    #     ]
    # }
    # post(url='https://ippanel.com/api/select', data=json.dumps(data))


class IsNotAuthenticatedUserMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated


