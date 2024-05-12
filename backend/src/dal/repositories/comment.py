from entities.comment import Comment
    
    def create(self):
        database.session.add(self)
        database.session.commit()
    

def read_comments(**kwargs):
    query = database.session.query(Comment)
    if kwargs:
        return query.filter_by(**kwargs).all()
    else:
        return query.all()

def read_comment(**kwargs):
    comments = read_comments(**kwargs)
    return comments[0] if comments else None