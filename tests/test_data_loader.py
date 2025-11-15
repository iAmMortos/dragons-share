import context

from model.data_loader import DataLoader


def main():
  import os
  dl = DataLoader("Complete")
  dl.print_stats()
  
  speeds = []
  for m in dl.monsters():
    speed = str(m.speed)
    if speed not in speeds:
      speeds += [speed]
  for s in sorted(speeds):
    
    print(s)
if __name__ == '__main__':
  main()
  
