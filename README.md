VimStudio - an Gradle/Android Neovim plugin - batteries included
================================================================================

This is a Vim Plugin for Android development based on the superb [Vim-Grand](https://github.com/meonlol/vim-grand) which is in turn based on [hsanson/vim-android](https://github.com/hsanson/vim-android).

Requirements
--------------------------------------------------------------------------------

- Neovim w/ Python 3 installed
- [exuberant-ctags](http://ctags.sourceforge.net/) for the `VimStudioCtags` command.
- [Neomake](https://github.com/neomake/neomake) for syntax
  checking.
- [artur-shaik/javacomplete2](https://github.com/artur-shaik/vim-javacomplete2) For code
  completion and classpath gathering


Installation
--------------------------------------------------------------------------------

If you don't use one already, install a package manager plugin like Pathogen
or Vundle. It makes installing as simple as:

_vim-plug:_

1. Add the line `Plug 'DonnieWest/VimStudio'` to your .vimrc
2. Call `:so %` on the updated .vimrc to reload it.
3. Run `:PlugInstall` to let vundle install it for you.



Features
--------------------------------------------------------------------------------

### Warning! VimStudio currently only works on Unix systems

*:SetupVimStudio* Sets the compiler to be Gradle and builds the project. Relies on the JavaComplete2 plugin

*:Gradle* is a wrapper around the gradle command line interface

*:ADB* is a wrapper around the adb command line interface

*:VimStudioEmulator* autocompletes and launches emulators available on your system

*:VimStudioInstall* installs the apk on a device of your choice

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
