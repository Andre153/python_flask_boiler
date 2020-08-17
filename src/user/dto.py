from .. import marsh


class UserDTO:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
