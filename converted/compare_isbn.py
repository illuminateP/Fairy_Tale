import os
import re
import json

# 경로 설정
sublabel_dir = os.path.join(os.path.dirname(__file__), 'sublabel')
source_dir = os.path.join(os.path.dirname(__file__), 'training', '01.원천데이터')

# ISBN 추출 함수 (파일명에서)
def extract_isbn(filename):
    match = re.search(r'(97[89][0-9A-Za-z]{10}|[0-9]{9,10}[0-9Xx])', filename)
    return match.group(1) if match else None

# Sublabel ISBN 목록
sublabel_isbns = set()
for fname in os.listdir(sublabel_dir):
    if fname.endswith('.json'):
        isbn = extract_isbn(fname)
        if isbn:
            sublabel_isbns.add(isbn)

# 원천데이터 ISBN 목록 (하위 폴더까지)
source_isbns = set()
for root, dirs, files in os.walk(source_dir):
    for fname in files:
        if fname.endswith('.json'):
            isbn = extract_isbn(fname)
            if isbn:
                source_isbns.add(isbn)

# 비교
only_in_sublabel = sublabel_isbns - source_isbns
only_in_source = source_isbns - sublabel_isbns
in_both = sublabel_isbns & source_isbns

print(f'Sublabel에만 있는 ISBN 개수: {len(only_in_sublabel)}')
print(f'원천데이터에만 있는 ISBN 개수: {len(only_in_source)}')
print(f'둘 다 있는 ISBN 개수: {len(in_both)}')

if only_in_sublabel:
    print('\nSublabel에만 있는 ISBN:')
    for isbn in sorted(only_in_sublabel):
        print(isbn)
if only_in_source:
    print('\n원천데이터에만 있는 ISBN:')
    for isbn in sorted(only_in_source):
        print(isbn)

# (선택) 둘 다 있는 ISBN 중 텍스트 비교 (샘플 3개)
def get_sublabel_text(isbn):
    for fname in os.listdir(sublabel_dir):
        if isbn in fname:
            with open(os.path.join(sublabel_dir, fname), encoding='utf-8') as f:
                data = json.load(f)
                return data.get('text', '').strip()
    return None

def get_source_text(isbn):
    for root, dirs, files in os.walk(source_dir):
        for fname in files:
            if isbn in fname:
                with open(os.path.join(root, fname), encoding='utf-8') as f:
                    data = json.load(f)
                    # 문단별 텍스트 이어붙이기
                    if 'paragraphInfo' in data:
                        return '\n'.join([p['srcText'].strip() for p in data['paragraphInfo']])
    return None

print('\n---\n모든 ISBN 텍스트 비교 결과:')
match_count = 0
mismatch_count = 0
mismatch_isbns = []

for isbn in sorted(in_both):
    sublabel_text = get_sublabel_text(isbn)
    source_text = get_source_text(isbn)
    if sublabel_text and source_text:
        if sublabel_text.replace('\n', '').replace(' ', '') == source_text.replace('\n', '').replace(' ', ''):
            match_count += 1
        else:
            mismatch_count += 1
            mismatch_isbns.append(isbn)
    else:
        mismatch_count += 1
        mismatch_isbns.append(isbn)

print(f'텍스트 완전 일치: {match_count}권')
print(f'텍스트 불일치: {mismatch_count}권')
if mismatch_isbns:
    print('\n불일치 ISBN:')
    for isbn in mismatch_isbns:
        print(isbn) 