from lib.users import Users
from lib.UserRepository import UserRepository
def test_get_all_users(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    users = repository.all_users()
    
    assert users == [
        Users(1,'Umut','umutc901@gmail.com','123'),
        Users(2,'calzagly','calzagly@gmail.com','234')
    ]
    
def test_get_all_posts(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = UserRepository(db_connection)
    users = repository.all_users()
    