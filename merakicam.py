import meraki
import requests
import time
import ocr

start_time=time.time() 
API_KEY = 'b9466f2bb4bc9b6f9c1e99fb46c36fcce3563797' 
dashboard = merakicam.DashboardAPI(API_KEY)  # 본인 api 키를 이용해서 dashboard 접근
end_time = time.time()
execution_time = end_time - start_time
print("dashboard 접근시간: {} 초".format(execution_time))
serial = 'Q2GV-GF7Q-9VQQ'  # 사용하고자 하는 메라키 카메라 시리얼넘버

def download_image(filename): 
    start_time=time.time() 
    response = dashboard.camera.generateDeviceCameraSnapshot (  # 현재 실시간 카메라로 접근가능한 url을 뽑아낸다.
        serial
    )
    print(response)
    url = response['url']
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("이미지 다운로드 완료")
        end_time = time.time()
        execution_time = end_time - start_time
        print("이미지 다운로드 시간: {} 초".format(execution_time))
    else:
        print("이미지를 다운로드할 수 없습니다.")

filename = "image.jpg"  # 저장할 파일명