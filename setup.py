from setuptools import setup
import os
import versioneer

package_name = 'sherpatest'

files = []
for root, dirnames, filenames in os.walk(package_name):
    for filename in filenames:
        files.append(os.path.join(root, filename))

versioneer.VCS = 'git'
versioneer.versionfile_source = '{}/_version.py'.format(package_name)
versioneer.versionfile_build = '{}/_version.py'.format(package_name)
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = '{}-'.format(package_name)

setup(name=package_name,
      version=versioneer.get_version(),
      packages=[package_name],
      package_data={'sherpatest': files},
      include_package_data=True,
      cmdclass=versioneer.get_cmdclass(),
      )
