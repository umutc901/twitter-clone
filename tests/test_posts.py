from lib.posts import Posts
def test_post():
   post =  Posts("post id", "my post","date","user id",)
   assert post.id == "post id"
   assert post.content == "my post"
   assert post.date_time == "date"
   assert post.user_id == "user id"
