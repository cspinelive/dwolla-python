import unittest

from dwolla import request, constants
from mock import MagicMock


class RequestTest(unittest.TestCase):
    def setUp(self):
        request.r._get = MagicMock()
        request.r._post = MagicMock()
        constants.client_id = "SOME ID"
        constants.client_secret = "SOME ID"
        constants.access_token = "AN OAUTH TOKEN"

    def testcreate(self):
        request.create('812-123-1234', 5.50, a='parameter')
        request.r._post.assert_any_call('/requests/', {'sourceId': '812-123-1234', 'a': 'parameter', 'amount': 5.5}, authorization='AN OAUTH TOKEN', dwollaparse='dwolla')

    def testget(self):
        request.get(another='parameter')
        request.r._get.assert_any_call('/requests', {'another': 'parameter'}, authorization='AN OAUTH TOKEN', dwollaparse='dwolla')

    def testinfo(self):
        request.info('654321')
        request.r._get.assert_any_call('/requests/654321', {}, authorization='AN OAUTH TOKEN', dwollaparse='dwolla')

    def testcancel(self):
        request.cancel('12345')
        request.r._post.assert_any_call('/requests/12345/cancel/', {}, authorization='AN OAUTH TOKEN', dwollaparse='dwolla')

    def testfulfill(self):
        request.fulfill('12345', 13.37, a='parameter')
        request.r._post.assert_any_call('/requests/12345/fulfill', {'a': 'parameter', 'amount': 13.37, 'pin': 1234}, authorization='AN OAUTH TOKEN', dwollaparse='dwolla')


if __name__ == '__main__':
    unittest.main()