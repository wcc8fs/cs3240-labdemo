Last login: Thu Sep 24 14:57:32 on ttys000
d-172-25-43-98:~ willcray$ ls
Applications		Downloads		Music			PycharmProjects
Desktop			Library			Pictures		cs3240-labdemo
Documents		Movies			Public			virtual_environment
d-172-25-43-98:~ willcray$ cd cs3240-labdemo
d-172-25-43-98:cs3240-labdemo willcray$ ls
LICENSE		README.md	hello.py
d-172-25-43-98:cs3240-labdemo willcray$ hello.py
-bash: hello.py: command not found
d-172-25-43-98:cs3240-labdemo willcray$ nano hello.py
d-172-25-43-98:cs3240-labdemo willcray$ ls
LICENSE		README.md	hello.py
d-172-25-43-98:cs3240-labdemo willcray$ cd ..
d-172-25-43-98:~ willcray$ ls
Applications		Downloads		Music			PycharmProjects
Desktop			Library			Pictures		cs3240-labdemo
Documents		Movies			Public			virtual_environment
d-172-25-43-98:~ willcray$ cd cs3240-labdemo
d-172-25-43-98:cs3240-labdemo willcray$ status
-bash: status: command not found
d-172-25-43-98:cs3240-labdemo willcray$ ls
LICENSE		README.md	hello.py
d-172-25-43-98:cs3240-labdemo willcray$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
d-172-25-43-98:cs3240-labdemo willcray$ git commit
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
	modified:   hello.py

no changes added to commit
d-172-25-43-98:cs3240-labdemo willcray$ git add hello.py
d-172-25-43-98:cs3240-labdemo willcray$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   hello.py

d-172-25-43-98:cs3240-labdemo willcray$ git commit
[master be66892] hello.py updated
 1 file changed, 2 insertions(+), 1 deletion(-)
d-172-25-43-98:cs3240-labdemo willcray$ git log
commit be6689269627db740e27808c8d53930820ea28c5
Author: wcc8fs <wcc8fs@virginia.edu>
Date:   Mon Sep 28 16:42:36 2015 -0400

    hello.py updated

commit 7346ba96680033f41d76f1968c59cfd9a5dd72f7
Author: wcc8fs <wcc8fs@virginia.edu>
Date:   Thu Sep 24 15:05:50 2015 -0400

    Initial commit

commit c62b51054f5aaf0a6b245fb440c8a146b9d4365c
Author: wcc8fs <wcc8fs@virginia.edu>
Date:   Thu Sep 24 15:01:49 2015 -0400

    Initial commit
d-172-25-43-98:cs3240-labdemo willcray$ nano

  GNU nano 2.0.6                       New Buffer                                          Modified  

def greeting(msg):
        print(msg)

















































^G Get Help     ^O WriteOut     ^R Read File    ^Y Prev Page    ^K Cut Text     ^C Cur Pos
^X Exit         ^J Justify      ^W Where Is     ^V Next Page    ^U UnCut Text   ^T To Spell
