const response = {
  hobbies: ["글쓰기", "독서", "드로잉"],
  most_frequent: "글쓰기",
  frequency: "주 3~4회",
  with_who: "혼자",
  monthly_spend: "1만~3만 원",
  stress_relief: "매우 그렇다",
  new_hobby: "네",
  want_hobby: "캘리그래피",
  reason_keep: "재미있어서",
  hobby_meaning: "감정 표현의 수단"
};

function analyzeTags(res) {
  const tags = [];

  // 사교성
  if (res.with_who === "혼자") tags.push("혼자");
  else if (res.with_who.includes("친구") || res.with_who.includes("동호회")) tags.push("사교적");

  // 감성/창의
  if (res.hobby_meaning.includes("감정") || res.hobbies.includes("드로잉")) {
    tags.push("감성적", "창의적");
  }

  // 꾸준함
  if (["매일", "주 3~4회"].includes(res.frequency)) tags.push("꾸준함");

  // 내향적
  if (res.hobbies.includes("글쓰기") || res.hobbies.includes("독서")) tags.push("내향적");

  return [...new Set(tags)];
}

function recommendByTags(tags) {
  const tagSet = new Set(tags);

  if (tagSet.has("혼자") && tagSet.has("감성적") && tagSet.has("창의적")) {
    return {
      type: "감성 창작형",
      tagsText: "혼자이고 감성적인 당신을 위한 취미!",
      hobbies: ["캘리그래피", "드로잉", "글쓰기", "손글씨"]
    };
  }

  if (tagSet.has("사교적") && tagSet.has("꾸준함")) {
    return {
      type: "열정적 사교형",
      tagsText: "사교적이고 꾸준한 당신을 위한 취미!",
      hobbies: ["댄스", "러닝크루", "보드게임"]
    };
  }

  if (tagSet.has("내향적") && tagSet.has("꾸준함")) {
    return {
      type: "내향 몰입형",
      tagsText: "조용히 몰입하는 걸 좋아하는 당신을 위한 취미!",
      hobbies: ["에세이 쓰기", "프라모델", "독서", "블로그"]
    };
  }

  return {
    type: "일반형",
    tagsText: "당신에게 잘 맞는 취미는?",
    hobbies: ["독서", "요리", "영화 감상"]
  };
}

function renderResult(res) {
  const tags = analyzeTags(res);
  const result = recommendByTags(tags);

  const resultCard = document.getElementById("resultCard");
  resultCard.innerHTML = `
    <h3 class="mb-3">🧠 성향 분석 결과: <span class="text-primary">${result.type}</span></h3>

    <hr class="my-4">

    <h5>📌 당신의 응답 요약</h5>
    <ul class="list-group list-group-flush">
      <li class="list-group-item"><strong>가장 자주 하는 취미:</strong> ${res.most_frequent}</li>
      <li class="list-group-item"><strong>활동 빈도:</strong> ${res.frequency}</li>
      <li class="list-group-item"><strong>함께 하는 방식:</strong> ${res.with_who}</li>
      <li class="list-group-item"><strong>스트레스 해소 도움:</strong> ${res.stress_relief}</li>
      <li class="list-group-item"><strong>지금 해보고 싶은 취미:</strong> ${res.want_hobby}</li>
    </ul>

    <div class="mt-4 p-3 bg-success bg-opacity-10 rounded">
      <strong>✨ ${result.tagsText}</strong><br>
      ${result.hobbies.join(" · ")}
    </div>
  `;
}

renderResult(response);
