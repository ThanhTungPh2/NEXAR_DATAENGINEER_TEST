import pandas as pd
import json
import gzip
from datetime import datetime

current_date = datetime.now().strftime('%Y/%m/%d')

# Hàm chuyển đổi file ndjson sang CSV
def convert_ndjson_to_csv(ndjson_file, csv_file):
    with open(ndjson_file, 'r') as f:
        data = [json.loads(line) for line in f.readlines()]
    
    # Chuyển đổi dữ liệu thành DataFrame
    df = pd.DataFrame(data)
    
    # Thêm các cột mới với giá trị cụ thể
    df['created_date'] = current_date
    df['updated_date'] = current_date
    
    df.to_csv(csv_file, index=False)

# Hàm nén file CSV với gzip
def compress_csv_to_gzip(csv_file, gzip_file):
    with open(csv_file, 'rb') as f_in:
        with gzip.open(gzip_file, 'wb') as f_out:
            f_out.writelines(f_in)

# Thực thi chuyển đổi và nén
if __name__ == "__main__":
    ndjson_file = f'../files/{current_date}/photos.ndjson'
    csv_file = f'../files/{current_date}/photos.csv'
    convert_ndjson_to_csv(ndjson_file, csv_file)
    print(f"Converted {ndjson_file} to {csv_file}")

    # Nén file CSV với gzip
    gzip_file = f'../files/{current_date}/photos.csv.gz'
    compress_csv_to_gzip(csv_file, gzip_file)
    print(f"Compressed {csv_file} to {gzip_file}")
