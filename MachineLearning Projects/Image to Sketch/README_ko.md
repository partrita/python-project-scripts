# 파이썬을 사용하여 이미지를 연필 스케치로 변환

👉 여기서 임무는 이미지를 연필 스케치로 변환하는 것입니다.

![dog](https://user-images.githubusercontent.com/82924828/191065579-f0f29b4f-dda3-44f1-985d-042e11086e49.jpg)

👉 먼저 RGB 이미지를 회색조로 변환합니다.

![download](https://user-images.githubusercontent.com/82924828/191065626-8caf751d-5480-452a-81a5-78d6cd21ab5f.png)

👉 그런 다음 회색조를 회색조 이미지를 반전시키는 네거티브 이미징으로 변환합니다.

![dog_sketch](https://user-images.githubusercontent.com/82924828/191066033-04489ba7-1c13-4f0d-ae7c-60e82c12f2a7.jpg)

👉 이것은 회색조 이미지를 반전된 흐릿한 이미지로 나누어 수행할 수 있습니다.


![dog_sketch2](https://user-images.githubusercontent.com/82924828/191066150-a770a274-546a-47eb-ad4b-24fdcdd8fdfe.jpg)

👉 이러한 작업은 cv2 라이브러리를 사용하여 수행할 수 있습니다.
