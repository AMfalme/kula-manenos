"""This module manages user information """
class Users(object):
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name
		self.preferences=[]

	def create_preference(self,pref):
		return self.preferences.append(pref)