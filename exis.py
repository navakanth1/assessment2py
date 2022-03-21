dictionary={'name':'akash','age':20,'department':'BME'}
key= input("Enter key to check whether it is present or not:")
if key in dictionary.keys():
      print("Key is present and key value is:")
      print(dictionary[key])
else:
      print("Key is not present in dictionary")