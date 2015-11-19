VimStudio - an Gradle/Android Neovim plugin - batteries included
================================================================================

This is a Vim Plugin for Android development based on the superb [Vim-Grand](https://github.com/meonlol/vim-grand) which is in turn based on [hsanson/vim-android](https://github.com/hsanson/vim-android).

Requirements
--------------------------------------------------------------------------------

- Neovim w/ Python 3 installed
- [exuberant-ctags](http://ctags.sourceforge.net/) for the `VimStudioCtags` command.
- [scrooloose/syntastic](https://github.com/scrooloose/syntastic) for syntax
  checking.
- [artur-shaik/javacomplete2](https://github.com/artur-shaik/vim-javacomplete2) For code
  completion and classpath gathering

### Recommended

- [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) for managing
  additional autocompletion features.


Installation
--------------------------------------------------------------------------------

If you don't use one already, install a package manager plugin like Pathogen
or Vundle. It makes installing as simple as:

_Vundle:_

1. Add the line `Plugin 'DonnieWest/VimStudio'` to your .vimrc
2. Call `:so %` on the updated .vimrc to reload it.
3. Run `:PluginInstall` to let vundle install it for you.

_Pathogen:_

Copy and past into the terminal:

    cd ~/.vim/bundle
    git clone git://github.com/tpope/vim-fugitive.git
    vim -u NONE -c "helptags vim-fugitive/doc" -c q



Features
--------------------------------------------------------------------------------

### Warning! VimStudio currently only works on Unix systems

*:SetupVimStudio* Sets up all the project paths for syntastic. Relies on the JavaComplete2 plugin

*:VimStudioCtags* Generates a tags file in the background using exuberant-ctags.
This way you can jump to classes (even Android source files) simply by
pressing `CTRL-]`.

*VimStudio sets gradle to be the compiler

Contributing
--------------------------------------------------------------------------------

Please do! You know the drill. Just
[issue](https://github.com/DonnieWest/VimStudio/issues) and
[pull](https://github.com/DonnieWest/VimStudio/pulls).

License
--------------------------------------------------------------------------------

Copyright (c) Leon Moll & Donnie West. Distributed under the same terms as Vim itself.
See `:help license`.
