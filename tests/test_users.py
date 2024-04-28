from lib.users import Users
def test_user():
   user =  Users("my id","my username","my email",'my password')
   assert user.id == "my id"
   assert user.username == "my username"
   assert user.email == "my email"
   assert user.password == "my password"
