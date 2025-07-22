from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age.value if hasattr(self.age, "value") else self.age,
            "gender": (
                self.gender.value if hasattr(self.gender, "value") else self.gender
            ),
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Question {self.question_text}>'

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "is_active": self.is_active,
            "sqe": self.sqe,
            "image": self.image.to_dict() if self.image else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
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
            "id": self.id,
            "content": self.content,
            "is_active": self.is_active,
            "sqe": self.sqe,
            "question_id": self.question_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
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
            "id": self.id,
            "url": self.url,
            "type": self.type.value if hasattr(self.type, "value") else self.type,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
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
            "id": self.id,
            "user_id": self.user_id,
            "choice_id": self.choice_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }