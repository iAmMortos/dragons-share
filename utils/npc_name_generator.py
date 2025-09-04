
import random
from utils.data_file_loader import DataFileLoader as DFL


class NPCNameGenerator(object):
  def __init__(self):
    data = DFL().load_csv('npc_names')
    self._first_names = []
    self._epithets = []
    self._nouns = []
    for datum in data:
      a,b,c,d,e = datum
      self._first_names += [a]
      self._epithets += [b, d]
      self._nouns += [c, e]

  def generate_random_name(self):
    first = random.choice(self._first_names)
    epithet = random.choice(self._epithets)
    noun = random.choice(self._nouns)

    return f'{first} {epithet}{noun}'

  def generate_paired_name(self):
    first = random.choice(self._first_names)
    i = random.randint(0, len(self._nouns) - 1)
    last = f'{self._epithets[i]}{self._nouns[i]}'
    return f'{first} {last}'
    
  def get_alliteration_name(self):
    l = 'z'
    while l == 'z':  # There's no last names that start with Z
      first = random.choice(self._first_names)
      l = first[0].lower()
    es = []
    for e in self._epithets:
      if e[0].lower() == l:
        es += [e]
    epithet = random.choice(es)
    noun = random.choice(self._nouns)
    return f'{first} {epithet}{noun}'

  def get_last_name_starting_with(self, start):
    eps = []
    start = start.lower()
    for e in self._epithets:
      if e.lower().startswith(start):
        eps += [e]
    return f'{random.choice(eps)}{random.choice(self._nouns)}'


if __name__ == '__main__':
  import os
  import sys
  sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
  os.chdir('..')

  gen = NPCNameGenerator()
  print("Randomized Last Names:")
  for _ in range(10):
    print('  ', gen.generate_random_name())

  print("\nPre-Paired Last Names:")
  for _ in range(10):
    print('  ', gen.generate_paired_name())
    
  print('\nAlliterated Names:')
  for _ in range(10):
    print('  ', gen.get_alliteration_name())

  print('\nR Last Names:')
  for _ in range(10):
    print('  ', gen.get_last_name_starting_with('R'))
