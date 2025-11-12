import context

from model.data_loader import DataLoader


def main():
  import os
  dl = DataLoader("Complete")
  dl.print_stats()
  
  types = []
  for m in dl.monsters():
    speed = str(m.speed)
    if 'walk 400' in speed:
      print(m.name)
      print(m.description)
if __name__ == '__main__':
  main()
  
