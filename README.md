# CNU_Enrolment_Macro

## Things to install설치해야할 것들
(개발환경 : Windows 10, Python 3.7.0)
Python 3.7.0
pip install Pillow
pip install pytesseract
pip install pyperclip
pip install pyautogui
pip install opencv-python
pip install numpy
pip install python3_xlib

pip3에 python3가깔려있다면 pip -> pip3로 변경 후 install
ex)pip3 install Pillow

## 변수 설정
CNU_Macro.py 파일 안의 변수 개인에 맞게끔 수정

## CNU_Macro.py 프로그램 실행
(실행 후 크롬을 foreground process로 바꾸기)

### 유의사항
- capture.png에 나오는 숫자들 밑에 밑줄이 안나오게끔 변수를 설정해야 정확도가 향상됩니다.(STEP 3 - 관련 변수명 : numCodeX(constant area), numCodeY(constant area), width, height)
- capture.png는 실행 후 생성됩니다.
- 프로그램 사용으로 일어나는 모든 책임은 사용자에게 있습니다.