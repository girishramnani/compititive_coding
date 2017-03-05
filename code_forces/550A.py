word = input()
print("YES" if abs(word.find("AB")-word.find("BA"))>=2  else "NO")
