from configparser import ConfigParser

config = ConfigParser()


def get_token() -> str:
    try:
        file = open("settings.ini", "x")
        file.close()
    except FileExistsError:
        pass

    config.read("settings.ini")
    try:
        token = config["SETTINGS"]["TOKEN"]
    except KeyError:
        token = input("Введите токен вашего бота: ")
        if not config.has_section("SETTINGS"):
            config.add_section("SETTINGS")
        config.set("SETTINGS", "TOKEN", token)
        with open("settings.ini", "w") as configfile:
            config.write(configfile)

    return token


def get_openai_token() -> str:
    try:
        file = open("settings.ini", "x")
        file.close()
    except FileExistsError:
        pass

    config.read("settings.ini")
    try:
        token = config["SETTINGS"]["OPENAI"]
    except KeyError:
        token = input("Введите ваш ключ от OpenAI API: ")
        if not config.has_section("SETTINGS"):
            config.add_section("SETTINGS")
        config.set("SETTINGS", "OPENAI", token)
        with open("settings.ini", "w") as configfile:
            config.write(configfile)

    return token
