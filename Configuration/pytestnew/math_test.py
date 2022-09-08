
Path=open("/Configuration/pytestnew/new", "rt")
data=Path.read()
count = data.split()
print("total count ",len(count))