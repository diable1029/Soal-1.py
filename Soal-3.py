nilai_teori=int(input("nilai ujian="))
nilai_praktikum=int(input("nilai praktikum="))
if nilai_teori>=70 and nilai_praktikum>=70 :
    print("Selamat, anda lulus!")
elif nilai_teori>=70 and nilai_praktikum<70 :
    print("Anda harus mengulang ujian praktek")
elif nilai_teori<70 and nilai_praktikum>=70 :
    print("Anda harus mengulang ujian teori.")
else :
    print("Anda harus mengulang ujian teori dan praktek.")
