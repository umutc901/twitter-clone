class Posts():
    def __init__(self,id, content,date_time,user_id):
        self.id = id
        self.content = content
        self.date_time = date_time
        self.user_id = user_id
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.content}, {self.date_time}, {self.user_id})"