from lib.posts import Posts
class PostRepository:
    def __init__(self, connection):
        self.connection = connection
        
    def all_posts(self):
        rows = self.connection.execute('SELECT * FROM posts')
        return [
            Posts(row['id'], row['post'], row['date_time'], row['user_id'])
            for row in rows
        ]
