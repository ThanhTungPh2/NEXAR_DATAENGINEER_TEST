from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig, SourceFormat
from google.api_core.exceptions import NotFound
from datetime import datetime

# Hàm để kiểm tra nếu bảng tồn tại
def table_exists(client, dataset_id, table_id):
    try:
        client.get_table(f"{dataset_id}.{table_id}")
        return True
    except NotFound:
        return False

# Hàm tạo bảng với schema STRING nếu chưa tồn tại
def create_table_if_not_exists(client, dataset_id, table_id, schema):
    if not table_exists(client, dataset_id, table_id):
        table_ref = bigquery.Table(f"{dataset_id}.{table_id}", schema=schema)
        client.create_table(table_ref)
        print(f"Created table {table_id} in dataset {dataset_id}.")
    else:
        print(f"Table {table_id} already exists in dataset {dataset_id}.")

# Hàm import dữ liệu từ GCS vào BigQuery
def load_data_from_gcs(client, dataset_id, table_id, gcs_uri):
    # Cấu hình để BigQuery biết file CSV là file nén và sử dụng định dạng CSV
    job_config = LoadJobConfig(
        source_format=SourceFormat.CSV,  # Định dạng CSV
        skip_leading_rows=1,  # Bỏ qua dòng đầu tiên (header)
        autodetect=False,  # Tắt autodetect schema
        schema=[
            bigquery.SchemaField("albumId", "STRING"),
            bigquery.SchemaField("id", "STRING"),
            bigquery.SchemaField("title", "STRING"),
            bigquery.SchemaField("url", "STRING"),
            bigquery.SchemaField("thumbnailUrl", "STRING"),
            bigquery.SchemaField("created_date", "STRING"),
            bigquery.SchemaField("updated_date", "STRING")
        ],
        schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION],
    )
    
    table_ref = f"{dataset_id}.{table_id}"
    load_job = client.load_table_from_uri(gcs_uri, table_ref, job_config=job_config)
    
    # Chờ đợi quá trình load hoàn thành
    load_job.result()
    
    print(f"Loaded data from {gcs_uri} to table {table_ref}.")
    print(f"Table schema: {client.get_table(table_ref).schema}")

if __name__ == "__main__":
    # Khởi tạo client BigQuery
    bq_client = bigquery.Client()

    # Đặt tên dataset và bảng
    dataset_id = "prismatic-canto-378608.dataengineertest"  # Thay thế bằng dataset của bạn
    table_id = "photos"  # Tên bảng
    
    # Xác định schema với kiểu dữ liệu chính xác
    schema = [
        bigquery.SchemaField("albumId", "STRING"),
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("title", "STRING"),
        bigquery.SchemaField("url", "STRING"),
        bigquery.SchemaField("thumbnailUrl", "STRING"),
        bigquery.SchemaField("created_date", "STRING"),
        bigquery.SchemaField("updated_date", "STRING")
    ]

    # Tạo bảng nếu chưa tồn tại
    create_table_if_not_exists(bq_client, dataset_id, table_id, schema)

    # Đường dẫn GCS (thay thế với bucket và file của bạn)
    current_date = datetime.now().strftime("%Y/%m/%d")
    gcs_uri = f"gs://dateengineertest/{current_date}/photos.csv.gz"

    # Tải dữ liệu từ GCS vào BigQuery
    load_data_from_gcs(bq_client, dataset_id, table_id, gcs_uri)
