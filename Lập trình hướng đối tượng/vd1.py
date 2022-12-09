from student import SinhVien
def main():
    sv = [SinhVien('Phạm Nhật Huy', 2004, 10),
          SinhVien('Phan Bá Hùng', 2004, 12),
          SinhVien('Trần Hữu Bảo Anh', 2004, 1),
          SinhVien('Lê Nguyễn Vũ Duy', 2004, 7),
          SinhVien('Phan Nam Hà', 2004, 11),
          SinhVien('Phạm Văn Nhật Minh', 2004, 17)]
    sv = sorted(sv)
    for item in sv:
        print(item)
    sv = sorted(sv, reverse=True)
    for item in sv:
        print(item)
if __name__ == "__main__":
    main()