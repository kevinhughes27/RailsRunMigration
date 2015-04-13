import sublime, sublime_plugin
import subprocess
import os
import re


class Error(Exception):
  def __init__(self, msg):
    self.msg = msg
    sublime.error_message(self.msg)


class NotMigration(Error):
  pass


class RailsDownMigrationCommand(sublime_plugin.TextCommand):


  def run(self, edit):
    self.edit = edit
    self.run_migration('down')


  def run_migration(self, direction):
    filename = self.view.file_name()

    if( filename and self.is_migration(filename) ):
      version = self.get_migration_version(filename)

      path = self.rails_bin_path(filename)

      cmd = ["./bundle exec rake db:migrate:{direction} VERSION={version}".format(
        direction=direction, version=version
      )]

      output = self.run_command(cmd, path)
      self.display_output(output)
    else:
      raise NotMigration("The current file is not a rails migration")

    return


  def is_migration(self, filename):
    return re.match('\S*/db/migrate/\d{14,14}\S*.rb', filename)


  def get_migration_version(self, filename):
    return re.search("\d{14,14}", filename).group()


  def rails_bin_path(self, filename):
    idx = filename.find("db/migrate")
    return filename[0:idx] + "bin"


  def run_command(self, cmd, path):
    p = subprocess.Popen(
      cmd,
      cwd=path,
      stdout=subprocess.PIPE,
      stderr=subprocess.STDOUT,
      shell=True,
    )
    output = p.stdout.read().decode("utf-8")
    return output


  def display_output(self, output):
    new_file = self.view.window().new_file()
    new_file.insert(self.edit, 0, output)
    new_file.set_name('Migration results')
    new_file.set_scratch(True)
    new_file.set_read_only(True)
    return
