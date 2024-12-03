def inject_fields(parent):
    def generate(cls):
        cls.__annotations__ = parent.__annotations__ | cls.__annotations__
        return cls
    return generate