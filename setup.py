from setuptools import setup

setup(
    name='aioschedule',  # Укажите уникальное имя для вашего пакета
    version='0.1.0',            # Версия вашего пакета
    py_modules=['aioschedule.py'], # Указываем, что это один модуль из файла aioschedule.py
    description='Modified aioschedule for Python 3.10+',
    long_description=open('README.md', encoding='utf-8').read() if 'README.md' else '',
    long_description_content_type='text/markdown',
    author='mrcat2445',
    author_email='mrcat2445official@gmail.com',
    url='https://github.com/mrcat2445/aioschedule',
    install_requires=[
        # Если ваш aioschedule.py использует какие-либо внешние библиотеки,
        # перечислите их здесь. Например:
        # 'asyncio', # Обычно asyncio встроен, но если есть другие...
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
