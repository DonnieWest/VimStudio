let current_compiler = 'gradleLint'

exec 'CompilerSet makeprg=' . g:gradleBin . '\ --console=plain\ '


CompilerSet errorformat=\%-G%f:%l:\ %tarning:\ Element\ SubscribeHandler\ unvalidated\ %.%#,
                        \[ant:checkstyle\]\ %f:%l:%c:\ %m,
                        \[ant:checkstyle\]\ %f:%l:\ %m,
                        \Build\ file\ '%f'\ line:\ %l,
                        \%+GUnknown\ command-line\ option\ %m,
                        \%+GTask\ %.%#\ not\ found\ %.%#.\ %m,
                        \%E>\ %f:%l:%c:\ %trror:\ %m,
                        \%W>\ %f:%l:%c:\ %tarning:\ %m,
                        \%E%f:%l:\ %trror:\ %m,
                        \%W%f:%l:\ %tarning:\ %m,
                        \%EFAILURE:\ %m,
                        \%Z%p%*[%^~],
                        \%Z>\ %m\ file://%f,
                        \%Z>\ %m,
                        \%C%.%#
