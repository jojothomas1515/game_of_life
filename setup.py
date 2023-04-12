from cx_Freeze import setup, Executable

build_exe_options = {

    "zip_include_packages": ["tkinter"],
}

setup(
        name='game_of_life',
        version='0.10',
        url='',
        license='',
        author='jojo',
        author_email='',
        description='Conwey game of life',
        options={"build_exe": build_exe_options},
        executables=[Executable(
                "main.py",
        )]
)
