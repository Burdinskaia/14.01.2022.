teksts = input("Ievadit tekstu: ")
def reverseWord(teksts):
  sar1 = teksts.split()
  if len(sar1)>1:
    sar.reverse()
    teksts=""
    for elements in sar1:
      teksts+=elements
    print(teksts)
  else:
    teksts = "Parāk iss teikums!"
    print(teksts)
  return teksts
reverseWord(teksts)