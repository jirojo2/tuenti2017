for branch in $(git branch); do for commit in $(git rev-list $branch); do git checkout $commit; date=($(git show -s --format=%ci $commit)); cp script.php ../script-$date.php; done; done
do for commit in $(git rev-list master); do git checkout $commit; date=($(git show -s --format=%ci $commit)); cp script.php ../script-$date.php; done
