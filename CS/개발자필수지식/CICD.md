## CI / CD

CI/CD(Continuous Integration / Delivery & Deployment)는 지속적으로 코드를 합치고 배포하는 것을 말한다. CI/CD는 혼자가 아닌 수많은 개발자가 코드를 합치고 배포를 시스템없이 한다면 특정 환경에서만 되거나 잘못된 코드를 배포할 수 있는 문제가 발생하게 된다. 이를 해결하기위해 CI/CD라는 개념이 도입됨

### 파이프라인

코드구축부터 배포까지의 일련의 과정들을 CI/CD 파이프라인이라고 하고 총 3단계로 구성됨
![image](https://github.com/pjaehyun/TIL/assets/56579736/ff370b2c-7210-40a5-bad6-8a0a8d55b4c4)

1. Continuous Integration: 코드를 빌드하고 테스트하고 합친다.
2. Continuous Delivery: 해당 레포지토리에 릴리즈한다.
3. Continuous Deployment: 실제 서비스에 배포한다.
