def suma(a, b):
    """
    suma dos numeros
    :param a:
    :param b:
    :return:
    """
    return a+b


def login(username: str) -> str:
    if username == "admin":
        return "Login Successful"

    return "Login Failed"


def resta(a: int, b: int) -> int:
    return a - b


if __name__ == '__main__':
    print(suma(2, 3))
    print(login("admin"))
