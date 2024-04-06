import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('Asm2_Data.csv')


# Xác định và loại bỏ dữ liệu nhiễu
# Ở đây, chúng ta sẽ kiểm tra xem có dòng nào bị trùng lặp không.
duplicate_rows = df[df.duplicated()]
if not duplicate_rows.empty:
    print("Có dữ liệu nhiễu - dòng bị trùng lặp. Loại bỏ các dòng trùng lặp...")
    df = df.drop_duplicates()
else:
    print("Không có dữ liệu nhiễu - không có dòng bị trùng lặp.")


# Xử lý dữ liệu thiếu sót
# Ở đây, chúng ta sẽ xác định số lượng dữ liệu thiếu sót trong mỗi cột và xử lý nếu cần.
missing_data = df.isnull().sum()
print("Dữ liệu thiếu sót trong mỗi cột:")
print(missing_data)
# Xử lý dữ liệu bị thiếu nếu cần
# Ví dụ: Thay thế các giá trị thiếu bằng giá trị trung bình của cột


# Chuyển đổi cột 'gender' về dạng chính xác
valid_genders = ['Male', 'Female', 'Other', 'Unknown']
df['gender'] = df['gender'].apply(lambda x: x if x in valid_genders else 'Unknown')
# Kiểm tra dữ liệu sau khi chuyển đổi
print(df['gender'].value_counts())
# Kiểm tra và sửa lỗi cú pháp của email
# Đây là một ví dụ đơn giản, bạn có thể sử dụng các biểu thức chính quy phức tạp hơn
df['email'] = df['email'].str.replace(r'[^@]+@[^@]+\.[^@]+', 'invalid_email')
print(df['email'].value_counts())

# Loại bỏ đặc điểm không cần thiết
# Trong trường hợp này, chúng ta sẽ loại bỏ cột "id" vì nó không cần thiết.
df = df.drop(columns=['id'])

# Lưu trữ dữ liệu đã xử lý vào file CSV mới
df.to_csv('Asm2_Cleaned_Data.csv', index=False)

print("Xử lý dữ liệu hoàn thành. Dữ liệu đã được lưu vào file Asm2_Cleaned_Data.csv.")
