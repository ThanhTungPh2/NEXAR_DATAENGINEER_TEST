import os
import requests
import concurrent.futures
import json
from datetime import datetime

# Hàm để gọi API và xử lý từng response
def fetch_photo(photo_id):
    url = f"https://jsonplaceholder.typicode.com/photos/{photo_id}"
    response = requests.get(url)
    
    # Kiểm tra response và trả về kết quả hoặc lỗi
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Sử dụng ThreadPoolExecutor để xử lý nhiều luồng
def download_photos_multithread():
    photo_ids = range(1, 101)  # Tải 100 ảnh đầu tiên
    photos = []
    
    # Sử dụng 5 luồng
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Gọi API cho mỗi photo_id trong danh sách
        future_to_photo = {executor.submit(fetch_photo, photo_id): photo_id for photo_id in photo_ids}
        
        # Xử lý kết quả trả về từ các luồng
        for future in concurrent.futures.as_completed(future_to_photo):
            photo_id = future_to_photo[future]
            try:
                photo_data = future.result()
                if photo_data:
                    photos.append(photo_data)  # Thêm ảnh vào danh sách nếu tải thành công
                    print(f"Downloaded photo ID {photo_id}")
            except Exception as exc:
                print(f"Photo ID {photo_id} generated an exception: {exc}")
    
    return photos

# Lưu ảnh vào file ndjson
def save_to_ndjson(photos, filename):
    # Tạo thư mục nếu nó chưa tồn tại
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
        for photo in photos:
            f.write(json.dumps(photo) + '\n')  # Ghi từng object JSON trên một dòng

# Gọi hàm để bắt đầu tải về
if __name__ == "__main__":

    all_photos = download_photos_multithread()
    print(f"Downloaded {len(all_photos)} photos.")
    
    # Tạo đường dẫn theo ngày hiện tại
    current_date = datetime.now().strftime('%Y/%m/%d')
    filename = f'../files/{current_date}/photos.ndjson'
    
    # Lưu kết quả vào file JSON NDJSON với định dạng ngày
    save_to_ndjson(all_photos, filename)
    print(f"Saved {len(all_photos)} photos to {filename}")
