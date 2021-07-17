# 생활코딩 GIT - CLI협업

## 1. Git == 협업의 도구

* Branch의 개념 필수





## 2. A와 B가 협업

### 2-1. A가 먼저 작업을 한다.

	##### 1. A가 work.txt 파일을 만들고 '1'이라고 문서 작성

##### 2. work.txt 파일을 `add` -> `commit`

##### 3. Github 활용 시작

##### 4. 원격 저장소 생성 -> 원격 저장소와 연결

```
git remote add origin [저장소 주소]
```

###### 	origin : 저장소 별명  __->이걸 까먹었다면? 다시 알아내는 방법은 뭘까?__

##### 5. `push`하여 저장소에 파일 백업

```
git push origin master
```





### 2-2.  동료 B가 합류한다.

##### 1. 권한 설정

###### 	`Settings` -> `Collaborators & teams` -> 동료 B의 github ID 추가 -> e-mail 인증 -> 협업 시작

`permission level` 설정 : Admin / Write / Read

##### 2. 동료B의 환경 세팅

```
git clone [협업 원격 저장소 주소]
```

######	`clone`은 맨 처음에 저장소를 가져올 때만 사용. 그 이후에는 `pull`.





### 2-3. 협업 시작

##### 1. 같은 시간에 같은 파일의 같은 부분을 수정하는 __conflict(충돌)__이 발생한다면?

##### 	`git push`를 거절당한다면, 다시 `git pull`을 하여 충돌이 생기지 않도록 다시 정리해야한다.

##### 2. `git merge`를 하거나 파일을 열어 엉킨 부분을 수정해야 한다.

##### 3. 고쳐진 파일을 다시 `git add` -> `git commit`을 한다.

##### 4. 다시 `git push`한다.

##### __5. 결론 : 최대한 작업을 빨리 끝내고, `push`를 자주 해야 서로 충돌이 일어나지 않는다. 작업을 하기 전에 무조건 먼저 `git pull`을 해야한다.__





## 3. pull 방법 : git fetch -> git merge FETCH_HEAD

* 기존 방법 : `git pull` -> `git commit` -> `git push`

* 새로운 방법 : `git fetch` -> `git merge FETCH_HEAD` -> `git commit` -> `git push`

  ​	git fetch : 원격저장소 업데이트 (remote branch를 가저옴) -> __뭔말인지 모르겠음..branch더공부필요..__

  ​	git merge FETCH_HEAD : 최신 원격저장소의 파일과 머지함 (원격 브렌치와 지역 브렌치를 머지)

* 신중하게 `pull`하고자 할 때 사용하자.





## 4. 다음 공부 내용

* code review - Gerrit : 프로젝트용으로 만들어진 개발자들의 코드 품질을 상호 검증하는 도구(일종의 투표소)

  ​	`push`를 하면 바로 원격 저장소로 올라가는 것이 아니라, 투표소로 감.

  ​	동료들은 투표를 하고 코멘트를 달며 투표 결과에 따라 반영, 거절, 유보가 자동화 됨

* Issue Tracker : 게시판 기능을 사용하여 체계적으로 업무 분담, 진행 가능

* Insight : 업무가 얼마나 활발하게 이뤄지고 있는지 한 눈에 파악 가능





