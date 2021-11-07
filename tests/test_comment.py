import unittest
from app.db_class import Comment ,Pitch
from app import db

class commentTest(unittest.TestCase):
  def setUp(self):
    self.new_pitch=Pitch