from setuptools import setup, find_packages


def listify(filename):
    return filter(None, open(filename, 'r').read().split('\n'))


def remove_externals(requirements):
    return filter(lambda e: not e.startswith('-e'), requirements)

setup(
    name="vxgsm",
    version="0.1.0",
    url='http://github.com/praekelt/vxgsm',
    license='BSD',
    description="Gammu based GSM Transport for Vumi",
    long_description=open('README.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekeltfoundation.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['setuptools'] +
                     remove_externals(listify('requirements.pip')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
    ],
)
