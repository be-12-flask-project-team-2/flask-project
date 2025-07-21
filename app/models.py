from datetime import datetime
import enum

from sqlalchemy import create_engine, Column, Integer, String, Enum, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# 데이터베이스 베이스 클래스 생성
Base = declarative_base()

# Enum 클래스들 정의
class AgeEnum(enum.Enum):
    TEEN = "teen"
    TWENTY = "twenty"
    THIRTY = "thirty"
    FORTY = "forty"
    FIFTY = "fifty"

class GenderEnum(enum.Enum):
    MALE = "male"
    FEMALE = "female"

class ImageTypeEnum(enum.Enum):
    MAIN = "main"
    SUB = "sub"

# 모델 클래스들 정의
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    age = Column(Enum(AgeEnum, native_enum=False), nullable=False)
    gender = Column(Enum(GenderEnum, native_enum=False), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    answers = relationship("Answer", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False)
    type = Column(Enum(ImageTypeEnum, native_enum=False), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    question = relationship("Question", back_populates="image", uselist=False)

    def __repr__(self):
        return f"<Image(id={self.id}, url='{self.url}', type='{self.type.value}')>"

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_id = Column(Integer, ForeignKey('images.id'), nullable=False)
    title = Column(String(100), nullable=False)
    sqe = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    image = relationship("Image", back_populates="question")
    choices = relationship("Choice", back_populates="question", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Question(id={self.id}, title='{self.title}', sqe={self.sqe})>"

class Choice(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    content = Column(String(255), nullable=False)
    sqe = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    question = relationship("Question", back_populates="choices")
    answers = relationship("Answer", back_populates="choice")

    def __repr__(self):
        return f"<Choice(id={self.id}, content='{self.content}', sqe={self.sqe})>"

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    choice_id = Column(Integer, ForeignKey('choices.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="answers")
    choice = relationship("Choice", back_populates="answers")

    def __repr__(self):
        return f"<Answer(id={self.id}, user_id={self.user_id}, choice_id={self.choice_id})>"

# 데이터베이스 연결 및 세션 설정 함수들
def create_database_engine(database_url="sqlite:///survey.db"):
    """
    데이터베이스 엔진을 생성합니다.
    기본값으로 SQLite를 사용하지만, 다른 데이터베이스 URL도 지원합니다.
    """
    engine = create_engine(database_url, echo=True)
    return engine

def create_tables(engine):
    """
    모든 테이블을 생성합니다.
    """
    Base.metadata.create_all(engine)

def get_session(engine):
    """
    데이터베이스 세션을 생성합니다.
    """
    Session = sessionmaker(bind=engine)
    return Session()
