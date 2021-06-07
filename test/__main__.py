from . import other

flag = True

def print_flag():
  print(f"My name is '{__name__}' and I see {flag}")

def main():
  print_flag()
  other.set_flat()
  print_flag()

if __name__ == "__main__":
  main()