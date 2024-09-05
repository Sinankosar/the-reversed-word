def FirstReverse(strParam):
  # Sinan Koşar
  cevap = []
  a =-1
  for i in range(len(strParam)): # girilen değer uzunluğu kadar işlem yaptırır.
    cevap.append(strParam[a]) #en son karakterden başlayarak cevap listesine ekler
    a-=1

  cevap = "".join(cevap) # virgülleri sildim
  strParam = cevap


  # code goes here
  return strParam

# keep this function call here
print(FirstReverse("Hello world i am33 sinan"))