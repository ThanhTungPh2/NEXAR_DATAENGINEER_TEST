from google.cloud import storage
import os
from datetime import datetime

# Hàm đẩy file lên Google Cloud Storage
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # Khởi tạo client GCS
    storage_client = storage.Client()
    
    # Truy cập bucket
    bucket = storage_client.bucket(bucket_name)
    
    # Tạo blob (đối tượng lưu trữ)
    blob = bucket.blob(destination_blob_name)
    
    # Tải file lên
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

if __name__ == "__main__":
    # Lấy ngày hiện tại để tạo đường dẫn
    current_date = datetime.now().strftime("%Y/%m/%d")
    
    # Đường dẫn file local
    local_file_path = f'./files/{current_date}/photos.csv.gz'
    
    # Tên bucket trong Google Cloud Storage
    bucket_name = 'dateengineertest'  # Thay bằng tên bucket của bạn
    
    # Đường dẫn file trên GCS (blob name)
    destination_blob_name = f'{current_date}/photos.csv.gz'
    
    # Gọi hàm upload
    upload_to_gcs(bucket_name, local_file_path, destination_blob_name)
