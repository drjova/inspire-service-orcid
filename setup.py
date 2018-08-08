
from setuptools import setup
setup(**{'author': 'puntonim',
 'author_email': 'foo@gmail.com',
 'classifiers': ['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Internet :: WWW/HTTP'],
 'description': 'ORCID service client',
 'include_package_data': True,
 'install_requires': ['pkgsettings<1.0.0,>=0.12.0', 'orcid<2,>=1.0.3'],
 'long_description': "[![Build Status](https://travis-ci.org/puntonim/inspire-service-orcid.svg?branch=master)](https://travis-ci.org/puntonim/inspire-service-orcid)\n\n# Inspire ORCID service client\n\nThis package is service client for ORCID API used in inspire-next.\n\n## Client usage\n\n```python\n# Configure settings.\nimport inspire_services.orcid.conf\nd = dict(\n    DO_USE_SANDBOX=False,\n    CONSUMER_KEY='myorcidappkey',\n    CONSUMER_SECRET='myorcidappsecret',\n    REQUEST_TIMEOUT=30,\n)\ninspire_services.orcid.conf.settings.configure(**d)\n\n# Use the client.\nfrom inspire_services.orcid.client import OrcidClient\nclient = OrcidClient('mytoken', '0000-0002-0942-3697')\nresponse = client.get_all_works_summary()\nresponse.raise_for_result()\nputcode = response['group'][0]['work-summary'][0]['put-code']\n```\n\n## Development\n\n```bash\n# Create a venv and install the requirements:\n$ make venv\n\n# Run isort and lint:\n$ make isort\n$ make lint\n\n# Run all the tests:\n$ make test  # tox against Python27 and Python36.\n$ tox -e py27  # tox against a specific Python version.\n$ pytest  # pytest against the active venv.\n\n# Run a specific test:\n$ make test/tests/test_orcid.py  # tox against Python27 and Python36.\n$ tox -e py27 -- tests/test_orcid.py  # tox against a specific Python version.\n$ pytest tests/test_orcid.py  # pytest against the active venv.\n```\n\nTo publish on PyPi, first set the PyPi credentials:\n\n```bash\n# Edit .pypirc:\n$ cat $HOME/.pypirc\n[pypi]\nusername: myuser\npassword: mypass\n```\n\n```bash\n# Edit the version in `setup_gen.py`.\n# ... version=pep440_version('1.1.1'),\n# Then generate setup.py with:\n$ make setup.py\n# Commit, tag, push:\n$ git commit -m '1.1.1 release'\n$ git tag 1.1.1\n$ git push origin master --tags\n\n# Finally publish:\n$ make publish\n```\n",
 'name': 'inspire-service-orcid',
 'packages': ['inspire_services', 'inspire_services.orcid'],
 'tests_require': ['tox'],
 'url': 'https://github.com/puntonim/inspire-service-orcid',
 'version': '2.0.2',
 'zip_safe': False})
