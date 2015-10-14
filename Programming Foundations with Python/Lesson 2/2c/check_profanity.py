def read_text(file_location):
  file_data = open(file_location, "r" )
  print(file_data.read())
  file_data.close()
read_text("README.rd")
