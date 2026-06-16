import numpy as np

marks = np.array([[54, 68, 96], [87, 42, 36], [75, 55, 99]])

print(np.mean(marks))             # Overall mean

print(np.mean(marks, axis=1))     # Mean per Student {Row}

print(np.mean(marks, axis=0))     # Mean per Student {Column}

print(np.max(marks))              # Highest marks

print(np.std(marks))              # Standard deviation