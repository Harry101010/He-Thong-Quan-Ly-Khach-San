from services import QuanLyKhachSan

def nhap_so(thong_bao, kieu=float):
  while True:
    try:
      giatri = kieu(input(thong_bao).strip())
      return giatri
    except ValueError:
      print(f"Dữ liệu không hợp lệ, xin nhập lại: ")
          
def nhap_chuoi(thong_bao):
  return input(thong_bao).strip()

def them_phong(qlks):
    print("==========THÊM PHÒNG MỚI==========")
    
    ma_phong = nhap_chuoi("Nhập Mã Phòng: ")
    ten_phong = nhap_chuoi("Nhập Tên Phòng: ")
    gia_co_ban = nhap_so("Nhập Giá Cơ Bản/Ngày: ", float)
    
    print("1. Phòng Thường")
    print("2. Phòng VIP")

    loai = nhap_chuoi("Chọn Loại Phòng: ")
    
    phi_don_dep = 0
    phi_minibar = 0
    
    if loai == "2":
        phi_don_dep = nhap_so("Nhập Phí Dọn Dẹp: ", float)
        phi_minibar = nhap_so("Nhập Phí Minibar: ", float)
        
    phong = qlks.them_phong(
        ma_phong,
        ten_phong,
        gia_co_ban,
        loai,
        phi_don_dep,
        phi_minibar
    )

    print(f"Đã thêm phòng {phong.ma_phong} thành công!")
    
def dat_phong(qlks):
    print("==========ĐẶT PHÒNG==========")
    
    ma_phong = nhap_chuoi("Nhập Mã Phòng Cần Đặt:")
    ma_khach = nhap_chuoi("Nhập Mã Khách: ")
    ten_khach = nhap_chuoi("Nhập Tên khách: ")
    cccd = nhap_chuoi("Nhập Số CCCD/CMND: ")
    so_ngay = nhap_so("Nhập Số Ngày Thuê: ", int)

    phieu = qlks.dat_phong(
      ma_phong,
      ma_khach,
      ten_khach,
      cccd,
      so_ngay
    )
    
    print(
      f"Đặt Phòng Thành Công: {phieu.phong.ma_phong} | "
      f"Khách: {phieu.khach_hang.ten} | "
      f"Số Ngày: {phieu.so_ngay}"
    )

def tra_phong(qlks):
    print(" ------- Trả phòng & Thanh toán ------- ")

    ma_phong = nhap_chuoi("Nhập mã phòng cần trả: ")

    phieu, tong_tien = qlks.tra_phong(ma_phong)

    print("\nThanh toán thành công!")
    print(f"Mã phòng: {phieu.phong.ma_phong}")
    print(f"Tên khách: {phieu.khach_hang.ten}")
    print(f"Loại phòng: {phieu.phong.__class__.__name__}")
    print(f"Số ngày thuê: {phieu.so_ngay}")
    print(f"Giá cơ bản/ngày: {phieu.phong.gia_co_ban:,.0f} VNĐ")

    if phieu.phong.__class__.__name__ == "PhongVIP":
        print(
            f"Phí Dọn Dẹp: "
            f"{phieu.phong.phi_don_dep:,.0f} VNĐ"
        )
        print(
            f"Phí Minibar: "
            f"{phieu.phong.phi_minibar:,.0f} VNĐ"
        )

    print(f"Tổng Thanh Toán: {tong_tien:,.0f} VNĐ")

def menu():
    print("==========HỆ THỐNG QUẢN LÝ KHÁCH SẠN==========")
    print("1. Hiển Thị Danh Sách Phòng")
    print("2. Thêm Phòng Mới")
    print("3. Đặt Phòng")
    print("4. Trả Phòng & Thanh Toán")
    print("5. Xem Báo Cáo Doanh Thu")
    print("0. Thoát & Lưu Dữ Liệu")
    print("==============================================")
    
def main():   
  qlks = QuanLyKhachSan()
  
  try: 
    qlks.tai_du_lieu()
  except (OSError, ValueError) as e:
    print(f"Không thể tải dữ liệu: {e}")
    return
  
  print(f"Số Phòng Hiện Tại Có: {len(qlks.danh_sach_phong)}")
  while True:
    menu()
    lua_chon = nhap_chuoi("Nhập Lựa Chọn: ")

    try:
      if lua_chon == "1":
        qlks.hien_thi_phong()
      elif lua_chon == "2":
        them_phong(qlks)
        qlks.luu_du_lieu()
      elif lua_chon == "3":
        dat_phong(qlks)
        qlks.luu_du_lieu()
      elif lua_chon == "4":
        tra_phong(qlks)
        qlks.luu_du_lieu()
      elif lua_chon == "5":
        qlks.bao_cao_doanh_thu()
      elif lua_chon == "0":
        qlks.luu_du_lieu()
        break
      else:
          print("Lựa Chọn Không Hợp Lệ.")
    except (ValueError, OSError) as e:
        print(f"Không thể thực hiện thao tác: {e}")
    except Exception as e:
        print(f"Đã xảy ra lỗi ngoài dự kiến: {e}")

    print("\n")

if __name__ == "__main__":
  main()