from setuptools import setup, find_packages

VERSION = '0.9.1'
DESCRIPTION = 'A command-line tool to save and execute commands with variables.'
LONG_DESCRIPTION = """
cosave is a command-line tool that allows you to save and execute frequently used commands with placeholders for variables. 
This can be extremely useful for developers and system administrators who often run complex commands and want to avoid retyping them or remembering intricate syntax.

**Key Features:**

- **Save Commands:** Store your frequently used commands with names.
- **Variables:** Define variables within your commands using `[variable_name]` syntax.
- **Execute Commands:** Run saved commands by name, providing values for the variables on the fly.
- **List Commands:** Easily list all your saved commands.
- **Update Commands:** Modify existing saved commands.
- **Delete Commands:** Remove commands you no longer need.
- **Backup and Restore:** Backup your command library to a file and restore it later.
- **Output Control:** Choose whether to display the output of executed commands.

**Example Use Cases:**

- Quickly initialize projects with custom setups.
- Automate repetitive tasks with variable parameters.
- Share command recipes with colleagues.
- Keep a personal library of useful commands.
"""

setup(
    name='cosave',
    version=VERSION,
    author='Salah AlHajj',
    author_email='contact@salahaldin.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['PyYAML'],
    keywords=['command-line', 'automation', 'productivity', 'shell', 'scripting'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Shells",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'cosave=cosave:main',
        ],
    },
)