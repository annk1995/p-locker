class User:
    """
    Class to generate instances of users
    """

    user_list = []

    def __init__(self, user_name, password):
        '''
        __init__ method that defines properties for our users objects.
        '''
        self.user_name = user_name
        self.password = password

    def create_user(self):
        '''
        create_user method adds new users objects into user_list
        '''
        User.user_list.append(self)
    