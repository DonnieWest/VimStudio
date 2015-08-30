VimStudio - an Gradle/Android Neovim plugin - batteries included
================================================================================

This is a Vim Plugin for Android development based on the superb [Vim-Grand](https://github.com/meonlol/vim-grand) which is in turn based on [hsanson/vim-android](https://github.com/hsanson/vim-android).

When Vim-Grand turned into a Ruby project, it broke the ability for it to be used with Neovim. This project is essentially a fork of the old python version of Vim-Grand turned into a remote plugin for Neovim. It also happens to work perfectly with generic Gradle projects.

Requirements
--------------------------------------------------------------------------------

- Neovim w/ Python 3 installed
- Android SDK installed with the $ANDROID_HOME environment variable set.
- Gradle 2.0+ (?) or a gradle wrapper in the project.
- [exuberant-ctags](http://ctags.sourceforge.net/) for the `VimStudioCtags` command.
- [scrooloose/syntastic](https://github.com/scrooloose/syntastic) for syntax
  checking.
- [artur-shaik/javacomplete2](https://github.com/artur-shaik/vim-javacomplete2) For code
  completion.

### Recommended

- [Tim Pope's Dispatch](https://github.com/tpope/vim-dispatch) vim-grand will
  run the appropriate commands through it, so vim doesn't get blocked. Highly
  recommended.
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
### Warning! VimStudio also currently modifies files in your home directory and adds plugins to Gradle. This will be configurable in the future

*On first launch, VimStudio will automatically setup Neovim and Gradle to behave most like an IDE. It will install a global Gradle plugin that it will run at start or when the build.gradle file is modified. This plugin provides the classpaths for autocompletion via Javacomplete2.

*:VimStudioSetup* Sets up all the project paths for javacomplete and syntastic.
When used in combination with the `grand.gradle` script, all paths defined in
your build.gradle will also be used for autocompletion and syntax checking.  

*:VimStudioCtags* Generates a tags file in the background using exuberant-ctags.
This way you can jump to classes (even Androids source files) simply by
pressing `CTRL-]`.

*VimStudio sets gradle to be the compiler

Additional setup for a pleasant experience
--------------------------------------------------------------------------------

These tweaks and mappings for in you .vimrc will make you happy.

Contributing
--------------------------------------------------------------------------------

Please do! You know the drill. Just
[issue](https://github.com/DonnieWest/VimStudio/issues) and
[pull](https://github.com/DonnieWest/VimStudio/pulls).

License
--------------------------------------------------------------------------------

Copyright (c) Leon Moll & Donnie West. Distributed under the same terms as Vim itself.
See `:help license`.
