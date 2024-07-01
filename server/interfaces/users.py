from cli_parser.users import get_users


class Users:
    def __init__(self) -> None:
        pass

    def total_count(self) -> int:
        matches = get_users()
        print(matches)

        return len(matches)

    def all_users(self):
        pass

    def create_user(self, username, password):
        pass

    def update_password(self, username, password):
        pass

    def delete_user(self, username):
        pass