let current_compiler = 'gradle'

let f = tempname()
call mkdir(fnamemodify(f,':h'),'p',0700)
exec 'CompilerSet makeprg=javac\ -Xlint\ -d\ ' . shellescape(fnamemodify(f, ':h')) . '\ -cp\ ' . g:gradleClasspath

CompilerSet errorformat =%E%f:%l:\ error:\ %m,%W%f:%l:\ warning:\ %m,%E%f:%l:\ %m,%Z%p^,%-G%.%#
