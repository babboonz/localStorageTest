# get the local storage
storage = LocalStorage(driver)

# set an item
storage["mykey"] = 1234
storage.set("mykey2", 5678)

# get an item
print(storage["mykey"])      # raises a KeyError if the key is missing
print(storage.get("mykey"))  # returns None if the key is missing

# delete an item
storage.remove("mykey")

# iterate items
for key, value in storage.items():
  print("%s: %s" % (key, value))

# delete items
storage.clear()
