import setuptools

#with open('README.rst', 'r') as readme:
#    long_description = readme.read()

setuptools.setup(
    name='declare_ui',
    version='0.1.0',
    author='Jason DeLaat',
    author_email='jason.develops@gmail.com',
    packages=setuptools.find_packages(),
    #url='https://bitbucket.org/jason_delaat/pymonad',
    license='BSD-3-Clause',
    description='A thin-ish wrapper around tkinter for specifying GUIs declaratively.',
    #long_description= long_description,
    #long_description_content_type='text/x-rst',
    classifiers=[ "Intended Audience :: Developers"
                  , "License :: OSI Approved :: BSD License"
                  , "Operating System :: OS Independent"
                  , "Programming Language :: Python :: 3"
                  , "Topic :: Software Development"
                  , "Topic :: Software Development :: Libraries"
                  , "Topic :: Utilities"
    ],
    python_requires='>=3.7',
)
