import mock
import requests
import unittest


MockedSession = mock.create_autospec(requests.Session, spec_set=True)


class UnitHelper(unittest.TestCase):
    # Sub-classes must assign the class to this during definition
    described_class = None
    # Sub-classes must also assign a dictionary to this during definition
    example_data = {}

    def create_session_mock(self):
        session = MockedSession()
        session.attach_mock(mock.Mock(), 'headers')
        return session

    def setUp(self):
        self.session = self.create_session_mock()
        self.instance = self.described_class(self.example_data, self.session)