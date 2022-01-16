print("program pembagian dua buah angka\n")

while True:
  try:
    a = int(input("masukkan angka pertama : "))
    b = int(input("masukkan angka kedua : "))
    result = a / b
    break
  except Exception as err:
    result = str(err)
    break

isError = isinstance(result, str)  # check if result is string -> True if string, False if not string
if isError :
  print("error : ", result)
else:
  print("result : ", result)