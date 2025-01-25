def show_color_palette():
  for i in range(256):
    print(f"\033[38;5;{i}m{str(i).rjust(3)}\033[0m", end=" ")
    if (i + 1) % 16 == 0:
      print()

if __name__ == '__main__':
  show_color_palette()