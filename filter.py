import pandas as pd
import emoji
import re

# Đọc file Excel
a_df = pd.read_excel(r'D:\ScanReview_Theards\UnfilteredData\AppStoreReviews.xlsx') #appstore
g_df = pd.read_excel(r'D:\ScanReview_Theards\UnfilteredData\GooglePlayReviews.xlsx') #googlePlay

# Đọc file txt chứa các từ dừng
with open('vietnamese-stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set(file.read().splitlines())

# Hàm loại bỏ các Emoji
def remove_emojis(text):
    return emoji.replace_emoji(text, replace='')

# Hàm loại bỏ các Stopword
def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word.lower() not in stopwords])

# Áp dụng các hàm trên cho cột chứa các câu đánh giá
a_df['cleaned_reviews'] = a_df['review_title'].apply(lambda x: remove_stopwords(remove_emojis(x))) #appstore
g_df['cleaned_reviews'] = g_df['review_description'].apply(lambda x: remove_stopwords(remove_emojis(x))) #googlePlay

# Lưu kết quả vào file Excel mới
a_df.to_excel('D:\ScanReview_Theards\FilteredData\A_cleaned_reviews.xlsx', index=False) #appstore 
g_df.to_excel('D:\ScanReview_Theards\FilteredData\G_cleaned_reviews.xlsx', index= False) #googlePlay