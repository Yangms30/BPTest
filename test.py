# test용입니다.2 yang
# ㅉㅁㄴㅇㅁㄴㅇ
# ㅁㄴㅇㄹㅁㄴㅇㄹ


def reverse_string(text):
    """문자열을 뒤집는 함수"""
    return text[::-1]


# 테스트 실행
if __name__ == "__main__":
    print("=== 문자열 뒤집기 테스트 ===")
    test_text = "안녕하세요"
    print(f"원본: {test_text}")
    print(f"뒤집기: {reverse_string(test_text)}")

    test_text2 = "Python"
    print(f"원본: {test_text2}")
    print(f"뒤집기: {reverse_string(test_text2)}")
