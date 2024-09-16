## Hướng dẫn cài đặt
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
