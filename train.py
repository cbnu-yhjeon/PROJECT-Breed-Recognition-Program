# train.py
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import os

# --- 설정 변수 ---
STUDENT_ID = '2025254002'
IMAGE_SIZE = 224
BATCH_SIZE = 32
DATA_DIR = 'Images' # Stanford Dogs Dataset의 'Images' 폴더 경로

# --- 1. 데이터 준비 ---
# ImageDataGenerator를 사용해 이미지 증강 및 데이터 로드
# 학습 데이터는 증강을 적용하고, 검증 데이터는 단순 스케일링만 적용
train_datagen = ImageDataGenerator(
    rescale=1./255.,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2 # 20%를 검증 데이터로 사용
)

train_generator = train_datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training' # 학습용 데이터
)

validation_generator = train_datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation' # 검증용 데이터
)

# --- 2. 견종 이름 파일 저장 ---
# 생성기에서 클래스(견종) 이름을 가져와 txt 파일로 저장
class_names = list(train_generator.class_indices.keys())
# 폴더명에서 'n******-' 부분을 제거하여 순수 견종 이름만 남김
cleaned_class_names = [name.split('-', 1)[1] for name in class_names]

with open('dog_species_name.txt', 'w') as f:
    for name in cleaned_class_names:
        f.write(f"{name}\n")

print(f"견종 목록을 'dog_species_name.txt' 파일로 저장했습니다.")

# --- 3. 모델 구축 (사전학습 모델 + Fine-tuning) ---
# ImageNet으로 사전학습된 MobileNetV2 모델을 불러옴 (분류기는 제외)
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3))

# 사전학습된 층은 동결하여 가중치 업데이트를 막음
base_model.trainable = False

# 새로운 분류기(Classifier) 추가
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
x = Dropout(0.5)(x)
# 출력층: 120개 견종 클래스 수에 맞게 설정
predictions = Dense(len(class_names), activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# --- 4. 모델 컴파일 및 학습 ---
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# 최적의 모델을 저장하기 위한 콜백 설정
model_checkpoint = ModelCheckpoint(
    filepath=f'{STUDENT_ID}.h5', # <학번>.h5 형식으로 저장
    save_best_only=True,
    monitor='val_loss',
    mode='min',
    verbose=1
)

early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=5,
    verbose=1,
    restore_best_weights=True
)

# 모델 학습 시작
history = model.fit(
    train_generator,
    epochs=20, # 필요에 따라 에포크 수 조정
    validation_data=validation_generator,
    callbacks=[model_checkpoint, early_stopping]
)

print(f"\n✅ 학습 완료! 최적의 모델이 '{STUDENT_ID}.h5' 파일로 저장되었습니다.")