from storage import simpan_semua
from simpan_fungsi import jeda


def delete_film_admin(daftar_film): 
    if len(daftar_film) == 0: 
        print("Anda tidak memiliki daftar film apapun")
        jeda()
        return daftar_film
    
    print("====== Daftar film ======")
    for i, film in enumerate(daftar_film, start=1): 
        print(f"{i}. {film.get('judul')} (genre: {film.get('genre')})")
    while True:
        try: 
            hapus_film = int(input("Masukkan nomor film yang ingin anda hapus (0 untuk batal): "))
            if hapus_film == 0:
                print("Penghapusan dibatalkan.")
                break
            elif 1 <= hapus_film <= len(daftar_film):
                terhapus = daftar_film.pop(hapus_film - 1)
                simpan_semua()
                print(f"Film untuk '{terhapus['judul']}' berhasil dihapus!")
                break
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")
    jeda()
    return daftar_film

def delete_admin(daftar_review):
    if len(daftar_review) == 0: 
        print("Belum ada ulasan yang bisa dihapus")
        jeda()
        return daftar_review
    
    print("====== Daftar Ulasan ======")

    for i, film in enumerate(daftar_review, start=1): 
        print(f"{i}. {film.get('judul')} - oleh {film.get('username', 'Anonim')} (Rating: {film.get('rating')}/10)")

    while True:
        try: 
            hapus_ulasan = int(input("Masukkan nomor ulasan yang ingin anda hapus (0 untuk batal): "))
            if hapus_ulasan == 0:
                print("Penghapusan dibatalkan.")
                break
            elif 1 <= hapus_ulasan <= len(daftar_review): 
                terhapus = daftar_review.pop(hapus_ulasan - 1)
                simpan_semua()
                print(f"Ulasan untuk '{terhapus['judul']}' berhasil dihapus!")
                break
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")
    jeda()
    return daftar_review