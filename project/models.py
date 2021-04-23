from project.app import db

class Post(db.Model):
    id = db.Column()
    title = db.Column()
    text = db.Coolumn()


    def __init__(self, title, title, text):
        self.title = title
        self.text = text


    def __repr__(self):
        return f'<title {self.title}>'
