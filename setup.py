"""Setup for orbitdocXBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='orbitdoc-xblock',
    version='0.1',
    description='This XBlock enables an easy way to embed documents(.doc,.ppt,etc..)and allows to download them.',
    packages=[
        'orbitdoc',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'orbitdoc = orbitdoc:orbitdocXBlock',
        ]
    },
    package_data=package_data("orbitdoc", "static"),
)