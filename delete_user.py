from storage import simpan_semua
from simpan_fungsi import jeda
from read_user import read_user

def delete_user(user, daftar_review):
    ulasan_saya = read_user(user, daftar_review)
    if len(ulasan_saya) == 0: 
        jeda()
        return daftar_review

    while True:
        try: 
            nomor_hapus = int(input("Masukkan nomor yang ingin dihapus (0 untuk batal): "))
            if nomor_hapus == 0: 
                print("Penghapusan dibatalkan")
                jeda()
                return daftar_review
            
            if nomor_hapus < 1 or nomor_hapus > len(ulasan_saya): 
                print("Nomor tidak valid")
            else:
                break
        except ValueError: 
            print("Masukkan angka!")

    review_hapus = ulasan_saya[nomor_hapus - 1]
    daftar_review.remove(review_hapus)
    simpan_semua()
    print("Review berhasil dihapus!")
    jeda()
    return daftar_review