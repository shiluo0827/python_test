##如何删除git and github 上的历史提交记录？

1.尝试运行 git checkout --orphan lastest_branch
2.添加所有文件 git add -A ## 或使用 git add .
3.提交更改 git commit -am "commit message"
4.删除分支 git branch -D master
5.将当前分支重命名 git branch -m master
6.最后，强制更新github仓库 git push -f origin master

主要原理就是将当前最新的版本代码，建立一个分支，以当前版本为基础提交代码。
删除原来的master主分支，再将当前分支名称改成master，以便替换掉原来的分支。
最后更新远程库，github自然也会以新的代码版本和替换的主分支为唯一的代码版本。
这样就实现了删除所有历史版本的目的。
