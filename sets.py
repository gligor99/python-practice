# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(3) #Not added
print(s)

# Remove elements from set
s.remove(2)
print(s)

# Get length of set
print(f"The set has:  {len(s)} elements.") 