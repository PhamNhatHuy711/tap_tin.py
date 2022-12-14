from student import SinhVien
import pickle
import os
def luu_class(thumuc: str, ten_taptin: str, obj: SinhVien):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
         pickle.dump(obj, f)
        print('ket thuc chuong trinh luu du lieu')
    except Exception as e:
        print(e)

def doc_class(thumuc: str, ten_taptin: str) -> SinhVien:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        print(e)

def in_list_sinhvien(content: list[SinhVien]):
    for item in content:
        print(item)

def main():
    path = 'C:/Users/LEGION/PycharmProjects/Huy'
    filename = 'sinhvien.dat'
    sv = [SinhVien('Huy', 2004, 10),
          SinhVien('Huy', 2004, 10),
          SinhVien('Huy', 2004, 10)]
    luu_class(path, filename, sv)
    noidung = doc_class(path, filename)
    in_list_sinhvien(noidung)
    print('ket thuc chuong trinh')
if __name__ == '__main__':
    main()
