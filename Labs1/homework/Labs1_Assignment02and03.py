from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. Connect to database
client = MongoClient(uri)

#2. Get database
db = client.get_default_database()

#3. Get collection
posts = db['posts']

#4. Add blog
blog_post = {
    "title": "Những cái nhất của C4E19",
    "author": "Nhung nhúc",
    "content": "Những cái nhất của C4E19 \n - Lớp nhiều con gái nhất \n - Giảng viên có cố gắng nhất (really, TA, đã bảo đừng có cố kể chuyện cười rồi mà cứ để mọi người phải cố cười trừ là sao? =.=) \n - Có nhiều học viên bốc phét nhất (Cụ thể chính là người đang viết cái bài blog posts này đây :|) \n - Còn gì nữa nhở có đi học mấy khóa trước đâu mà biết. Bị đúp 3 khóa rồi :|"
}

posts.insert_one(blog_post)
