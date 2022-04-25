import unittest
from user import User
from credentials import Credentials


class TestLocker(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("kabuikariuki", "12139lenana**")

        self.new_account = Credentials("GitHub", "kabuikariuki", "12139**")

    def tearDown(self):
        '''
        does clean up/ destroys entries after each test case has run.
        '''

        User.user_list = []
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "JamesMutahi")
        self.assertEqual(self.new_user.password, "12139lenana**")
        self.assertEqual(self.new_account.account_name, "GitHub")
        self.assertEqual(self.new_account.account_user_name, "JamesMutahi")
        self.assertEqual(self.new_account.account_password, "12139**")

    def test_create_user(self):
        '''
        test_create_user test case to test if the user object is saved into the user list
        '''
        self.new_user.create_user()
        self.assertEqual(len(User.user_list), 1)

    def test_add_credentials(self):
        '''
        test_add_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_account.add_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_create_multiple_users(self):
        '''
        test_create_multiple_users to check if we can create multiple user
        objects to our user list
        '''
        self.new_user.create_user()
        test_user = User("John", "Doe")
        test_user.create_user()
        self.assertEqual(len(User.user_list), 2)

    def test_add_multiple_credentials(self):
        '''
        test_create_multiple_credentials to check if we can create multiple credentials
        objects to our credentials list
        '''
        self.new_account.add_credentials()
        test_credentials = Credentials("Github", "John", "Doe")
        test_credentials.add_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove an account's credentials from our credentials list
        '''
        self.new_account.add_credentials()
        test_credentials = Credentials("Github", "John", "Doe")
        test_credentials.add_credentials()
        self.new_account.delete_credentials("Github")
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_by_account(self):
        '''
        test_find_credentials_by_account to check if we can find an account's credentials by account name and display information
        '''
        self.new_account.add_credentials()
        test_credentials = Credentials("Github", "John", "Doe")
        test_credentials.add_credentials()

        searched_account = Credentials.find_by_account("Github")

        self.assertEqual(searched_account.account_name,
                         test_credentials.account_name)

    def test_display_all_credentials(self):
        '''
        returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_all_accounts(),
                         Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()
