import sys
import os
from pathlib import Path
import re


# here you can append the path to your configuration to extract the used needs
p = Path(__file__).parent.resolve().joinpath('../../docs').resolve()
sys.path.append(p.as_posix())

def replace_match_with_spaces(match):
   return " " * len(match.group(0))

def replace_directives():

   replacements = []

   # you have to adapt how to extract your directives to be replaced
   # start:
   from metamodel import needs_types

   for need in needs_types:
         need_name = need['directive']
         needpattern =    r"\.\.(\s+)" + r'{}'.format(need_name) + r"::"
         replacepattern = replace_match_with_spaces
         replacements.append((needpattern, replacepattern))

   # end:

   return replacements


def replace_directive_options():

   replacements = []

   # you have to adapt how to extract your directives to be replaced
   # start:
   from sphinx_needs.defaults import NEED_DEFAULT_OPTIONS

   for key, value in NEED_DEFAULT_OPTIONS.items():
      optionpattern =  r":" + r'{}'.format(key) + r":" + r"[^\n\r]*"
      replacepattern = replace_match_with_spaces
      replacements.append((optionpattern, replacepattern))

   from metamodel import needs_extra_options

   for option in needs_extra_options:
      optionpattern =  r":" + r'{}'.format(option) + r":" + r"[^\n\r]*"
      replacepattern = replace_match_with_spaces
      replacements.append((optionpattern, replacepattern))
   #end:

   return replacements


def replace_directive_links():

   replacements = []

   # you have to adapt how to extract your directives to be replaced
   # start:
   from metamodel import needs_extra_links

   for link in needs_extra_links:
      optionpattern =  r":" + r'{}'.format(link["option"]) + r":" + r"[^\n\r]*"
      replacepattern = replace_match_with_spaces
      replacements.append((optionpattern, replacepattern))
   #end:

   return replacements


def replace_roles():

   replacements = []

   # you have to adapt how to extract your directives to be replaced
   # start:

   roles = ["need", "need_incoming", "need_outgoing", "need_part", "np", "need_count", "need_func", "ndf", ]

   for role in roles:
      rolepattern =    r":" + r'{}'.format(role) + r":" + r"`[^`]*`"
      replacepattern = replace_match_with_spaces
      replacements.append((rolepattern, replacepattern))

   replacements = []
   #currently disabled

   #end:

   return replacements


def replace_additional_strings():
   replacements = []
   #here you can give in additional replacements

   return replacements


class clean_rst:

   def __init__(self):
      self.directives = replace_directives()
      self.directive_options = replace_directive_options()
      self.directive_links = replace_directive_links()
      self.roles = replace_roles()
      self.additional_strings = replace_additional_strings()

      self.replacements = self.directives + \
                          self.directive_options + self.directive_links + \
                          self.roles + self.additional_strings

   def replace_content_in_file(self, file):

      print("replace file: " + str(file))

      content = file.read_text()

      for replacement in self.replacements:
         content = re.sub(replacement[0], replacement[1], content)

      file.write_text(content)

      return True

   def replace_content_in_files(self, folder_path, filepattern:str='**/*.rst'):

      success = True

      p = Path(folder_path).resolve()

      #print(p)

      files = p.glob(filepattern)

      #print(list(files))

      for file in files:

         success = success and self.replace_content_in_file(file)

         if not success:
            break

      return success

if __name__ == '__main__':

   p = Path(__file__).parent.resolve().joinpath('../..').resolve()

   cr = clean_rst()

   cr.replace_content_in_files(p)
