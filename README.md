# 브릿지AI — 웹소설 AI 창작 플랫폼

> GitHub Pages 배포 버전

## 🌐 테스트 접속

**URL**: `https://[깃허브계정].github.io/bridge-ai/`

입장 코드를 입력하면 바로 사용할 수 있습니다.

---

## 📁 파일 구조

```
bridge-ai/
├── docs/
│   └── index.html     ← 실제 앱 (GitHub Pages가 이 파일을 서빙)
└── README.md
```

---

## 🚀 GitHub Pages 설정 방법

1. 이 저장소를 GitHub에 push
2. GitHub 저장소 → **Settings** → **Pages**
3. Source: `Deploy from a branch`
4. Branch: `main` / 폴더: `/docs`
5. **Save** 클릭
6. 몇 분 후 `https://[계정].github.io/[저장소명]/` 접속 가능

---

## 🔐 입장 코드 변경 방법

입장 코드를 바꾸려면 아래 Python 스크립트를 실행 후
`docs/index.html`의 `const _EK = "..."` 값을 교체하세요.

```python
import base64

API_KEY = "sk-ant-..."        # 실제 Claude API 키
ACCESS_CODE = "새입장코드"     # 원하는 입장 코드

def xor_encrypt(text, key):
    result = []
    for i, c in enumerate(text):
        result.append(chr(ord(c) ^ ord(key[i % len(key)])))
    return base64.b64encode(''.join(result).encode('latin-1')).decode()

print(xor_encrypt(API_KEY, ACCESS_CODE))
```

---

## ⚠️ 보안 주의사항

- API 키는 소스코드에 **직접 노출되지 않습니다**
- 입장 코드 없이는 API 키를 추출할 수 없습니다
- 단, 입장 코드를 아는 사람은 API를 사용할 수 있으므로
  테스트 종료 후 Anthropic 콘솔에서 해당 키를 **비활성화**하세요
- 테스트용 키는 별도로 발급하는 것을 권장합니다

---

## 📝 테스터에게 전달할 정보

```
🔗 접속 URL: https://[계정].github.io/bridge-ai/
🔑 입장 코드: [입장코드]

사용 방법:
1. URL 접속 → 입장 코드 입력
2. 장르 선택 후 소설 작성 시작
3. 피드백은 [연락처]로 전달해 주세요
```
