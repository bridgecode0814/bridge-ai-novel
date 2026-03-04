"""
입장 코드 변경 스크립트
========================
입장 코드를 바꾸고 싶을 때 이 스크립트를 실행하세요.
출력된 값을 docs/index.html의 _EK 변수에 붙여넣으면 됩니다.

사용법: python3 rotate_code.py
"""

import base64

# ── 여기만 수정하세요 ──────────────────────────────────────────
API_KEY     = "sk-ant-api03-..."   # 실제 Claude API 키를 넣으세요
ACCESS_CODE = "bridge2025"         # 새 입장 코드를 정하세요
# ──────────────────────────────────────────────────────────────


def xor_encrypt(text, key):
    result = []
    for i, c in enumerate(text):
        result.append(chr(ord(c) ^ ord(key[i % len(key)])))
    return base64.b64encode(''.join(result).encode('latin-1')).decode()


def xor_decrypt(enc, key):
    decoded = base64.b64decode(enc.encode()).decode('latin-1')
    result = []
    for i, c in enumerate(decoded):
        result.append(chr(ord(c) ^ ord(key[i % len(key)])))
    return ''.join(result)


if __name__ == "__main__":
    encrypted = xor_encrypt(API_KEY, ACCESS_CODE)
    verified  = xor_decrypt(encrypted, ACCESS_CODE)

    print("=" * 60)
    print(f"  입장 코드   : {ACCESS_CODE}")
    print(f"  암호화된 값 : {encrypted}")
    print(f"  검증        : {'✅ 정상' if verified == API_KEY else '❌ 오류'}")
    print("=" * 60)
    print()
    print("▶ docs/index.html 에서 아래 줄을 찾아 교체하세요:")
    print()
    print(f'  const _EK = "{encrypted}";')
    print()
    print("▶ 테스터에게 알려줄 정보:")
    print(f"  입장 코드: {ACCESS_CODE}")
