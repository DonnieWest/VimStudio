if !has('nvim') || !has('python3')
  echomsg '[VimStudio] VimStudio does not work with this version.'
  echomsg '[VimStudio] It requires Neovim with Python3 support ("+python3")'
elseif !exists(':SetupVimStudio')
  UpdateRemotePlugins
  echomsg '[VimStudio] Not initialized. Please restart Neovim'
  return
endif

  let g:VimStudioDirectory = expand('<sfile>:p:h:h')
