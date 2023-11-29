import pandas as pd

# URL của trang web
url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"

# Đọc dữ liệu từ trang web và lưu vào DataFrame của pandas
df = pd.read_csv(url)

# In danh sách các cột
print(df.columns)
