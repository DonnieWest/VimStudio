" Ripped from https://github.com/hsanson/vim-android/blob/51135fb6b0b9a8bd84aff215def76fb6a6ef0236/compiler/gradle.vim
let current_compiler = 'gradle'

" Links to understand error formats
"   http://flukus.github.io/2015/07/03/2015_07_03-Vim-errorformat-Demystified/
exec 'CompilerSet makeprg=' . g:gradleBin . '\ --console=plain\ '
CompilerSet errorformat=\%-G%f:%l:\ %tarning:\ Element\ SubscribeHandler\ unvalidated\ %.%#,
                        \[ant:checkstyle\]\ %f:%l:%c:\ %m,
                        \[ant:checkstyle\]\ %f:%l:\ %m,
                        \Build\ file\ '%f'\ line:\ %l,
                        \%+GUnknown\ command-line\ option\ %m,
                        \%+GTask\ %.%#\ not\ found\ %.%#.\ %m,
                        \%f:%l\ :\ %trror\ parsing\ XML:\ %m,
                        \%f:%l\ :\ %tarning\ parsing\ XML:\ %m,
                        \%E%f:%l:\ %trror:\ %m,
                        \%W%f:%l:\ %tarning:\ %m,
                        \%EFAILURE:\ %m,
                        \%Z%p%*[%^~],
                        \%Z>\ %m\ file://%f,
                        \%Z>\ %m,
                        \%C%.%#
