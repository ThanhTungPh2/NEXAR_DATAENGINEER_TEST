## Hướng dẫn cài đặt

**Ở đây em không thể cung cấp file cấu hình IAM của Google Cloud được vì đây là tài khoản cá nhân**. Nếu bên công ty có test thì có thể đặt file config theo như hình ảnh hoặc như video em cung cấp.

![image](https://github.com/user-attachments/assets/f3a1707b-2378-40ce-bb37-8c18286d36e5)

Đối với chạy chương trình trên môi trường Linux thì trước câu lệnh có từ khóa `sudo` hoặc dùng `sudo -i` để chuyển sang user root
1. Khởi chạy docker-compose
- Trên môi trường Windows: `docker-compose up`
- Trên môi trường Linux: `sudo docker compose up`
2. Truy cập vào container 
- Dùng lệnh `sudo docker ps` tìm id của container airflow-worker
- Dùng lệnh `sudo docker exec -it -u root container_id_airflow_worker bash`
3. Thiết lập time-zone múi giờ thứ 7 `ln -sf /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime`
4. Truy cập thư mục `cd /opt/airflow/Python`
5. Thiết lập môi trường ảo `python -m venv my_project`
6. Truy cập vào môi trường ảo `. my_project/bin/activate`
7. Cài đặt thư viện python `pip install -r requirements.txt`
8. Truy cập vào UI airflow browser `http://localhost:8080/home`

## Video hướng dẫn cài đặt và demo
[Xây dựng stack:Apache Airflow, Google Cloud Storage(GCS), BigQuery.](https://youtu.be/hl4FGbp7rMg)

## Luồng dữ liệu ngày 17/09/2024 sau ngày quay video 16/07/2024
1. API được Call về và tạo thành thư mục ngày 17

 ![image](https://github.com/user-attachments/assets/b7b27fc3-7cdd-4c3f-9d45-965435c4c49a)

2. File được đẩy lên GCS
![image](https://github.com/user-attachments/assets/271fc0b6-5ef8-49d7-8e99-3de4c218d5fb)

3. Trong bảng ở Bigquery có dữ liệu ngày 17/9/2024
![image](https://github.com/user-attachments/assets/ccd17dff-d352-4e7e-92fc-18244b92bdb7)


