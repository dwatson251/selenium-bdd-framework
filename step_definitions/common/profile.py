import json


class Profile:

    def __init__(self, profile_name):
        """
        Given a profile name

        :param profile_name:
        """
        self.profile_name = profile_name

        try:
            with open('resources/user_profiles/' + self.profile_name + '.json', 'r') as f:
                self.profile = json.load(f)
        except IOError as error:
            print(error)

    def get_profile(self):
        """
        Obtains the profile json

        :return:
        """
        return self.profile
