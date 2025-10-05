from gc import get_stats

from model.background import Background
from model.char_class import CharClass
from model.feat import Feat
from model.item import Item
from model.monster import Monster
from model.race import Race
from model.spell import Spell
from errors.no_such_entity_error import NoSuchEntityError
from utils.data_file_loader import DataFileLoader as DFL


class DataLoader (object):
  def __init__(self, data_name):
    self._bgs = {}
    self._cls = {}
    self._fts = {}
    self._itms = {}
    self._mnsts = {}
    self._rcs = {}
    self._spls = {}

    root = DFL().load_compendium_xml(data_name)
    for c in list(root):
      t = c.tag
      if t == 'background':
        bg = Background(c)
        self._bgs[bg.name] = bg
      elif t == 'class':
        cls = CharClass(c)
        self._cls[cls.name] = cls
      elif t == 'feat':
        ft = Feat(c)
        self._fts[ft.name] = ft
      elif t == 'item':
        itm = Item(c)
        self._itms[itm.name] = itm
      elif t == 'monster':
        mnst = Monster(c)
        self._mnsts[mnst.name] = mnst
      elif t == 'race':
        rc = Race(c)
        self._rcs[rc.name] = rc
      elif t == 'spell':
        spl = Spell(c)
        self._spls[spl.name] = spl
        
  def get_background(self, name):
    if name in self._bgs:
      return self._bgs[name]
    else:
      raise NoSuchEntityError(name, 'Background')
    
  def get_class(self, name):
    if name in self._cls:
      return self._cls[name]
    else:
      raise NoSuchEntityError(name, 'Class')
    
  def get_feat(self, name):
    if name in self._fts:
      return self._fts[name]
    else:
      raise NoSuchEntityError(name, 'Feat')
    
  def get_item(self, name):
    if name in self._itms:
      return self._itms[name]
    else:
      raise NoSuchEntityError(name, 'Item')
    
  def get_monster(self, name):
    if name in self._mnsts:
      return self._mnsts[name]
    else:
      raise NoSuchEntityError(name, 'Monster')
    
  def get_race(self, name):
    if name in self._rcs:
      return self._rcs[name]
    else:
      raise NoSuchEntityError(name, 'Race')
    
  def get_spell(self, name):
    if name in self._spls:
      return self._spls[name]
    else:
      raise NoSuchEntityError(name, 'Spell')
  
  def backgrounds(self):
    return list(self._bgs.values())
    
  def classes(self):
    return list(self._cls.values())

  def feats(self):
    return list(self._fts.values())
    
  def items(self):
    return list(self._itms.values())
    
  def monsters(self):
    return list(self._mnsts.values())
    
  def races(self):
    return list(self._rcs.values())
    
  def spells(self):
    return list(self._spls.values())

  def get_stats(self):
    stats = f"""
    Backgrounds: {len(self._bgs)} item(s)
    Classes: {len(self._cls)} item(s)
    Feats: {len(self._fts)} item(s)
    Items: {len(self._itms)} item(s)
    Monsters: {len(self._mnsts)} item(s)
    Races: {len(self._rcs)} item(s)
    Spells: {len(self._spls)} item(s)
    """
    return stats

  def print_stats(self):
    print(get_stats())
