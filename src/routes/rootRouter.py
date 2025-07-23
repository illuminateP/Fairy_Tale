from flask import Blueprint, render_template, jsonify
import json
import os
from src.models.qa_model import qa_infer

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

@root_bp.route('/ask', methods=['GET'])
def ask():
    meta_path = os.path.join(os.path.dirname(__file__), '../resources/meta/book_meta_all.json')
    with open(meta_path, encoding='utf-8-sig') as f:
        books = json.load(f)
    return render_template('ask.html', books=books)

@root_bp.route('/api/book_content', methods=['POST'])
def book_content():
    from flask import request, jsonify
    data = request.get_json()
    isbn = data.get('isbn')
    if not isbn:
        return jsonify({'error': 'ISBN이 필요합니다.'}), 400
    sublabel_path = os.path.join(os.path.dirname(__file__), '../resources/sublabel', f'{isbn}.json')
    if not os.path.exists(sublabel_path):
        return jsonify({'error': '책 내용 파일이 없습니다.'}), 404
    with open(sublabel_path, encoding='utf-8-sig') as f:
        try:
            content = json.load(f)
        except Exception as e:
            return jsonify({'error': f'JSON 파싱 오류: {str(e)}'}), 500
    return jsonify({'content': content})

@root_bp.route('/api/ask_question', methods=['POST'])
def ask_question():
    from flask import request, jsonify
    data = request.get_json()
    text = data.get('text')
    question = data.get('question')
    if not text or not question:
        return jsonify({'error': '본문과 질문이 모두 필요합니다.'}), 400
    print("\n[질문하기 API 호출]")
    print("[본문(srctext)]\n" + text)
    print("[질문]", question)
    try:
        answer = qa_infer(question, text)
    except Exception as e:
        return jsonify({'error': f'모델 예측 오류: {str(e)}'}), 500
    return jsonify({'answer': answer}) 