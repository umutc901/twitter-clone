from lib.users import Users

class UserRepository:
    def __init__(self,connection):
        self.connection = connection
        
    def all_users(self):
        rows = self.connection.execute('SELECT * FROM users')
        return [
            Users(row['id'], row['username'], row['email'],row['pass'])
            for row in rows
        ]
        