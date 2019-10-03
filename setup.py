import setuptools

setuptools.setup(
  name = 'pyazdvop',
  version = '1.0',
  description = 'Library for Azure DevOps API for Python',
  author = 'M Faizal Sidek',
  author_email = 'mfaizal.sidek@petronas.com.my',
  license = 'MIT',
  packages = ['azdvop'],
  zip_safe = False,
  install_requires = ['requests'],
  url = 'https://github.com/rockraft7/pyazdevops',
  keywords = ['Azure', 'DevOps', 'Python', 'API'],
  classifiers = [
    'Development Status :: Early access', 
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: SDK',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7'
  ]
)
