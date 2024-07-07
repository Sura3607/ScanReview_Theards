from app_store_scraper import AppStore
from google_play_scraper import app, Sort, reviews_all
import pandas as pd
import numpy as np
import json, os, uuid

#truy vấn google play
g_reviews = reviews_all(
        "com.instagram.barcelona",
        sleep_milliseconds=0, # defaults to 0
        lang='vi', # defaults to 'en'
        country='vn', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    )

#truy vấn appstore
a_reviews = AppStore('vn', 'threads-an-instagram-app', '6446901002')
a_reviews.review()


#googleplay
g_df = pd.DataFrame(np.array(g_reviews),columns=['review'])
g_df2 = g_df.join(pd.DataFrame(g_df.pop('review').tolist()))

g_df2.drop(columns={'userImage', 'reviewCreatedVersion'},inplace = True)
g_df2.rename(columns= {'score': 'rating','userName': 'user_name', 'reviewId': 'review_id', 'content': 'review_description', 'at': 'review_date', 'replyContent': 'developer_response', 'repliedAt': 'developer_response_date', 'thumbsUpCount': 'thumbs_up'},inplace = True)
g_df2.insert(loc=0, column='source', value='Google Play')
g_df2.insert(loc=3, column='review_title', value=None)
g_df2['laguage_code'] = 'vi'
g_df2['country_code'] = 'vn'

#add to excel
g_df2.to_excel(r'D:\ScanReview_Theards\UnfilteredData\GooglePlayReviews.xlsx', index=False)
print('Dữ liệu đã được lưu vào tệp Excel thành công.')

#appstore
a_df = pd.DataFrame(np.array(a_reviews.reviews),columns=['review'])
a_df2 = a_df.join(pd.DataFrame(a_df.pop('review').tolist()))

a_df2.drop(columns={'isEdited'},inplace = True)
a_df2.insert(loc=0, column='source', value='App Store')
a_df2['developer_response_date'] = None
a_df2['thumbs_up'] = None
a_df2['laguage_code'] = 'vi'
a_df2['country_code'] = 'vn'
a_df2.insert(loc=1, column='review_id', value=[uuid.uuid4() for _ in range(len(a_df2.index))])
a_df2.rename(columns= {'review': 'review_description','userName': 'user_name', 'date': 'review_date','title': 'review_title', 'developerResponse': 'developer_response'},inplace = True)
a_df2 = a_df2.where(pd.notnull(a_df2), None)

#add to excel
a_df2.to_excel(r'D:\ScanReview_Theards\UnfilteredData\AppStoreReviews.xlsx', index=False)
print('Dữ liệu đã được lưu vào tệp Excel thành công.')

#hehehe