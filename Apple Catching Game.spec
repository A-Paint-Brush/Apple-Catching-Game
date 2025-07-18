# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py', 'Apple.py', 'Bowl.py', 'Data.py', 'Game.py', 'Results.py', 'Timer.py'],
    pathex=[],
    binaries=[],
    datas=[('Images', 'Images'), ('Sounds', 'Sounds')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Apple Catching Game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\cliff\\Pictures\\Icon Resources\\pygame.ico'],
)
