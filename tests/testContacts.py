import unittest
from dwolla import contacts, rest
from mock import MagicMock


class ContactsTest(unittest.TestCase):
    def setUp(self):
        rest.r._get = MagicMock()
        rest.r._post = MagicMock()
        rest.r.settings['client_id'] = "SOME ID"
        rest.r.settings['client_secret'] = "SOME ID"
        rest.r.settings['oauth_token'] = "AN OAUTH TOKEN"

    def testget(self):
        contacts.get({'a': 'parameter'})
        rest.r._get.assert_any_call('/contacts/', {'a': 'parameter', 'oauth_token': 'AN OAUTH TOKEN'})

    def testnearby(self):
        contacts.nearby(45, 50, {'another': 'parameter'})
        rest.r._get.assert_any_call('/contacts/nearby/', {'latitude': 45, 'client_secret': 'SOME ID', 'another': 'parameter', 'client_id': 'SOME ID', 'longitude': 50})

if __name__ == '__main__':
    unittest.main()