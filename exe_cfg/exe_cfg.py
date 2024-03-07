import PyInstaller.__main__


PyInstaller.__main__.run([
        'main_app/shifter.py',
        '--onefile',
        #'--windowed',
        '--noconfirm',
])