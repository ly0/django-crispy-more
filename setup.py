from setuptools import setup, find_packages
 
version = '0.0.1'
 
setup(
    name='django-crispy-more',
    version=version,
    description="Plugins for django-crispy-forms",
    long_description=open('README.md').read(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT Software License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=['forms', 'django', 'crispy', 'plugins'],
    author='latyas, wangwei',
    author_email='latyas@gmail.com, wangweiun@gmail.com',
    url='http://github.com/ly0/django-crispy-more',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['django',
                      'django-crispy-forms',
                      ],
)
