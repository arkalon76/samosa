from setuptools import setup

setup(name='samosa',
      version='0.1',
      description='Scans media files to find a better version of it self',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
      ],
      keywords='movie search quality download torrent',
      url='https://github.com/arkalon76/samosa',
      author='Kenth Fagerlund',
      author_email='kenth.fagerlund@gmail.com',
      license='MIT',
      packages=['samosa'],
      install_requires=[
        'mediainfo',
      ],
      test_suite='tests',
      tests_require=['pytest',
                     'pytest',
                     'pytest-pep8',
                     'pytest-cov'],
      entry_points={'console_scripts': [
                        'samosa = samosa:main',
                        ],
                    },
      zip_safe=False)
