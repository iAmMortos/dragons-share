import context

from model.data_loader import DataLoader


def main():
  import os
  dl = DataLoader("Complete")
  dl.print_stats()

if __name__ == '__main__':
  main()
  
