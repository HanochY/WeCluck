from entities.topic import Comment    
def create(self):
        database.session.add(self)
        database.session.commit()

def read_topics(**kwargs):
    query = database.session.query(Topic)
    if kwargs:
        return query.filter_by(**kwargs).all()
    else:
        return query.all()

def read_topic(**kwargs):
    topics = read_topics(**kwargs)
    return topics[0] if topics else None