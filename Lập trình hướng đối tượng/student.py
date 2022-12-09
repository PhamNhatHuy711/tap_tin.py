class SinhVien:
  def __init__(self, fullname, yob, score):
    self.hoten = fullname
    self.namsinh = yob
    self.dtb = score
  def __str__(self):
    message = '[Họ và tên : ' + self.hoten + '; năm sinh: ' + str(self.namsinh) + '; Điểm trung bình : ' + str(self.dtb) + ']'
    return message
  def __gt__(self, obj):
    return(self.dtb > obj.dtb)
  def __ge__(self, obj):
    return(self.dtb >= obj.dtb)
  def __lt__(self, obj):
    return(self.dtb < obj.dtb)
  def __le__(self, obj):
    return(sefl.dtb <= obj.dtb)
  def __eq__(self, obj):
   return(self.dtb == obj.dtb)
def main():
  sv1 = SinhVien('Phạm Nhật Huy', 2004, 10)
  sv2 = SinhVien('Phan Bá Hùng', 2004, 11)
  print(sv1)
if __name__ == "__main__":
  main()