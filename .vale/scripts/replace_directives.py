import sys
import os
from pathlib import Path
import re


# here you can append the path to your configuration to extract the used needs
sys.path.append(os.path.abspath('../../docs'))

def replace_directives():

   replacements = []

   # you have to adapt how to extract your directives to be replaced
   # start:
   from metamodel import needs_types

   for need in needs_types:
         need_name = need['directive']
         needpattern =    "\.\.(\s+)" + need_name + "::"
         replacepattern = "  \1" + " " * len(need_name) + "  "
         replacements.append((needpattern, replacepattern))

   # end:

   return replacements


def replace_directive_roles():

   replacements = []

   # you have to adapt how to extract your directives to be replaced
   # start:

   #end:

   return replacements


def replace_roles():

   replacements = []

   # you have to adapt how to extract your directives to be replaced
   # start:

   roles = ["need", "need_incoming", "need_outgoing", "need_part", "np", "need_count", "need_func", "ndf", ]

   for role in roles:
      rolepattern = ":" + role + ":"
      replacepattern = " " + " " * len(role) + " "
      replacements.append((rolepattern, replacepattern))

      from sphinx_needs.defaults import NEED_DEFAULT_OPTIONS

   for key, value in NEED_DEFAULT_OPTIONS.items():
      optionpattern = "\s+:" + key + ":.*"
      replacepattern = " " + " " * len(key) + " "
      replacements.append((optionpattern, replacepattern))

   from metamodel import needs_extra_options

   for option in needs_extra_options:
      optionpattern = "\s+:" + option + ":.*"
      replacepattern = " " + " " * len(option) + " "
      replacements.append((optionpattern, replacepattern))

   #end:

   return replacements


def replace_additional_strings():
   replacements = []
   #here you can give in additional replacements

   return replacements


class clean_rst:

   def __init__(self):
      this.directives = replace_directives()
      this.directive_roles = replace_directive_roles()
      this.roles = replace_roles()
      this.additional_strings = replace_additional_strings()

      this.replacements = this.directives + this.directive_roles + this.roles + this.additional_strings

   def replace_content_in_file(file):

      content = file.read_text()

      for replacement in this.replacements:
         content = re.sub(r"" + str(replacement[0]), r"" + str(replacement[1]), content)

      file.write_text(content)

      return True

   def replace_content_in_files(folder_path, filepattern:str='**/*.rst'):

      success = True

      p = Path(folder_path)

      files = Path(directory).glob(filepattern)

      for file in pfiles:

         success = success and replace_content_in_file(file)

         if not success:
            break

      return success
