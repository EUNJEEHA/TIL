# 생활코딩 Git - CLI branch & conflict

## 1. 간단한 개념

### 1-1. branch

> 가지
>
> 같은 뿌리에서 나왔지만 서로 다른 역사를 쓰고 있는 버전들

### 1-2. conflict

> branch를 만들 때 필연적으로 극복해야 하는 고개
>
> 하나의 파일에서 같은 부분을 각각 다르게 수정한 후, 병합 시키면 충돌이 생김



## 2. branch 3개를 만들어 보자

### 2-1. 'manual'폴더에 'work'파일을 생성하고 `commit`

```shell
USER@CT128 MINGW64 ~
$ mkdir manual
: 'manual'이라는 폴더 생성

USER@CT128 MINGW64 ~
$ cd manual
: 'manual'폴더 안으로 들어가기

USER@CT128 MINGW64 ~/manual
$ ls

USER@CT128 MINGW64 ~/manual
$ git init
Initialized empty Git repository in C:/Users/USER/manual/.git/
: git 초기화

USER@CT128 MINGW64 ~/manual (master)
$ ls -al
total 24
drwxr-xr-x 1 USER 197121 0 Jul 18 14:56 ./
drwxr-xr-x 1 USER 197121 0 Jul 18 14:56 ../
drwxr-xr-x 1 USER 197121 0 Jul 18 14:56 .git/
: 전체 list를 열어 '.git'파일 확인

USER@CT128 MINGW64 ~/manual (master)
$ nano work.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 처음 시도해본 것인데, 'git bash'에서 바로 파일에 텍스트를 작성했다. 
확인해보니 잘 작성 되어있는데, 왜 'error'라고 뜨는지는 잘 모르겠다.
-> 'nano'가 아니라 'vim'을 써야함!!(3번 부터 수정함)

USER@CT128 MINGW64 ~/manual (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        work.txt

nothing added to commit but untracked files present (use "git add" to track)
: git 상태 확인. 'untracked'상태.

USER@CT128 MINGW64 ~/manual (master)
$ git add work.txt
warning: LF will be replaced by CRLF in work.txt.
The file will have its original line endings in your working directory
: 'git add' 실행

USER@CT128 MINGW64 ~/manual (master)
$ git commit -m "work 1"
[master (root-commit) 6e2d21d] work 1
 1 file changed, 1 insertion(+)
 create mode 100644 work.txt
: 'commit' 실행

USER@CT128 MINGW64 ~/manual (master)
$ git log
commit 6e2d21d25bc92939cfacbe582bce4b0aeb054e34 (HEAD -> master)
Author: Eunji Ha <haej94@gmail.com>
Date:   Sun Jul 18 14:58:58 2021 +0900

    work 1
: 'git log'로 'commit'상태 확인
```

### 2-2. 같은 방식으로 'work 3'까지 `commit`하기

```shell
USER@CT128 MINGW64 ~/manual (master)
$ nano work.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 파일에 "content 2" 라인 추가

USER@CT128 MINGW64 ~/manual (master)
$ git commit -am "work 2"
warning: LF will be replaced by CRLF in work.txt.
The file will have its original line endings in your working directory
[master bcd604b] work 2
 1 file changed, 1 insertion(+)
: 'work 2'로 'commit'

USER@CT128 MINGW64 ~/manual (master)
$ nano work.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 파일에 "content 2" 라인 추가

USER@CT128 MINGW64 ~/manual (master)
$ git commit -am "work 3"
warning: LF will be replaced by CRLF in work.txt.
The file will have its original line endings in your working directory
[master f9e11f0] work 3
 1 file changed, 1 insertion(+)
: 'work 2'로 'commit'
```

### 2-3. 고객사마다 다른 사용 설명서를 제공 : `git branch`

```shell
USER@CT128 MINGW64 ~/manual (master)
$ git branch
* master
: git의 모든 branch를 보여줌

USER@CT128 MINGW64 ~/manual (master)
$ git branch apple
: 'apple'브렌치 추가

USER@CT128 MINGW64 ~/manual (master)
$ git branch
  apple
* master
: 브런치는 master, apple로 총 2개. 현재는 master브렌치에 있다.

USER@CT128 MINGW64 ~/manual (master)
$ git log --all --graph --oneline
* f9e11f0 (HEAD -> master, apple) work 3
* bcd604b work 2
* 6e2d21d work 1
: git의 log 전체를 그래프와 한 줄로 표현하여 보여줌
master, apple브렌치가 있고, HEAD는 master를 가리키고 있다.
master에 HEAD가 있는 상태로 apple브렌치를 만들었기 때문에
apple브렌치도 work 3상태이다.

USER@CT128 MINGW64 ~/manual (master)
$ git branch google

USER@CT128 MINGW64 ~/manual (master)
$ git branch ms
: 'google'과 'ms'브렌치도 추가한다.

USER@CT128 MINGW64 ~/manual (master)
$ git log --all --graph --oneline
* f9e11f0 (HEAD -> master, ms, google, apple) work 3
* bcd604b work 2
* 6e2d21d work 1
master, ms google, apple 총 4개의 브런치가 있고
HEAD는 master를 가리키고 있으므로 나머지 3개의 브런치도 work 3 상태이다.
```

### 2-4. 각 branch로 이동하기 : `git checkout`

```shell
USER@CT128 MINGW64 ~/manual (master)
$ nano work.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 'work.txt'파일에 "master content 4"라는 라인 추가

USER@CT128 MINGW64 ~/manual (master)
$ git commit -am "master work 4"
warning: LF will be replaced by CRLF in work.txt.
The file will have its original line endings in your working directory
[master e11715b] master work 4
 1 file changed, 1 insertion(+)
: 수정된 내용 'commit'

USER@CT128 MINGW64 ~/manual (master)
$ git log --all --graph --oneline
* e11715b (HEAD -> master) master work 4
* f9e11f0 (ms, google, apple) work 3
* bcd604b work 2
* 6e2d21d work 1
: master는 'work 4'이고, 나머지 ms, google, apple 브렌치는 'work3'

USER@CT128 MINGW64 ~/manual (master)
$ git checkout apple
Switched to branch 'apple'
: apple 브렌치로 이동

USER@CT128 MINGW64 ~/manual (apple)
$ git log --all --graph --oneline
* e11715b (master) master work 4
* f9e11f0 (HEAD -> apple, ms, google) work 3
* bcd604b work 2
* 6e2d21d work 1
: 현재 apple브렌치로 HEAD가 이동하여 work 3상태임
```

### 2-5. 새로운 버전의 apple브렌치 생성

```shell
__<현재 apple 브렌치 work 3 상태>__

USER@CT128 MINGW64 ~/manual (apple)
$ nano work.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 'work.txt'파일에 "apple work 4" 라인 추가

USER@CT128 MINGW64 ~/manual (apple)
$ touch apple.txt
: 'apple.txt'파일 생성

USER@CT128 MINGW64 ~/manual (apple)
$ nano apple.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 'apple.txt'파일에 "apple work 4"라인 추가

USER@CT128 MINGW64 ~/manual (apple)
$ git add .
warning: LF will be replaced by CRLF in apple.txt.
The file will have its original line endings in your working directory
: 모든 파일 'git add'

USER@CT128 MINGW64 ~/manual (apple)
$ git status
On branch apple
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   apple.txt
        modified:   work.txt
: git 상태 확인

USER@CT128 MINGW64 ~/manual (apple)
$ git commit -m "apple work 4"
[apple 9eef7e4] apple work 4
 2 files changed, 2 insertions(+)
 create mode 100644 apple.txt
: 'git commit'

USER@CT128 MINGW64 ~/manual (apple)
$ git log --all --graph --oneline
* 9eef7e4 (HEAD -> apple) apple work 4
| * e11715b (master) master work 4
|/
* f9e11f0 (ms, google) work 3
* bcd604b work 2
* 6e2d21d work 1
: 현재 apple에 있는 상태이며 apple work 4 버전
apple work 4의 부모는 work 3
master work 4의 부모도 work 3
```

### 2-6. 새로운 버전의 google과 ms 브렌치 생성

```shell
USER@CT128 MINGW64 ~/manual (apple)
$ git checkout google
Switched to branch 'google'
: google 브렌치로 이동

USER@CT128 MINGW64 ~/manual (google)
$ nano work.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 'work.txt'파일에 "google work 4"라인 추가

USER@CT128 MINGW64 ~/manual (google)
$ touch google.txt
: 'google.txt'파일 생성

USER@CT128 MINGW64 ~/manual (google)
$ nano google.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 'google.txt'파일에 "google work 4"라인 추가

USER@CT128 MINGW64 ~/manual (google)
$ git add .
warning: LF will be replaced by CRLF in google.txt.
The file will have its original line endings in your working directory
: git 아래 모든 파일 'add'

USER@CT128 MINGW64 ~/manual (google)
$ git commit -m "google work 4"
[google 59badb3] google work 4
 2 files changed, 2 insertions(+)
 create mode 100644 google.txt
: 'git commit'

USER@CT128 MINGW64 ~/manual (google)
$ git log --all --graph --oneline
* 59badb3 (HEAD -> google) google work 4
| * 9eef7e4 (apple) apple work 4
|/
| * e11715b (master) master work 4
|/
* f9e11f0 (ms) work 3
* bcd604b work 2
* 6e2d21d work 1
: 현재 google브렌치에 위치하고 있고, google work 4 버전이다.
google work 4의 부모는 work 3이다.

USER@CT128 MINGW64 ~/manual (google)
$ git checkout ms
Switched to branch 'ms'
: ms 브렌치로 이동

USER@CT128 MINGW64 ~/manual (ms)
$ nano work.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 'work.txt'파일에 "ms work 4"라인 추가

USER@CT128 MINGW64 ~/manual (ms)
$ touch ms.txt
: 'ms.txt'파일 생성

USER@CT128 MINGW64 ~/manual (ms)
$ nano ms.txt
Error in /etc/nanorc on line 237: Error expanding /usr/share/nano/*.nanorc: No such file or directory
: 'ms.txt'파일에 "ms work 4"라인 추가

USER@CT128 MINGW64 ~/manual (ms)
$ git add .
warning: LF will be replaced by CRLF in ms.txt.
The file will have its original line endings in your working directory
: git 아래 모든 파일 'add'

USER@CT128 MINGW64 ~/manual (ms)
$ git commit -m "ms work 4"
[ms bf7abc9] ms work 4
 2 files changed, 2 insertions(+)
 create mode 100644 ms.txt
: 'git commit'

USER@CT128 MINGW64 ~/manual (ms)
$ git log --all --graph --oneline
* bf7abc9 (HEAD -> ms) ms work 4
| * 59badb3 (google) google work 4
|/
| * 9eef7e4 (apple) apple work 4
|/
| * e11715b (master) master work 4
|/
* f9e11f0 work 3
* bcd604b work 2
* 6e2d21d work 1
: 현재 ms 브렌치에 위치하고 있고, ms work 4 버전이다.
ms work 4의 부모는 work 3이다.
```



## 3. 병합 : merge

### 3-1. master branch 생성

```shell
USER@CT128 MINGW64 ~/manual (ms)
$ cd ~
: home으로 돌아오기

USER@CT128 MINGW64 ~
$ ls
'3D Objects'/
 AppData/
'Application Data'@
 Contacts/
 Cookies@
 Desktop/
 Documents/
 Downloads/
 Favorites/
 IntelGraphicsProfiles/
 Jedi/
 Links/
'Local Settings'@
 Music/
'My Documents'@
 NTUSER.DAT
 NTUSER.DAT{fd9a35db-49fe-11e9-aa2c-248a07783950}.TM.blf
 NTUSER.DAT{fd9a35db-49fe-11e9-aa2c-248a07783950}.TMContainer00000000000000000001.regtrans-ms
 NTUSER.DAT{fd9a35db-49fe-11e9-aa2c-248a07783950}.TMContainer00000000000000000002.regtrans-ms
 NetHood@
 OneDrive/
 Pictures/
 PrintHood@
 PycharmProjects/
 Recent@
'Saved Games'/
 Searches/
 SendTo@
 Templates@
 Videos/
 campus/
 git-test/
 house/
 manual/
 ntuser.dat.LOG1
 ntuser.dat.LOG2
 ntuser.ini
 push-practice/
 recap/
 test.ipynb
 test.py
 test.txt
 til/
'시작 메뉴'@
: list 확인

USER@CT128 MINGW64 ~
$ git init manual-merge
Initialized empty Git repository in C:/Users/USER/manual-merge/.git/
: 'manual-merge'폴더 git 초기화

USER@CT128 MINGW64 ~
$ cd manual-merge
: 'manual-merge'폴더로 이동

USER@CT128 MINGW64 ~/manual-merge (master)
$ touch work.txt
: 'work.txt'파일 생성

USER@CT128 MINGW64 ~/manual-merge (master)
$ vim work.txt
: 'work.txt'파일에 "1"라인 추가

USER@CT128 MINGW64 ~/manual-merge (master)
$ cat work.txt
1
: 'work.txt' 내용 확인

USER@CT128 MINGW64 ~/manual-merge (master)
$ git add work.txt
warning: LF will be replaced by CRLF in work.txt.
The file will have its original line endings in your working directory
: 'git add'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git commit -m "work 1"
[master (root-commit) 3d9f4ff] work 1
 1 file changed, 1 insertion(+)
 create mode 100644 work.txt
: 'git commit'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git log
commit 3d9f4ffdd057920d8590da38d51dd70b12663541 (HEAD -> master)
Author: Eunji Ha <haej94@gmail.com>
Date:   Sun Jul 18 17:09:54 2021 +0900

    work 1
: log 확인
```

### 3-2. o2 branch 생성

```shell
USER@CT128 MINGW64 ~/manual-merge (master)
$ git branch o2
: 'o2'브렌치 생성

USER@CT128 MINGW64 ~/manual-merge (master)
$ vim master.txt
: 'master.txt'파일 생성 후 "1"라인 추가

USER@CT128 MINGW64 ~/manual-merge (master)
$ git add master.txt
warning: LF will be replaced by CRLF in master.txt.
The file will have its original line endings in your working directory
: 'git add'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git commit -m "work 2"
[master 3edfd67] work 2
 1 file changed, 1 insertion(+)
 create mode 100644 master.txt
: 'git commit'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git checkout o2
Switched to branch 'o2'
: 'o2'브렌치 생성

USER@CT128 MINGW64 ~/manual-merge (o2)
$ vim o2.txt
: 'o2.txt'파일 생성하고 "o2 2"라인 입력

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git add o2.txt
warning: LF will be replaced by CRLF in o2.txt.
The file will have its original line endings in your working directory
: 'git add'

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git commit -m "o2 work 2"
[o2 cee9fd8] o2 work 2
 1 file changed, 1 insertion(+)
 create mode 100644 o2.txt
: 'git commit'

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git log --all --graph --oneline
* cee9fd8 (HEAD -> o2) o2 work 2
| * 92ef832 (master) work 2
|/
* 3d9f4ff work 1
: master와 o2 각각 존재
```

### 3-3. master + o2 : merge

```shell
master에 o2 병합 -> master 브렌치로 이동 필수

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git checkout master
Switched to branch 'master'
: 'master'브렌치로 이동

USER@CT128 MINGW64 ~/manual-merge (master)
$ git merge o2
Merge made by the 'recursive' strategy.
 o2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 o2.txt
: 현재 상태인 'master'브렌치에 'o2'병합

USER@CT128 MINGW64 ~/manual-merge (master)
$ git log --all --graph --oneline
*   a5d2f22 (HEAD -> master) Merge branch 'o2'
|\
| * cee9fd8 (o2) o2 work 2
* | 92ef832 work 2
|/
* 3d9f4ff work 1
: 완성!!!!!!
```

### 

## 4. 같은 파일 내 병합

### 4-1. 같은 파일, 다른 부분 병합

```shell
USER@CT128 MINGW64 ~/til (master)
$ cd ~
: home으로 이동

USER@CT128 MINGW64 ~
$ git init manual-merge
Initialized empty Git repository in C:/Users/USER/manual-merge/.git/
: 'manual-merge'폴더 생성 후 초기화

USER@CT128 MINGW64 ~
$ cd manual-merge
: 'manual-merge'폴더로 이동

USER@CT128 MINGW64 ~/manual-merge (master)
$ vim work.txt
: 'work.txt'파일 생성
	title
	content
	
	title
	content 글 추가
	
USER@CT128 MINGW64 ~/manual-merge (master)
$ git add work.txt
warning: LF will be replaced by CRLF in work.txt.
The file will have its original line endings in your working directory
: 'git add'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git commit -m "1"
[master (root-commit) 21cddf1] 1
 1 file changed, 6 insertions(+)
 create mode 100644 work.txt
: 'git commit'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git log
commit 21cddf1d5793fc6c7b0f6fdc2939c30f784eac4e (HEAD -> master)
Author: Eunji Ha <haej94@gmail.com>
Date:   Sun Jul 18 21:38:12 2021 +0900

    1
: 'git log'

USER@CT128 MINGW64 ~/manual-merge (master)
$ vim work.txt
: 현재 master상태. 'work.txt'파일을 변경
	title
	master content
	
	title
	content

USER@CT128 MINGW64 ~/manual-merge (master)
$ git branch o2
: 'o2' 브렌치 생성

USER@CT128 MINGW64 ~/manual-merge (master)
$ git commit -am "master work 2"
warning: LF will be replaced by CRLF in work.txt.
The file will have its original line endings in your working directory
[master bf3113d] master work 2
 1 file changed, 1 insertion(+), 1 deletion(-)
: 'git add & commit'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git checkout o2
Switched to branch 'o2'
: o2 브렌치로 이동

USER@CT128 MINGW64 ~/manual-merge (o2)
$ vim work.txt
: 현재 o2 브렌치 상태. 'work.txt'파일을 변경
	title
	content
	
	title
	o2 content
	
USER@CT128 MINGW64 ~/manual-merge (o2)
$ git add work.txt
: 'git add'

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git commit -m "o2 work 2"
[o2 ea66d1d] o2 work 2
 1 file changed, 1 insertion(+), 1 deletion(-)
: 'git commit'

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git log --all --graph --oneline
* ea66d1d (HEAD -> o2) o2 work 2
| * bf3113d (master) master work 2
|/
* 21cddf1 1
: 브렌치 그래프 완성

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git checkout master
Switched to branch 'master'
: 'master'브렌치로 이동 (master에 o2를 병합)

USER@CT128 MINGW64 ~/manual-merge (master)
$ git merge o2
Auto-merging work.txt
Merge made by the 'recursive' strategy.
 work.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
: master에 o2를 merge

USER@CT128 MINGW64 ~/manual-merge (master)
$ git log --all --graph --oneline
*   220dd03 (HEAD -> master) Merge branch 'o2'
|\
| * ea66d1d (o2) o2 work 2
* | bf3113d master work 2
|/
* 21cddf1 1
: 그래프 참고

USER@CT128 MINGW64 ~/manual-merge (master)
$ cat work.txt
# title
master content


# title
o2 content
: 같은 파일의 서로 다른 부분을 수정한 후 merge하면
두 부분이 다 반영이 되어 합쳐진다.
```

### 4-2. 같은 파일, 같은 부분 병합

> 같은 파일의 같은 부분을 서로 다른 브렌치에서 수정한 후 merge시키면,
>
> git은 자동으로 병합하지 못한다. 이를 'conflic(충돌)'이라고 한다.

```shell
USER@CT128 MINGW64 ~/manual-merge
$ cd ~
: home으로 이동

USER@CT128 MINGW64 ~
$ ls
'3D Objects'/
 AppData/
'Application Data'@
 Contacts/
 Cookies@
 Desktop/
 Documents/
 Downloads/
 Favorites/
 IntelGraphicsProfiles/
 Jedi/
 Links/
'Local Settings'@
 Music/
'My Documents'@
 NTUSER.DAT
 NTUSER.DAT{fd9a35db-49fe-11e9-aa2c-248a07783950}.TM.blf
 NTUSER.DAT{fd9a35db-49fe-11e9-aa2c-248a07783950}.TMContainer00000000000000000001.regtrans-ms
 NTUSER.DAT{fd9a35db-49fe-11e9-aa2c-248a07783950}.TMContainer00000000000000000002.regtrans-ms
 NetHood@
 OneDrive/
 Pictures/
 PrintHood@
 PycharmProjects/
 Recent@
'Saved Games'/
 Searches/
 SendTo@
 Templates@
 Videos/
 campus/
 git-test/
 house/
 manual/
 ntuser.dat.LOG1
 ntuser.dat.LOG2
 ntuser.ini
 push-practice/
 recap/
 test.ipynb
 test.py
 test.txt
 til/
'시작 메뉴'@
: home의 모든 파일 확인

USER@CT128 MINGW64 ~
$ git init manual-merge
Initialized empty Git repository in C:/Users/USER/manual-merge/.git/
: 'manual-merge'폴더 생성 및 초기화

USER@CT128 MINGW64 ~
$ cd manual-merge
: 'manual-merge'파일로 이동

USER@CT128 MINGW64 ~/manual-merge (master)
$ vim work.txt
: 'work.txt'파일 생성 후 텍스트 추가
	#Title
	content
	
	#Title
	content
	
USER@CT128 MINGW64 ~/manual-merge (master)
$ git add work.txt
warning: LF will be replaced by CRLF in work.txt.
The file will have its original line endings in your working directory
: 'git add'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git commit -m "work 1"
[master (root-commit) 9923fa6] work 1
 1 file changed, 5 insertions(+)
 create mode 100644 work.txt
: 'git commit'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git branch o2
: 'o2'브렌치 생성

USER@CT128 MINGW64 ~/manual-merge (master)
$ git log --all --graph --oneline
* 9923fa6 (HEAD -> master, o2) work 1
: 브렌치 확인

USER@CT128 MINGW64 ~/manual-merge (master)
$ vim work.txt
: master상태에서 'work.txt'파일의 텍스트 수정
	#Title
	content
	master
	#Title
	content
	
USER@CT128 MINGW64 ~/manual-merge (master)
$ git commit -am "master work 2"
warning: LF will be replaced by CRLF in work.txt.
The file will have its original line endings in your working directory
[master a114127] master work 2
 1 file changed, 1 insertion(+), 1 deletion(-)
: 'git add & commit'

USER@CT128 MINGW64 ~/manual-merge (master)
$ git checkout o2
Switched to branch 'o2'
: 'o2'브렌치로 이동

USER@CT128 MINGW64 ~/manual-merge (o2)
$ vim work.txt
: o2상태에서 'work.txt'파일의 텍스트 수정
	#Title
	content
	o2
	#Title
	content
	
USER@CT128 MINGW64 ~/manual-merge (o2)
$ git add work.txt
: 'git add'

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git commit -m "o2 work 2"
[o2 bff1bd6] o2 work 2
 1 file changed, 1 insertion(+), 1 deletion(-)
: 'git commit'

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git log --all --graph --oneline
* bff1bd6 (HEAD -> o2) o2 work 2
| * a114127 (master) master work 2
|/
* 9923fa6 work 1
: master와 o2 브렌치 확인

USER@CT128 MINGW64 ~/manual-merge (o2)
$ git checkout master
Switched to branch 'master'
: master브렌치로 이동

USER@CT128 MINGW64 ~/manual-merge (master)
$ git merge o2
Auto-merging work.txt
CONFLICT (content): Merge conflict in work.txt
Automatic merge failed; fix conflicts and then commit the result.
: 'master'에 'o2'를 merge

USER@CT128 MINGW64 ~/manual-merge (master|MERGING)
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   work.txt

no changes added to commit (use "git add" and/or "git commit -a")
: conflict 발생

USER@CT128 MINGW64 ~/manual-merge (master|MERGING)
$ vim work.txt
: 충돌한 부분 수정
	#Title
	content
	master, o2
	#Title
	content
	
USER@CT128 MINGW64 ~/manual-merge (master|MERGING)
$ git add work.txt
: 수정한 충돌 부분 'git add'

USER@CT128 MINGW64 ~/manual-merge (master|MERGING)
$ git status
On branch master
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   work.txt
: 계속해서 merge하려면 'git commit'실행

USER@CT128 MINGW64 ~/manual-merge (master|MERGING)
$ git commit
[master a962728] Merge branch 'o2'
: 'git commit'실행하여 master에 o2 merge 성공

USER@CT128 MINGW64 ~/manual-merge (master)
$ git log --all --graph --oneline
*   a962728 (HEAD -> master) Merge branch 'o2'
|\
| * bff1bd6 (o2) o2 work 2
* | a114127 master work 2
|/
* 9923fa6 work 1
: merge된 새로운 브렌치 탄생

USER@CT128 MINGW64 ~/manual-merge (master)
$ vim work.txt
: 수정된 work.txt 내용 확인
```

## 5. CONFLICT 2WAY MERGE

> git은 어떻게 충돌을 파악하는가

### 5-1. 

```
```







## 6. 













