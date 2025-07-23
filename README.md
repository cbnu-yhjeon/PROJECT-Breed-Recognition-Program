# 🐶 견종 인식 프로그램 (Breed Recognition Program)

<p align="center">
  <img src="https://img.shields.io/badge/status-completed-brightgreen?style=for-the-badge" alt="Status: Completed"/>
  <img src="https://img.shields.io/badge/python-3.9+-blue?style=for-the-badge&logo=python" alt="Python 3.9+"/>
  <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License: MIT"/>
</p>

TensorFlow/Keras 프레임워크와 사전 학습된 MobileNetV2 모델을 활용하여 강아지 사진의 품종을 인식하는 프로그램입니다. `train.py`를 통해 모델을 학습시키고, `recognize.py`를 통해 이미지를 입력하여 상위 5개의 예측 결과를 이미지 파일로 저장합니다.

<br>

## 📸 데모 (Screenshots)

`recognize.py` 실행 시, 테스트 이미지에 예측 확률 상위 5개의 견종 이름과 신뢰도가 표시되어 `<학번>.png` 파일로 저장됩니다.

<p align="center">
  <img src="<https://github.com/CBike/CBNU_AI/blob/main/Image_Procesing/%EA%B2%AC%EC%A2%85%EC%9D%B8%EC%8B%9D%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8/Pug_result.png?raw=true>" alt="프로그램 실행 데모" width="700"/>
  <em><p align="center">pug.jpg 이미지에 대한 인식 결과 예시</p></em>
</p>

## ✨ 주요 기능 (Key Features)

- **전이 학습 기반 모델**: ImageNet으로 사전 학습된 MobileNetV2를 사용하여 효율적으로 모델을 학습합니다.
- **데이터 증강**: `ImageDataGenerator`를 통해 이미지 회전, 이동, 확대 등을 적용하여 모델의 일반화 성능을 높입니다.
- **자동 모델 저장**: 학습 중 검증 손실(val_loss)이 가장 낮은 최적의 모델을 `<학번>.h5` 파일로 자동 저장합니다.
- **결과 시각화**: `OpenCV`를 사용하여 원본 이미지에 상위 5개 예측 결과를 텍스트로 그려 저장합니다.

## 💻 기술 스택 (Tech Stack)

- **언어**: `Python`
- **핵심 라이브러리**: `TensorFlow`, `Keras`, `OpenCV-Python`, `NumPy`
- **기반 모델**: `MobileNetV2`
- **학습 데이터셋**: Stanford Dogs Dataset

## 🗂️ 주요 파일 설명

- **`train.py`**: Stanford Dogs Dataset을 불러와 데이터 증강을 적용하고, 전이 학습을 통해 모델을 훈련시킨 후 `<학번>.h5` 모델 파일과 `dog_species_name.txt`를 생성합니다.
- **`recognize.py`**: `train.py`로 생성된 모델과 이름 파일을 로드하여, 지정된 테스트 이미지의 견종을 예측하고 결과를 텍스트로 표기한 이미지 파일(`<학번>.png`)을 저장합니다.
- **`<학번>.h5`**: 훈련된 Keras 모델 가중치 파일입니다.
- **`dog_species_name.txt`**: 120종의 견종 이름 목록입니다.
- **`<학번>.png`**: `recognize.py` 실행 시 생성되는 최종 결과 이미지입니다.

## 🛠️ 설치 및 실행 방법 (Installation & Usage)

### 1. 환경 설정

```bash
# 1. 프로젝트 저장소를 복제합니다.
git clone [https://github.com/cbnu-yhjeon/PROJECT-Breed-Recognition-Program.git](https://github.com/cbnu-yhjeon/PROJECT-Breed-Recognition-Program.git)

# 2. 프로젝트 디렉터리로 이동합니다.
cd PROJECT-Breed-Recognition-Program

# 3. 필요한 라이브러리를 설치합니다.
pip install -r requirements.txt
```
> **`requirements.txt` 내용:**
> ```txt
> tensorflow
> opencv-python
> numpy
> ```

### 2. 모델 학습 (Training)

`Stanford Dogs Dataset`의 `Images` 폴더를 프로젝트 디렉터리 내에 위치시킨 후, 아래 명령어를 실행하여 모델 학습을 시작합니다.
```bash
python train.py
```
학습이 완료되면 `2025254002.h5` 모델 파일과 `dog_species_name.txt` 파일이 생성됩니다.

### 3. 견종 인식 (Recognition)

인식하고 싶은 이미지를 프로젝트 폴더에 넣고, `recognize.py` 파일 내의 `TEST_IMAGE_PATH` 변수를 해당 이미지 파일명으로 수정한 뒤 아래 명령어를 실행합니다.
```bash
python recognize.py
```
실행이 완료되면 예측 결과가 그려진 `2025254002.png` 파일이 생성됩니다.

## 🚀 모델링 및 학습 과정 (Modeling & Training Process)

- **기반 모델**: ImageNet으로 사전 학습된 `MobileNetV2` 모델의 Convolutional Base를 사용했습니다.
- **학습 기법**: **전이 학습(Transfer Learning)**을 적용했습니다. `MobileNetV2`의 가중치는 동결(`trainable = False`)하고, 모델 위에 `GlobalAveragePooling2D`와 `Dense` Layer로 구성된 새로운 분류기만 훈련시켜 효율성을 높였습니다.
- **데이터 증강**: `ImageDataGenerator`를 사용하여 훈련 데이터에 한해 회전, 너비/높이 이동, 전단, 확대, 좌우 반전 등 다양한 증강 기법을 적용하여 모델이 과적합되는 것을 방지했습니다.
- **콜백(Callbacks)**:
    - **`ModelCheckpoint`**: 검증 손실(`val_loss`)을 기준으로 가장 성능이 좋은 모델만 파일로 저장합니다.
    - **`EarlyStopping`**: 검증 손실이 5 에포크 동안 개선되지 않으면 학습을 조기 종료하여 불필요한 훈련을 방지합니다.

## 📜 라이선스 (License)

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.

---
*이 프로젝트가 마음에 드셨다면, ⭐(Star)를 눌러주세요!*
*Made by **전양호***
