# 설치: pip install openai
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")  # 또는 env var로 설정

resp = client.chat.completions.create(
    model="gpt-4o",            # 또는 사용 가능한 모델 이름 (예: gpt-5.1 등)
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "안녕, 오늘 날씨 어때?"}
    ],
    max_tokens=300
)

# 응답 출력
print(resp.choices[0].message.content)