try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

long_desc = """
	Expense.txt allows you to track and analyze your expenses using plain text files. With this tool you can see what your spending money on, search based on categories, projects amounts, dates or some combination of the aforementioned list. The format of the expense file is completely freeform and consistent with GTD style for todos.
"""


setup(name="expense.txt",
      version=1.0,
      description="Expense.txt allows you to track and analyze your expenses using plain text files.",
      author="Ben Smith",
      author_email="ben@wbpsystems.com",
      url="https://github.com/tazzben/expense.txt",
      license="MIT",
      packages=[],
      scripts=['expense'],
      package_dir={},
      long_description=long_desc,
      classifiers=[
          'Topic :: Text Processing',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop'
      ]
     )