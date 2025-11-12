
from enum import Enum

# TODO: flesh out class
class Speed(object):
  def __init__(self, s):
    self.s = s

  def __repr__(self):
    return self.s
    
class MovementType (Enum):
  B = 'burrow'
  C = 'climb'
  F = 'fly'
  S = 'swim'
  W = 'walk'

