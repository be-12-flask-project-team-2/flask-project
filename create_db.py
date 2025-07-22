# create_db.py
from app import app, db
from app.models import User, Question, Choice, Answer, Image

def create_database():
    """데이터베이스와 모든 테이블을 생성합니다."""
    with app.app_context():
        try:
            # 모든 테이블 생성
            db.create_all()
            
            print("✅ 데이터베이스가 성공적으로 생성되었습니다!")
            print(f"📁 저장 위치: instance/project.db")
            
            # 테이블 목록 확인
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"📋 생성된 테이블: {', '.join(tables)}")
            
        except Exception as e:
            print(f"❌ 오류 발생: {e}")

if __name__ == '__main__':
    create_database()