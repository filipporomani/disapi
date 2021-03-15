from distutils.core import setup
import setuptools
setup(
  name = 'disapi',        
  packages = ['disapi'],   
  version = '0.0.2',    
  license='MIT',   
  description = 'Basic Discord API module, built with Python. For docs see github (https://github.com/filipporomani/disapi).',  
  author = 'Filippo Romani', 
  author_email = 'filipporomanionline@gmail.com',     
  url = 'https://github.com/filipporomani/DisAPI',   
  download_url = 'https://github.com/filipporomani/disapi/archive/0.0.2.tar.gz', 
  keywords = ['DISCORD', 'API', 'DISCORD API', 'PYTHON', 'DISCORD MODULE', 'BOT'],   # Keywords that define your package best
  install_requires=[
          'requests',
          'datetime'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
setuptools.setup()