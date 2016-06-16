class Users(object):
    """models a users name and preferences"""

    def __init__(self, name):
        self.name = name
        self.preferences = []

    def create_preference(self, pref):
        return self.preferences.append(pref)
