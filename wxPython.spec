# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['wxWindow.py'],
             pathex=['D:\\vs-work\\wxPython\\wxWindow'],
             binaries=[],
             datas=[("C:\\Users\\wes.wang\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\numpy", "numpy"),("C:\\Users\\wes.wang\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\wx", "wx"),("C:\\Users\\wes.wang\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\matplotlib", "matplotlib"),("C:\\Users\\wes.wang\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\PIL", "PIL")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='wxPython',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='wxPython')
