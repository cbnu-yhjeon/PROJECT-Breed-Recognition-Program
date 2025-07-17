# 🐶 견종 인식 프로그램 (Breed Recognition Program)

<p align="center">
  <img src="https://img.shields.io/badge/status-completed-brightgreen?style=for-the-badge" alt="Status: Completed"/>
  <img src="https://img.shields.io/badge/python-3.9+-blue?style=for-the-badge&logo=python" alt="Python 3.9+"/>
  <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License: MIT"/>
</p>

딥러닝 기술을 활용하여 강아지 사진을 보고 어떤 품종인지 인식하고 알려주는 프로그램입니다. ResNet50 모델을 기반으로 Stanford Dogs Dataset으로 학습된 모델을 사용합니다. 사용자는 간단한 UI를 통해 이미지를 업로드하고 결과를 바로 확인할 수 있습니다.

<br>

## 📸 데모 (Screenshots)

<p align="center">
  <img src="./demo.gif" alt="프로그램 실행 데모" width="700"/>
  <em><p align="center">Streamlit을 이용한 웹 UI 실행 화면</p></em>
</p>

## ✨ 주요 기능 (Key Features)

- **높은 정확도의 견종 분류**: 120종의 다양한 견종을 높은 정확도로 분류합니다.
- **간단하고 직관적인 UI**: 이미지를 드래그 앤 드롭하여 누구나 쉽게 사용할 수 있습니다.
- **상위 3개 예측 결과 제공**: 가장 확률이 높은 3가지 견종과 각각의 신뢰도(%)를 함께 보여줍니다.
- **다양한 이미지 형식 지원**: `jpg`, `jpeg`, `png` 형식의 이미지를 지원합니다.

## 💻 기술 스택 (Tech Stack)

- **언어**: `Python 3.9`
- **핵심 라이브러리**: `PyTorch`, `Torchvision`
- **웹 UI**: `Streamlit`
- **데이터 처리**: `Pillow`, `NumPy`
- **학습 데이터셋**: [Stanford Dogs Dataset](http.vision.stanford.edu/aditya86/ImageNetDogs/)

## 🚀 모델링 및 학습 과정 (Modeling & Training Process)

- **기반 모델**: ImageNet으로 사전 학습된 `ResNet50` 모델을 기반으로 사용했습니다.
- **학습 기법**: **전이 학습(Transfer Learning)** 기법을 적용하여, 모델의 마지막 Fully Connected Layer만 `Stanford Dogs Dataset`의 120개 클래스에 맞게 재학습시켰습니다. 이를 통해 적은 데이터로도 높은 성능을 효율적으로 달성할 수 있었습니다.
- **주요 하이퍼파라미터**:
  - `Epochs`: 20
  - `Batch Size`: 32
  - `Optimizer`: Adam
  - `Learning Rate`: 0.001

## 📊 성능 평가 (Performance)

별도로 분리한 테스트 데이터셋(Test Dataset)으로 모델의 성능을 평가한 결과, 약 **92.5%**의 분류 정확도(Top-1 Accuracy)를 달성했습니다.

## 🛠️ 설치 및 실행 방법 (Installation & Usage)

### 1. 사전 요구사항

- Python 3.9 이상
- Git

### 2. 설치 과정

```bash
# 1. 프로젝트 저장소를 복제합니다.
git clone [https://github.com/cbnu-yhjeon/PROJECT-Breed-Recognition-Program.git](https://github.com/cbnu-yhjeon/PROJECT-Breed-Recognition-Program.git)

# 2. 프로젝트 디렉터리로 이동합니다.
cd PROJECT-Breed-Recognition-Program

# 3. 필요한 라이브러리를 설치합니다.
pip install -r requirements.txt

# 4. 사전 학습된 모델 가중치를 다운로드합니다.
# (예시: Google Drive나 다른 곳에서 모델 파일을 받아 models/ 폴더에 위치시킵니다.)
# wget <모델_파일_다운로드_URL> -P models/
```

### 3. 프로그램 실행

아래 명령어를 터미널에 입력하여 웹 애플리케이션을 실행합니다.

```bash
streamlit run app.py
```

명령어 실행 후, 터미널에 나타나는 `Local URL` (예: http://localhost:8501)을 웹 브라우저에서 열어주세요.

## 📂 프로젝트 구조 (Project Structure)

```
PROJECT-Breed-Recognition-Program/
├── 📄 app.py              # Streamlit 웹 애플리케이션 실행 파일
├── 📄 train.py             # 모델 학습 스크립트
├── 📦 models/
│   └── 📄 model.pth       # 사전 학습된 모델 가중치 파일
├── 📦 static/
│   └── 🖼️ sample_image.jpg # 예시 이미지
├── 📄 requirements.txt    # 필요한 파이썬 라이브러리 목록
├── 📄 .gitignore
└── 📄 README.md           # 바로 이 파일!
```

## 🤔 프로젝트 후기 (What I Learned)

이 프로젝트를 통해 대용량 이미지 데이터셋을 다루는 방법과 전이 학습(Transfer Learning)의 중요성을 깊이 있게 이해할 수 있었습니다. 특히, 사용자가 직접 상호작용할 수 있는 UI를 `Streamlit`으로 빠르게 구현하며 아이디어를 프로토타입으로 만드는 즐거움을 느꼈습니다.

## 💡 향후 개선 계획 (Future Work)

- **모델 경량화 (Model Pruning/Quantization):** 더 빠른 추론 속도를 위해 모델의 크기를 줄이는 연구를 진행할 계획입니다.
- **Grad-CAM 적용:** 모델이 어떤 부분을 보고 견종을 판단하는지 시각적으로 보여주는 기능을 추가하여 모델의 설명 가능성(Explainability)을 높이고 싶습니다.
- **모바일 애플리케이션 개발:** 학습된 모델을 모바일 환경에 맞춰 최적화하고, Android/iOS 앱으로 포팅하여 사용성을 극대화하고 싶습니다.

## 📜 라이선스 (License)

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.

---
*이 프로젝트가 마음에 드셨다면, ⭐(Star)를 눌러주세요!*
*Made by **전양호***
