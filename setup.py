from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = parse_requirements("requirements.txt", session=False)
setup(
  name = "get_a_shell",
  packages = find_packages(),
  version = "1",
  license = "AGPLv3",
  description = "Get a shell code (bind/reverse) into different languages ",
  author = "Emilien Peretti",
  author_email = "code@emilienperetti.be",
  url = "https://github.com/EmilienPer/GetAShell",
  install_requires=[str(r.req) for r in requirements],
  long_description=long_description,
  long_description_content_type="text/markdown",
  entry_points={
        'console_scripts': ['get_a_shell=get_a_shell.get_a_shell:main_with_args',
                            'getashell=get_a_shell.get_a_shell:main_with_args'],
    }
)