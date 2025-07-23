from .utils.app import create_app # app.py에서 create_app 함수를 가져옵니다.

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # 개발 중에는 debug=True 사용, 포트 변경 가능 (예: port=5001) 