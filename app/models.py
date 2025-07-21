from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Question {self.question_text}>'

    def to_dict(self):
        return {
            'id': self.id,
            'question_text': self.question_text
        }

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_text = db.Column(db.String(255), nullable=False)

    question = db.relationship('Question', backref=db.backref('choices', lazy=True))

    def __repr__(self):
        return f'<Choice {self.choice_text}>'

    def to_dict(self):
        return {
            'id': self.id,
            'question_id': self.question_id,
            'choice_text': self.choice_text
        }

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

    question = db.relationship('Question', backref=db.backref('images', lazy=True))

    def __repr__(self):
        return f'<Image {self.image_url}>'

    def to_dict(self):
        return {
            'id': self.id,
            'question_id': self.question_id,
            'image_url': self.image_url
        }

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_id = db.Column(db.Integer, db.ForeignKey('choice.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('answers', lazy=True))
    question = db.relationship('Question', backref=db.backref('answers', lazy=True))
    choice = db.relationship('Choice', backref=db.backref('answers', lazy=True))

    def __repr__(self):
        return f'<Answer {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'question_id': self.question_id,
            'choice_id': self.choice_id
        }