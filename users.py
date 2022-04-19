from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['fname']
        self.last_name = data['lname']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (fname,lname,email) VALUES (%(fname)s,%(lname)s,%(email)s);"

        # comes back as the new row id
        result = connectToMySQL('users_schema').query_db(query,data)
        return result