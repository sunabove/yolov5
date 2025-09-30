import cv2
import sys

# 카메라 장치 열기 (0은 기본 카메라)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    sys.exit()

print("카메라가 성공적으로 열렸습니다. 프레임 화면을 확인하세요.")
print("'c' 키를 누르면 사진이 캡처되고, 'q' 키를 누르면 종료됩니다.")

while True:
    # 카메라에서 프레임 읽기
    ret, frame = cap.read()

    # 프레임을 성공적으로 읽지 못했을 경우
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 화면에 프레임 표시
    cv2.imshow('Camera Feed', frame)

    # 키보드 입력 대기
    key = cv2.waitKey(1) & 0xFF

    # 'c' 키를 누르면 프레임을 이미지 파일로 저장
    if key == ord('c'):
        # 이미지 파일 이름 설정
        img_name = "capture.jpg"
        # cv2.imwrite() 함수를 사용하여 이미지 저장
        cv2.imwrite(img_name, frame)
        print(f"'{img_name}' 파일로 사진이 저장되었습니다!")

    # 'q' 키를 누르면 반복문 탈출
    elif key == ord('q'):
        print("프로그램을 종료합니다.")
        break

# 사용이 끝난 후, 카메라 장치와 모든 창 닫기
cap.release()
cv2.destroyAllWindows()