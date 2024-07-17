# if is sqlalchemy...
class BaseEntity():
    def __init__(self, **attributes):
        for name, value in attributes.items():
            if hasattr(self, name) and name != 'id':
                setattr(self, name, value)
                
    def update(self, **attributes):
        for name, value in attributes:
            if hasattr(self, name) and name != 'id':
                setattr(self, name, value)
        
    def to_dict(self):
        data = vars(self)
        data.pop('_sa_instance_state')
        return data