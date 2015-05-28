from distutils.core import setup

import versioneer

versioneer.VCS = 'git'
versioneer.versionfile_source = 'sherpatest/_version.py'
versioneer.versionfile_build = 'sherpatest/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'sherpatest-'

setup(name='sherpatest',
      version=versioneer.get_version(),
      packages=['sherpatest'],
      cmdclass=versioneer.get_cmdclass(),
      )

