project(CHEESE_ENGINE)
cmake_minimum_required(VERSION 3.5.1)


file(GLOB_RECURSE SRCs src/*.py)
add_executable(${PROJECT_NAME} ${SRCs})
target_include_directories(${PROJECT_NAME} PUBLIC include)

pyinstaller --noconfirm --onefile --windowed --add-data "/home/gumball/.local/lib/python3.11/site-packages/customtkinter/assets/themes/blue.json:customtkinter/assets/themes" --add-data "/home/gumball/.local/lib/python3.11/site-packages/customtkinter/assets/fonts/Roboto/Roboto-Regular.ttf:customtkinter/assets/fonts/Roboto" --add-data "/home/gumball/.local/lib/python3.11/site-packages/customtkinter/assets/fonts/Roboto/Roboto-Medium.ttf:customtkinter/assets/fonts/Roboto" --add-data "/home/gumball/.local/lib/python3.11/site-packages/customtkinter/assets/fonts/CustomTkinter_shapes_font.otf:customtkinter/assets/fonts" --hidden-import=PIL --hidden-import=PIL._tkinter_finder --add-data "/home/gumball/.local/lib/python3.11/site-packages/face_recognition_models/models/shape_predictor_68_face_landmarks.dat:face_recognition_models/models" --add-data "/home/gumball/.local/lib/python3.11/site-packages/face_recognition_models/models/shape_predictor_5_face_landmarks.dat:face_recognition_models/models" --add-data "/home/gumball/.local/lib/python3.11/site-packages/face_recognition_models/models/mmod_human_face_detector.dat:face_recognition_models/models" --add-data "/home/gumball/.local/lib/python3.11/site-packages/face_recognition_models/models/dlib_face_recognition_resnet_model_v1.dat:face_recognition_models/models"  src/main.py
