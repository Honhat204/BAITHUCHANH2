import requests

# Thông tin cần thiết
access_token = 'EAAORImG8n5sBO3ZAXIN5WWgWwLdhXXp8g6NIcpgAdO2WsI6UCkdLSEO8ZAa4uF0qlmMTIotbZBueoHKz3UravGt789d3ZCn2CQEgERstcOQMoxPd4g3PciG11KKgTrVMiE1nIKNWZBHu35ZC16vRZAXhYckxRk83LbEfOS9JxICizRWoYw3ZAihTujnSMJnnw6WkFs6iK1wGhpRbe8mIx100LnOg'  # Thay bằng access token của bạn
page_id = '110362413747035'            # Thay bằng ID của trang bạn quản lý
message = 'Đây là bài viết tự động từ Python của HO NHAT'  # Nội dung bài đăng

# URL API của Facebook để đăng bài
url = f'https://graph.facebook.com/{page_id}/feed'

# Dữ liệu gửi đi
payload = {
    'message': message,
    'access_token': access_token
}

# Gửi yêu cầu POST đến Facebook Graph API
response = requests.post(url, data=payload)

# Xử lý kết quả
if response.status_code == 200:
    print("✅ Đăng bài thành công!")
    print("ID bài viết:", response.json().get('id'))
else:
    print("❌ Lỗi khi đăng bài:")
    print(response.status_code)
    print(response.text)