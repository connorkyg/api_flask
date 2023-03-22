from flask import Flask

def create_app():
    app = Flask(__name__)
    # Flask 애플리케이션 객체 생성
    # 블루프린트 등록, 로깅 설정 등의 작업 수행
    return app
