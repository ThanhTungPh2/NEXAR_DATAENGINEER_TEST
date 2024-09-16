### Câu 1
1. **Kimball (Dimensional Modeling)** là mô hình dữ liệu **dimensional**. Kimball dữ liệu thành các **fact tables** và **dimension tables**. Các mô hinh phổ biến là star schema, snowflake schema, galaxy schema.
	-   **Fact tables**: Chứa các dữ liệu định lượng, thường là dữ liệu giao dịch hoặc sự kiện.
	-   **Dimension tables**: Chứa dữ liệu mô tả, như thời gian, địa điểm, sản phẩm, khách hàng.
-   Dùng cho **hệ thống báo cáo và phân tích BI** với các yêu cầu phân tích tổng hợp, như doanh thu theo khu vực, sản phẩm, thời gian.
-   Phù hợp với các **hệ thống phân tích dữ liệu lớn (OLAP)**.
2. **One Big Table** là lưu trữ tất cả dữ liệu trong một bảng lớn duy nhất. Thay vì phân chia thành các bảng fact và dimension như Kimball, mỗi dòng chứa tất cả thông tin cần thiết cho một thực thể hoặc giao dịch.
-   Dùng cho các **hệ thống phân tích đơn giản** với quy mô dữ liệu vừa phải, yêu cầu truy vấn nhanh chóng mà không cần thiết kế phức tạp.
-   Phù hợp cho các **chiến dịch ngắn hạn** hoặc khi cần thử nghiệm nhanh với dữ liệu thô.
3. **Relational Modeling** thường xây dựng dựa trên nguyên tắc của **Third Normal Form (3NF)**. Mục tiêu chính là **loại bỏ sự dư thừa dữ liệu** bằng cách tách dữ liệu thành nhiều bảng nhỏ với các mối quan hệ được xác định thông qua khóa ngoại (foreign key).
- Dùng cho **hệ thống giao dịch (OLTP)**, khi cần đảm bảo tính toàn vẹn của dữ liệu và tránh dư thừa
- Phù hợp với **hệ thống dữ liệu động**, thường xuyên thay đổi hoặc cập nhật.
### Câu 2
Các loại dữ liệu khác như **STRING** hoặc **FLOAT** không được hỗ trợ partition vì việc chia dữ liệu theo các loại này khó tối ưu và phân mảnh dữ liệu có thể dẫn đến việc tạo ra quá nhiều partition nhỏ (phân mảnh quá mức), gây ảnh hưởng tiêu cực đến hiệu suất. Các loại dữ liệu như INTEGER và time-unit cho phép chia dữ liệu theo cách đơn giản, có thứ tự.
### Câu 3
-   **Sắp xếp dữ liệu theo cột `STRING`**: Khi một bảng được tạo với clustering dựa trên cột dạng `STRING`, BigQuery sẽ sắp xếp dữ liệu dựa trên các giá trị của cột này. Các giá trị `STRING` sẽ được lưu trữ và tổ chức trong các **block dữ liệu** theo thứ tự chữ cái (lexicographical order).
    
-   **Phân đoạn dữ liệu (Data Blocks)**: Dữ liệu của bảng được chia thành các phân đoạn (blocks). Mỗi block chứa một nhóm dữ liệu liên tiếp được sắp xếp theo cột `STRING` được chọn làm cluster key. Khi truy vấn dựa trên cột `STRING`, BigQuery chỉ cần quét các block liên quan đến phạm vi giá trị `STRING` trong câu truy vấn, thay vì quét toàn bộ bảng.
    
-   **Tối ưu hóa truy vấn (Query Optimization)**: Khi bạn truy vấn dữ liệu dựa trên cột được cluster, BigQuery có thể giảm đáng kể số lượng dữ liệu cần quét. Ví dụ, nếu bạn có một bảng chứa hàng tỷ dòng dữ liệu và bạn truy vấn bằng cách lọc trên giá trị cột `STRING`, BigQuery sẽ tìm và quét những block chứa các giá trị `STRING` phù hợp, bỏ qua các block không liên quan.
    
-   **Độ trễ khi insert dữ liệu**: Khi bạn thêm dữ liệu vào bảng được cluster, hệ thống BigQuery sẽ phải sắp xếp lại dữ liệu theo cột `STRING`. Điều này có thể tạo ra một chút độ trễ trong quá trình insert, nhưng mang lại hiệu suất truy vấn tốt hơn trong tương lai.
    
-   **Sự khác biệt so với partitioning**: Clustering không phải là partitioning. Trong partitioning, dữ liệu được chia theo các phần cứng nhắc như theo ngày hoặc số nguyên. Nhưng với clustering, dữ liệu được tổ chức theo một cột cụ thể (có thể là dạng `STRING`), và khi truy vấn lọc theo cột đó, BigQuery chỉ quét các phân đoạn có dữ liệu liên quan, làm cho truy vấn nhanh hơn.
### Câu 4
Count Distinct:  Trả về số lượng giá trị duy nhất trong một cột được chỉ định. Nó quét toàn bộ tập dữ liệu để xác định các giá trị riêng biệt, giúp dữ liệu chính xác nhưng có thể chậm, đặc biệt đối với các tập dữ liệu lớn
Approx_count_distinct: sử dụng các thuật toán xác suất như HyperLogLog (HLL) để ước tính số lượng giá trị duy nhất một cách nhanh chóng và giảm chi phí tính toán. Mặc dù nó có thể gây ra một số lỗi nhưng nó cải thiện đáng kể hiệu suất truy vấn, đặc biệt là khi xử lý các tập dữ liệu lớn.