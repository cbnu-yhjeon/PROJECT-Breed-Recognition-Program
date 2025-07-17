# recognize.py
import tensorflow as tf
import numpy as np
import cv2  # OpenCV 라이브러리
import os

# --- 설정 변수 ---
STUDENT_ID = '2025254002'
MODEL_PATH = f'{STUDENT_ID}.h5'
CLASS_NAME_PATH = 'dog_species_name.txt'
TEST_IMAGE_PATH = 'pug.jpg'  # 테스트할 이미지 파일 경로
IMAGE_SIZE = 224

# --- 1. 모델 및 클래스 이름 로드 ---
# 학습된 모델(.h5) 파일 로드
try:
    model = tf.keras.models.load_model(MODEL_PATH)
except IOError:
    print(f"오류: 모델 파일 '{MODEL_PATH}'을 찾을 수 없습니다. train.py를 먼저 실행하세요.")
    exit()

# 견종 이름(txt) 파일 로드
try:
    with open(CLASS_NAME_PATH, 'r') as f:
        class_names = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(f"오류: 견종 이름 파일 '{CLASS_NAME_PATH}'을 찾을 수 없습니다. train.py를 먼저 실행하세요.")
    exit()

# --- 2. 이미지 로드 및 전처리 ---
try:
    image = cv2.imread(TEST_IMAGE_PATH)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV는 BGR, TensorFlow는 RGB
except cv2.error:
    print(f"오류: 테스트 이미지 '{TEST_IMAGE_PATH}'를 찾을 수 없거나 손상되었습니다.")
    exit()

# 모델 입력에 맞게 이미지 크기 조정 및 정규화
resized_image = cv2.resize(image_rgb, (IMAGE_SIZE, IMAGE_SIZE))
input_image = np.expand_dims(resized_image, axis=0) / 255.0  # 배치 차원 추가 및 정규화

# --- 3. 견종 예측 ---
predictions = model.predict(input_image)

# 확률이 높은 순으로 5개 인덱스 추출
top_5_indices = np.argsort(predictions[0])[::-1][:5]

print("--- 예측 결과 (상위 5개) ---")

# --- 4. 결과 이미지 생성 및 저장 ---
# 결과 텍스트를 표시할 시작 위치 (y 좌표)
y_pos = 50
for i, index in enumerate(top_5_indices):
    # 확률과 품종 이름 가져오기
    probability = predictions[0][index]
    breed_name = class_names[index]

    # 출력 텍스트 생성
    text = f"({probability:.8f}){breed_name}"
    print(text)

    # 이미지에 텍스트 그리기
    cv2.putText(
        image,
        text,
        (10, y_pos),  # 텍스트 위치 (x, y)
        cv2.FONT_HERSHEY_SIMPLEX,  # 폰트
        2.0,  # 폰트 크기
        (0, 255, 0),  # 폰트 색상 (녹색)
        2,  # 폰트 두께
        cv2.LINE_AA
    )
    y_pos += 60  # 다음 텍스트를 위해 y 좌표 이동

# 결과 이미지를 <학번>.png 파일로 저장
output_path = f'{STUDENT_ID}.png'
cv2.imwrite(output_path, image)

print(f"\n✅ 인식 완료! 결과가 '{output_path}' 파일로 저장되었습니다.")