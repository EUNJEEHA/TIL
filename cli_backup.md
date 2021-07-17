# 생활코딩 GIT3 - CLI 백업

## 1. 간단 설명

* Local Repository1 -- `push` --> Remote Repository : 백업
* Remote Repository -- `clone` --> Local Repository2 : 복제
* Local Repository2 -- `push` --> Remote Repository : 백업
* Remote Repository -- `pull` --> Local Repository1 : 백업물 가져오기



## 2. Git hosting

* `Github`와 `Gitlab`
  * `github` : open-source 무료 / 용량 무제한 / 미공개 저장소 유료
  * `gitlab` :  open-source 무료 / 용량 무제한 / 미공개 저장소 무료, 무제한



## 3. Local -- `push` --> Remote

```
1. git remote add origin https://github.com/EUNJEEHA/second-backup.git
: 자신의 원격저장소 주소를 입력

2. git remote : 원격저장소의 정보를 보여줌

3. git push --set-upstream origin master : 기본 원격저장소 설정

4. 자신의 github 메일주소와 비밀번호로 인증

5. push된 파일 확인
```



## 4. Remote -- `clone` --> Local

```
git clone https://github.com/EUNJEEHA/second-backup.git : 복제할 저장소의 주소 입력

현재 명령을 실행시킨 디렉토리에 저장소의 디렉토리가 생성됨
```



## 5. Remote -- `pull` --> Local

```
git pull 
```



## 6. git과 오픈소스

#### open_source활용 방법

```
git clone [오픈소스 주소] : 복제를 사용하여 오픈소스 활용
```



## 7. 그 다음 공부 내용

* 원격저장소와 통신할 때마다 인증해야하는 문제 : SSH를 이용하여 자동 로그인 가능

* Issue tracker : 프로젝트를 진행하면서 생기는 이슈들을 공유하는 게시판. 

  문제 기록과 처리, 그리고 협업 기능과 함께 업무 분담 가능

* 협업 기능 : 충돌(conflict) 방지 방법 배우기







