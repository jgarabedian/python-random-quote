import random

def main():
  # print("Keep it logically awesome...")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1;
  rnd = random.randint(0,last)
  rnd2 = random.randint(0,last)
  while rnd == rnd2:
    rnd2 = random.randint(0,last)
  print(quotes[rnd] + '\n' + quotes[rnd2], end="")

if __name__== "__main__":
  main()
