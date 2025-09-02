
from enum import Enum

from model.roll import Roll
from model.range import Range
from model.attribute import Attribute
from model.xml_entity import XmlEntity


class WeaponProperty (Enum):
  A = 'ammunition'
  F = 'finesse'
  H = 'heavy'
  L = 'light'
  LD = 'loading'
  R = 'reach'
  S = 'special'
  T = 'thrown'
  TH = 'two-handed'
  V = 'versatile'
  M = 'martial weapon'

  def __str__(self):
    return self.value
  
  @staticmethod
  def of_value(s):
    if s == '2H':
      s = 'TH'
    try:
      return WeaponProperty.__getitem__(s)
    except Exception as ex:
      raise ValueError("No enum value available for string [%s]" % s)


class DamageType (Enum):
  B = 'bludgeoning'
  P = 'piercing'
  S = 'slashing'
  A = 'acid'
  C = 'cold'
  F = 'fire'
  FC = 'force'
  L = 'lightning'
  N = 'necrotic'
  PS = 'poison'
  R = 'radiant'
  T = 'thunder'

  def __str__(self):
    return self.value
  
  @staticmethod
  def of_value(s):
    try:
      return DamageType.__getitem__(s)
    except Exception as ex:
      raise ValueError("No enum value available for string [%s]" % s)


class ItemCategory (Enum):
  LA = "light armor"
  MA = "medium armor"
  HA = "heavy armor"
  S = "shield"
  M = "melee weapon"
  R = "ranged weapon"
  A = "ammunition"
  RD = "rod"
  ST = "staff"
  WD = "wand"
  RG = "ring"
  P = "potion"
  SC = "scroll"
  W = "wondrous item"
  G = "adventuring gear"
  MON = "money"

  def __str__(self):
    return self.value
  
  @staticmethod
  def of_value(s):
    if s == '$':
      s = 'MON'
    try:
      return ItemCategory.__getitem__(s)
    except Exception as ex:
      raise ValueError("No enum value available for string [%s]" % s)


class Item (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    self.name = self._get('name')
    self.type = self._get_as_obj('type', ItemCategory.of_value)
    self.value = self._get_as_obj('value', float, 0)
    self.weight = self._get_as_obj('weight', float, 0)
    self.text = self._get('text', '')
    self.armor_class = self._get_as_obj('ac', int, 0)
    self.strength = self._get_as_obj('strength', int, 0)
    self.stealth = self._get_as_bool('stealth', False)
    self.dmg1 = self._get_as_obj('dmg1', Roll)
    self.dmg2 = self._get_as_obj('dmg2', Roll)
    self.dmgType = self._get_as_obj('dmgType', DamageType.of_value)
    self.properties = self._get_as_list('property', fn=WeaponProperty.of_value)
    self.range = self._get_as_obj('range', Range)
    self.modifier = self._get_as_obj('modifier', Attribute)
    self.roll = self._get_as_obj('roll', Roll)

  def __repr__(self):
    return 'Name: {0.name}\nType: {0.type}\nValue: {0.value} gold\nWeight: {0.weight} pounds\nAC: {0.armor_class}\n' \
           'Strength: {0.strength}\nStealth: {0.stealth}\n1-handed damage: {0.dmg1}\n2-handed damage: '\
           '{0.dmg2}\nDamage Type: {0.dmgType}\nProperties: {0.properties}\nRange: {0.range}\nModifier: '\
           '{0.modifier}\nRoll: {0.roll}\nText: {0.text}'.format(self)
