if exists(g:gradleBin)
  let current_compiler = 'gradle'

  let s:makeprg = [
  \  g:gradleBin,
  \  '--console=plain',
  \  '-I',
  \  g:VimStudioDirectory . '/init.gradle',
  \ '--daemon'
  \ ]

  exec 'CompilerSet makeprg=' . join(s:makeprg, '\ ')

  CompilerSet errorformat=
      \%+ATask\ %.%#\ not\ found\ %.%#.,
      \%EExecution\ failed\ for\ task\ %m,
      \findbugs:\ %tarning\ %f:%l:%c\ %m,
      \pmd:\ %tarning\ %f:%l:%c\ %m,
      \checkstyle:\ %tarning\ %f:%l:%c\ %m,
      \lint:\ %tarning\ %f:%l:%c\ %m,
      \lint:\ %trror\ %f:%l:%c\ %m,
      \%A>\ %f:%l:%c:\ %trror:\ %m,
      \%A>\ %f:%l:%c:\ %tarning:\ %m,
      \%A%f:%l:\ %trror:\ %m,
      \%A%f:%l:\ %tarning:\ %m,
      \%A%f:%l:\ %trror\ -\ %m,
      \%A%f:%l:\ %tarning\ -\ %m,
      \%E%f:%l\ :\ %m,
      \%C>\ %m,
      \%-G%p^,
      \%+G\ \ %.%#,
      \%-G%.%#
endif
