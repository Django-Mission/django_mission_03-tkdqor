# :pushpin: Basic 과제
- **Basic 디렉터리 - first-django 디렉터리 내부 Support App에 Basic 과제 수행**


- **고객센터(support) 앱의 Faq 모델 관련 이미지**
<img width="973" alt="image" src="https://user-images.githubusercontent.com/95380638/166413303-47ef01f8-dd74-453c-9ed2-4f05bb4fe4c8.png">

<img width="463" alt="image" src="https://user-images.githubusercontent.com/95380638/166413432-37aca10a-8503-458a-9e2f-b03647e57585.png">

<img width="1415" alt="image" src="https://user-images.githubusercontent.com/95380638/166413487-d9ba1a9a-a20d-4524-a665-bad678404af5.png">

* * *

- **고객센터(support) 앱의 Inquiry 모델 관련 이미지**
<img width="992" alt="image" src="https://user-images.githubusercontent.com/95380638/166413834-6f0a4580-18bc-4e5b-86e4-f620cc410c36.png">

<img width="514" alt="image" src="https://user-images.githubusercontent.com/95380638/166413877-1a224612-6664-4927-a55d-af9b3a779e24.png">

<img width="1416" alt="image" src="https://user-images.githubusercontent.com/95380638/166413905-bb1e7a3e-f3ec-4179-a725-39514cd6e6c8.png">

* * *
- **고객센터(support) 앱의 Answer 모델 관련 이미지**
  - Answer 모델의 경우, 어드민 페이지에서 Inquiry 모델에 인라인 모델로 추가 

<img width="750" alt="image" src="https://user-images.githubusercontent.com/95380638/166414024-0a0a3708-6917-4678-972c-eb6c8ae30a10.png">

<img width="631" alt="image" src="https://user-images.githubusercontent.com/95380638/166414094-b4092f80-e433-4ec5-a92f-4b5b0b9037c3.png">

<img width="1422" alt="image" src="https://user-images.githubusercontent.com/95380638/166414174-3e2e891f-1956-4758-b5b8-b07d33da98c1.png">

* * *

# :pushpin: Challenge 과제
- Challenge 디렉터리 - first-django 디렉터리 내부 Support App과 Users App에 Challenge 과제 수행


- **고객센터(support) 앱의 Inquiry 모델 관련 이미지**
<img width="989" alt="image" src="https://user-images.githubusercontent.com/95380638/166414561-bf3de14a-360e-44ca-9895-61547b6bae97.png">

<img width="1016" alt="image" src="https://user-images.githubusercontent.com/95380638/166414774-5f2724d6-ed16-4d72-97fa-6056da07c84d.png">

<img width="1424" alt="image" src="https://user-images.githubusercontent.com/95380638/166414855-9e5d2a1f-a79d-4b6a-b67a-9851a7aeee63.png">

* * *

## :pushpin: 오류 해결 사항
- 사용자 모델 User에 phone 필드를 추가하기 위해, support App 내부 models.py에서 User 모델을 커스텀하기 위해 AbstractUser 클래스를 상속받아 코드를 입력했으나,
```terminal
ValueError: Related model 'support.user' cannot be resolved
```
- 다음과 같은 에러가 migrate 과정에서 발생
  - **그래서 python manage.py migrate support zero 명령어로 초기화한 다음, users라는 App을 생성하고 내부 models.py에 AbstractUser 클래스를 상속받아 User 모델에 phone 필드 추가**

<img width="849" alt="image" src="https://user-images.githubusercontent.com/95380638/166415505-160c44d3-d129-4816-8ffc-ebd086cfc2ee.png">

<img width="560" alt="image" src="https://user-images.githubusercontent.com/95380638/166415527-e5b7029a-a311-4707-abc7-9bd803fe4cbb.png">

<img width="1403" alt="image" src="https://user-images.githubusercontent.com/95380638/166415561-078fdb40-0d69-434d-b6b9-49d4b608abe2.png">



