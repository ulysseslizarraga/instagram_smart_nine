from setuptools import setup, find_packages

requires = ['pytz==2020.5',
            'opencv-python==4.4.0.46',
            'instagram-scraper==1.9.1',
            'matplotlib==3.3.3',
            'numpy==1.19.4',
            'scipy==1.5.4']

setup(name='smart-nine',
      version='0.0.2',
      description=("smart-nine is a command-line application written in Python"
                 " that generates an Instagram user's top nine photograph collage. Use responsibly."),
      url='https://github.com/ulysseslizarraga/instagram_smart_nine',
      author='Ulysses Lizarraga',
      author_email='ulises.lizarraga@gmail.com',
      license='Public domain',
      packages=find_packages(exclude=['tests']),
      install_requires=requires,
      entry_points={'console_scripts': ['smart-nine=smart_nine.app:main'],},
      zip_safe=False,
      keywords=['instagram', 'top', 'nine', 'smart', 'photos', 'collage', 'year'])