# CROWN-RaspberryPi

> 개발 환경

- **Raspberry Pi OS Debian**
- **UV4L**
- **Mosquitto MQTT Broker**
- **Bluetooth**



> 디바이스

- **Raspberry Pi 3 Model B+**
- **Web Camera**
- **Speaker**



## Setup-Raspberry Pi OS

- **Raspberry Pi Imager 설치 및 실행**

  - https://www.raspberrypi.org/software/

    <img src="https://user-images.githubusercontent.com/56067179/105951445-5d8f0a80-60b3-11eb-856b-0cb60f67e053.PNG" width="600px" />

  - `CHOOSE ON`을 눌러 원하는 Raspberry Pi OS 선택
  - `CHOOSE SD CARD` 를 눌러 SD카드 선택 후 `WRITE` 클릭
  - 본 팀은 Raspberry Pi OS Debian 사용

    <img src="https://user-images.githubusercontent.com/56067179/105951429-59fb8380-60b3-11eb-96a5-1b7951dcdfe1.PNG" width="400px" />

    <img src="https://user-images.githubusercontent.com/56067179/105951433-5b2cb080-60b3-11eb-8cc9-e841682b46f4.PNG" width="400px" />

  

- **WiFi 설정**

  - [Menu] > [Preferences] > [Raspberry Pi Configuration] > [Localisation]의 Local과 WiFi Country를 US 로 설정

- **카메라 활성화**

  - CMD > `Interfacing Options` > `Camera` > `Yes` > `Finish`

    ```
    $ sudo raspi-config
    ```

    <img src="https://user-images.githubusercontent.com/56067179/105951439-5c5ddd80-60b3-11eb-9fad-caa1d8ce46d8.PNG" width="400" />

  또는

  - [Menu] > [Preferences] > [Raspberry Pi Configuration] > [Interfaces]

    <img src="https://user-images.githubusercontent.com/56067179/105951443-5cf67400-60b3-11eb-9b38-8d64b64b1e9a.PNG" width="400" />

- **웹 카메라 연결**

  ```
  $ lsusb
  ```

  <img src="https://user-images.githubusercontent.com/56067179/105959466-42c29300-60bf-11eb-8ecc-7a1ae3c85a91.PNG" width="500" />



## Setup-UV4L

- **UV4L 설치**

  - V4L2 인증키 설치

    ```
    $ curl http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc | sudo apt-key add –
    ```

  - /etc/apt/sources.list 파일에 아래 명령 추가 ( V4L2 관련 리소스 리스트 추가)

    ```
    deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/strectch strectch main
    ```

    ```
    $ sudo apt-get update
    ```

  - UV4L 패키지 설치

    ```
    $ sudo apt-get install uv4l uv4l-raspicam 
    $ sudo apt-get install uv4l-raspicam-extras  // 부팅 시 자동 로드
    ```

  - 스트리밍 기능을 사용하기 위한 확장 패키지 설치

    ```
    $ sudo apt-get install uv4l-server uv4l-uvc uv4l-xscreen uv4l-mjpegstream uv4ldummy
    ```

- **UV4L 실행**

  ```
  $ sudo service uv4l_raspicam restart
  ```

  ```
  $ sudo reboot  // 작동이 안된다면 재부팅
  ```

- **원하는 환경에 맞게 conf 파일 수정**

  ```
  $ sudo nano /etc/uv4l/uv4l-raspicam.conf
  ```

- **UV4L 설치 확인**

  - 라즈베리파이 카메라: `라즈베리파이ip:8080/stream`
  - 웹 카메라: `라즈베리파이ip:8090/stream`

    <img src="https://user-images.githubusercontent.com/56067179/105951435-5b2cb080-60b3-11eb-90dd-ec7ebe30129c.PNG" width="500" />

  

> **참고**

- http://www.linux-projects.org/uv4l/installation/



## Setup-MQTT Broker

- **Mosquitto 설치**

  -  Mosquitto 프로그램의 서명키(인증키) 다운로드 및 설치 후 키 지우기
  
      ```
      $ wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key 
      $ sudo apt-key add mosquitto-repo.gpg.key 
      $ rm. mosquitto-repo.gpg.key
      ```

  - Mosquitto의 저장소 패키지 등록

    ```
    $ cd /etc/apt/source.list.d/ 
    $ sudo wget http://repo.mosquitto.org/debian/mosquitto-stretch.list
    ```

  - 라즈베리파이 업데이트 및 Mosquitto 관련 라이브러리 설치

    ```
    $ sudo apt-get update 
    $ sudo apt-get install mosquitto 
    $ sudo apt-get install mosquitto-clients 
    $ pip install paho-mqtt
    ```

- **Mosquitto 활성화 확인**

  ```
  $ sudo /etc/init.d/mosquitto status
  ```

  <img src="https://user-images.githubusercontent.com/56067179/105957766-0aba5080-60bd-11eb-8a87-2f1d98ebd3f2.PNG" width="500" />

  또는

  ```
  $ sudo systemctl status mosquitto
  ```

  <img src="https://user-images.githubusercontent.com/56067179/105957772-0beb7d80-60bd-11eb-8bbd-c2028571857e.PNG" width="500" />



## Setup-Bluetooth

- **Bluetooth 설치**

  - 라즈베리파이 업데이트

    ```
    $ sudo apt-get update 
    $ sudo apt-get upgrade
    ```

  - Bluetooth 패키지 설치 후 재부팅

    ```
    $ sudo apt-get install bluetooth blueman bluez 
    $ sudo apt-get install python-bluetooth 
    $ sudo reboot
    ```

- **Bluetooth 환경 설정**

  ```
  $ sudo bluetoothctl
  ```

  - 연결 가능한 장치 찾기

    ```
    $ scan on
    ```

  - 페어링

    ```
    $ pair 00:21:13:02:E6:AC  // 블루투스 칩의 맥 주소 
    $ 1234                    // 핀 코드
    ```

    <img src="https://user-images.githubusercontent.com/56067179/105951437-5bc54700-60b3-11eb-9d9e-4d737c902dc0.PNG" width="500" />
