RailsRunMigration
=================


Sublime Text 3 plugin to run or rollback the open migration using rake db:migrate:up/down


Usage
-----

Bring up your command pallette (Cmd + Shift + P / Ctrl + Shift + P) and then type `migrate` and you should see it pop up in the list of commands.


Development
-----------

clone the repo and then symlink it to your sublime packages directory

eg.

```
 ln -s /home/kevin/Dropbox/Projects/RailsRunMigration /home/kevin/.config/sublime-text-3/Packages/RailsRunMigration
```


Setting up with chruby
----------------------

see:

https://github.com/postmodern/chruby/wiki/Sublime-Text
(was this actually required?)

note - you need to run sublime from your terminal. If you get errors about bundler and your ruby version try changing cmd to `ruby -v` to make sure Sublime is successfully forwarding through chruby.
