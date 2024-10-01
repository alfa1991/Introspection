def introspection_info(obj):
    """
    Функция для подробной интроспекции объекта.

    Args:
        obj: Любой объект Python.

    Returns:
        Словарь с информацией об объекте: тип, атрибуты, методы, модуль и др.
    """

    info = {}
    info['type'] = type(obj)
    info['attributes'] = dir(obj)
    info['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]

    # Проверяем, является ли объект экземпляром класса
    if isinstance(obj, object):
        info['class'] = obj.__class__
        # Проверяем, есть ли у объекта модуль
        if hasattr(obj.__class__, '__module__'):
            info['module'] = obj.__class__.__module__

    return info

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

obj = MyClass("Alice")
info = introspection_info(obj)
print(info)