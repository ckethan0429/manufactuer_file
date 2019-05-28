import os
# mac
# os.chdir('/users/student/~~~')

# 파일의 주소로 이동
os.chdir(r'C:\Users\student\Desktop\CK\manufactuer_file\dummy_ex')
# 파일의 목록 리스트얻기
filenames = os.listdir('.')
for filename in filenames:
    txt = os.path.splitext(filename)[-1].lower()
    if txt == '.txt':
        # os.rename(filename, f'지원자_{filename}')
        os.rename(filename, filename.replace('지원자','합격자'))
