from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
from os import path
import shutil
import subprocess

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class build_py(_build_py):
    def run(self):
        self._build_js()
        super().run()

    def _build_js(self):
        build_js = path.join(here, 'jnitrace', 'build', 'jnitrace.js')
        if path.exists(build_js):
            return
        if shutil.which('npm') is None:
            raise RuntimeError('npm is required to build jnitrace.js')
        subprocess.check_call(['npm', 'install'], cwd=here)
        subprocess.check_call(['npm', 'run', 'build'], cwd=here)


setup(
    name='jnitrace',
    version='3.3.1',
    description='A tool for tracing use of the JNI in Android apps',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chame1eon/jnitrace',
    author='chame1eon',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'Topic :: Software Development :: Debuggers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='frida jni sre android tracing',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.0, <4',
    install_requires=[
        'frida>=14.0.5',
        'colorama',
        'hexdump'
    ],
    package_data={
        'jnitrace.build': ['jnitrace.js'],
    },
    include_package_data=True,
    cmdclass={
        'build_py': build_py,
    },
    entry_points={
        'console_scripts': [
            'jnitrace=jnitrace.jnitrace:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/chame1eon/jnitrace/issues',
    },
)
