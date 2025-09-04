import context

from model.data_loader import DataLoader


def main():
  import os
  dl = DataLoader("CoreOnly")
  for m in dl.monsters:
    print(m.name)

if __name__ == '__main__':
  main()
  
