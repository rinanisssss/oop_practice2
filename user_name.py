class User:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}はルール違反です")  # pythonにおいて強制的に起こすのがraise

        self.name = name

    def screen_name(self):
        return self.name.upper()

    def self_introduction(self):
        print(f"私の名前は{self.name.upper()}です。よろしくお願いします！")


# UserNameクラスのインスタンス化
tanaka = User(name="tanaka")


print(tanaka.screen_name())
print(tanaka.self_introduction())
