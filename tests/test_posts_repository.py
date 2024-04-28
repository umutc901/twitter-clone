from lib.posts import Posts
from lib.PostsRepository import PostRepository
import datetime

def test_get_all_posts(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PostRepository(db_connection)
    posts = repository.all_posts()

    # Convert datetime.datetime objects to strings with the same format
    actual_values = [(post.content, post.date_time.strftime('%Y-%m-%d %H:%M:%S'), post.user_id) for post in posts]

    assert actual_values == [
        ('My first post', '2024-04-27 16:34:00', 1),
        ('My second post', '2024-04-27 16:50:00', 1),
        ('My first post', '2024-04-27 16:34:00', 2),
        ('My second post', '2024-04-27 16:50:00', 2)
    ]


