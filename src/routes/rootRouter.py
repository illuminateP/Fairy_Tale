from flask import Blueprint, render_template, jsonify

# Blueprint 이름을 파일명 및 기능에 맞춰 root_bp로 변경합니다.
root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/')
def index():
    """온보딩 페이지 (루트 경로)를 보여줍니다."""
    return render_template('index.html', title='환영합니다!')

# 서버 상태 반환
@root_bp.route('/test')
def test_server():
    response_data = {
        "message": "이게 보인다면 서버가 살아 있다는 뜻입니다. 아마도요."
    }
    return render_template('test.html', data=response_data) 