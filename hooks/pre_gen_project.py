# def deprecation_warning():
#     print("""

# =============================================================================
# *** DEPRECATION WARNING ***

# Cookiecutter data science is moving to v2 soon, which will entail using
# the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
# will continue to work, and this version of the template will still be available.
# To use the legacy template, you will need to explicitly use `-c v1` to select it.

# Please update any scripts/automation you have to append the `-c v1` option,
# which is available now.

# For example:
#     cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
# =============================================================================

#     """)


# deprecation_warning()

import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.repo_name}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)