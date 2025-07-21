from flask import Blueprint, render_template, redirect, url_for, request

questions_bp = Blueprint("questions", __name__, url_prefix="/questions")

# 설문 문항 데이터 (각 문항과 선택지 정의)
questions = [
    {
        "id": 1,
        "title": "현재 즐기고 있는 취미는 무엇인가요? (복수 선택 가능)",
        "choices": [
            "독서", "영화/드라마 감상", "음악 감상", "악기 연주", "노래/보컬",
            "운동 (헬스, 요가, 러닝 등)", "등산", "자전거 타기", "수영",
            "게임 (콘솔, PC, 모바일 등)", "그림 그리기/캘리그라피", "글쓰기/일기",
            "요리/베이킹", "사진 촬영", "영상 제작/편집", "춤/댄스", "뜨개질/자수",
            "공예(DIY, 레진, 미니어처 등)", "퍼즐/보드게임", "정원 가꾸기/식물 키우기",
            "여행/캠핑", "애완동물 돌보기", "자원봉사", "기타"
        ],
        "multiple": True,
        "other": True
    },
    {
        "id": 2,
        "title": "하루 평균 취미 활동에 투자하는 시간은?",
        "choices": [
            "30분 이하", "30분~1시간", "1~2시간",
            "2~3시간", "3시간 이상", "시간이 날 때마다 다름"
        ]
    },
    {
        "id": 3,
        "title": "주로 취미를 즐기는 시간대는 언제인가요?",
        "choices": [
            "새벽", "오전", "오후", "저녁", "밤", "일정하지 않음"
        ]
    },
    {
        "id": 4,
        "title": "취미를 주로 누구와 함께 하나요?",
        "choices": [
            "혼자", "친구", "가족", "동호회/모임", "온라인 커뮤니티", "기타"
        ],
        "other": True
    },
    {
        "id": 5,
        "title": "최근 6개월 내 새롭게 시작한 취미가 있나요?",
        "choices": [
            "예", "아니오", "시도했지만 그만둠"
        ],
        "other": True  # 예일 경우 입력 필드
    },
    {
        "id": 6,
        "title": "가장 오래 해온 취미는 무엇인가요?",
        "choices": [],
        "text_only": True
    },
    {
        "id": 7,
        "title": "취미 활동을 통해 얻는 가장 큰 만족감은 무엇인가요?",
        "choices": [
            "스트레스 해소", "성취감", "창의력 향상", "체력 증진",
            "자기 표현", "새로운 사람과의 교류", "단순한 재미", "기타"
        ],
        "other": True
    },
    {
        "id": 8,
        "title": "새롭게 도전해보고 싶은 취미는 무엇인가요? (복수 선택 가능)",
        "choices": [
            "스카이다이빙", "스쿠버다이빙", "서핑", "사진/영상 촬영",
            "캠핑/차박", "해외 여행", "악기 배우기", "요리 마스터하기",
            "운동/바디 프로필", "플라워 클래스", "미술/도예",
            "펫 관련 활동", "자격증 취득 취미", "유튜브/Vlog 제작", "기타"
        ],
        "multiple": True,
        "other": True
    },
    {
        "id": 9,
        "title": "온라인 취미 활동에 대해 어떻게 생각하시나요?",
        "choices": [
            "매우 즐긴다", "종종 한다", "가끔 한다",
            "거의 하지 않는다", "온라인보다 오프라인 활동 선호"
        ]
    },
    {
        "id": 10,
        "title": "취미 활동에 월 평균으로 얼마나 지출하시나요?",
        "choices": [
            "거의 지출 없음", "1만 원 이하", "1~5만 원",
            "5~10만 원", "10만 원 이상", "금액은 들지만 아깝지 않다"
        ]
    }
]

# 질문 렌더링
@questions_bp.route("/<int:question_id>", methods=["GET", "POST"])
def question_page(question_id):
    if question_id < 1 or question_id > len(questions):
        return redirect(url_for("questions.question_page", question_id=1))

    question = questions[question_id - 1]

    if request.method == "POST":
        # 사용자 응답 처리 로직 필요시 여기에 추가
        next_id = question_id + 1
        if next_id > len(questions):
            return redirect(url_for("questions.complete"))
        return redirect(url_for("questions.question_page", question_id=next_id))

    return render_template("survey.html", question=question)

# 설문 완료 페이지
@questions_bp.route("/complete")
def complete():
    return render_template("complete.html")