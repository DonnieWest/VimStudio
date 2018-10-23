if !has('nvim') || !has('python3')
  echomsg '[VimStudio] VimStudio does not work with this version.'
  echomsg '[VimStudio] It requires Neovim with Python3 support ("+python3")'
  finish
endif

let g:VimStudioDirectory = expand('<sfile>:p:h:h')

let g:gradleBin = filereadable('./gradlew') ? './gradlew' : 'gradle'

let g:neomake_java_gradle_maker = {
    \ 'exe': g:gradleBin,
    \ 'append_file': 0,
    \ 'args': ['compileDebugSources', '--daemon'],
    \ 'errorformat': '\%+ATask\ %.%#\ not\ found\ %.%#.,'.
    \'%EExecution\ failed\ for\ task\ %m,'.
    \'findbugs:\ %tarning\ %f:%l:%c\ %m,'.
    \'pmd:\ %tarning\ %f:%l:%c\ %m,'.
    \'checkstyle:\ %tarning\ %f:%l:%c\ %m,'.
    \'lint:\ %tarning\ %f:%l:%c\ %m,'.
    \'%A>\ %f:%l:%c:\ %trror:\ %m,'.
    \'%A>\ %f:%l:%c:\ %tarning:\ %m,'.
    \'%A%f:%l:\ %trror:\ %m,'.
    \'%A%f:%l:\ %tarning:\ %m,'.
    \'%A%f:%l:\ %trror\ -\ %m,'.
    \'%A%f:%l:\ %tarning\ -\ %m,'.
    \'%E%f:%l\ :\ %m,'.
    \'%C>\ %m,'.
    \'%-G%p^,'.
    \'%+G\ \ %.%#,'.
    \'%-G%.%#'
    \ }
let g:neomake_java_enabled_makers = ['gradle']

let g:neomake_kotlin_gradle_maker = {
    \ 'exe': g:gradleBin,
    \ 'append_file': 0,
    \ 'args': ['compileDebugSources', '--daemon'],
    \ 'errorformat': '\%+ATask\ %.%#\ not\ found\ %.%#.,'.
    \'%EExecution\ failed\ for\ task\ %m,'.
    \'findbugs:\ %tarning\ %f:%l:%c\ %m,'.
    \'pmd:\ %tarning\ %f:%l:%c\ %m,'.
    \'checkstyle:\ %tarning\ %f:%l:%c\ %m,'.
    \'lint:\ %tarning\ %f:%l:%c\ %m,'.
    \'%A>\ %f:%l:%c:\ %trror:\ %m,'.
    \'%A>\ %f:%l:%c:\ %tarning:\ %m,'.
    \'%A%f:%l:\ %trror:\ %m,'.
    \'%A%f:%l:\ %tarning:\ %m,'.
    \'%A%f:%l:\ %trror\ -\ %m,'.
    \'%A%f:%l:\ %tarning\ -\ %m,'.
    \'%E%f:%l\ :\ %m,'.
    \'%C>\ %m,'.
    \'%-G%p^,'.
    \'%+G\ \ %.%#,'.
    \'%-G%.%#'
    \ }
let g:neomake_kotlin_enabled_makers = ['gradle']
