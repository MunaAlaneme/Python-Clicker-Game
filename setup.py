import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--name=MSCopilotClicker',
    '--windowed',
    '--noconsole',
    #'--icon=copilot.ico',
    '--icon=copilot.icns',
    '--onefile',
    '--onedir'
])