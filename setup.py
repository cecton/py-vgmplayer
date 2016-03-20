#!/usr/bin/env python
import os
import re
import sys

from setuptools import setup, find_packages, Extension


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


requires = [
]


def get_version():
    init = open(os.path.join(ROOT, 'vgmplayer', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


define_macros = [('ENABLE_ALL_CORES', 1)]
libraries = ['m', 'z']
include_dirs = []
if sys.platform == 'darwin':
    define_macros += [
        ('MACOSX', 1),
        ('USE_LIBAO', 1),
        ('DISABLE_HWOPL_SUPPORT', 1),
        ('DISABLE_HW_SUPPORT', 1),
    ]
    libraries += ['ao']
elif sys.platform == 'win32':
    define_macros += [('WINDOWS', 1)]


setup(
    name="py-vgmplayer",
    version=get_version(),
    description='A Python library to play VGM files',
    long_description=open('README.md').read(),
    author='Cecile Tonglet',
    author_email='cecile.tonglet@gmail.com',
    url='https://github.com/cecton/py-vgmplayer',
    scripts=[],
    zip_safe=False,
    packages=find_packages(exclude=['tests*']),
    install_requires=requires,
    license="GPLv2",
    ext_modules = [
        Extension(
            'vgmplayer/_libvgm',
            """
            VGMPlay/libvgm.c VGMPlay/VGMPlay.c
            VGMPlay/Stream.c VGMPlay/ChipMapper.c VGMPlay/chips/262intf.c
            VGMPlay/chips/2151intf.c VGMPlay/chips/2203intf.c
            VGMPlay/chips/2413intf.c VGMPlay/chips/2608intf.c
            VGMPlay/chips/2610intf.c VGMPlay/chips/2612intf.c
            VGMPlay/chips/3526intf.c VGMPlay/chips/3812intf.c
            VGMPlay/chips/8950intf.c VGMPlay/chips/adlibemu_opl2.c
            VGMPlay/chips/adlibemu_opl3.c VGMPlay/chips/ay8910.c
            VGMPlay/chips/ay_intf.c VGMPlay/chips/c140.c VGMPlay/chips/c352.c
            VGMPlay/chips/c6280.c VGMPlay/chips/c6280intf.c
            VGMPlay/chips/dac_control.c VGMPlay/chips/es5503.c
            VGMPlay/chips/es5506.c VGMPlay/chips/emu2149.c
            VGMPlay/chips/emu2413.c VGMPlay/chips/fm2612.c VGMPlay/chips/fm.c
            VGMPlay/chips/fmopl.c VGMPlay/chips/gb.c VGMPlay/chips/iremga20.c
            VGMPlay/chips/k051649.c VGMPlay/chips/k053260.c
            VGMPlay/chips/k054539.c VGMPlay/chips/multipcm.c
            VGMPlay/chips/nes_apu.c VGMPlay/chips/nes_intf.c
            VGMPlay/chips/np_nes_apu.c VGMPlay/chips/np_nes_dmc.c
            VGMPlay/chips/np_nes_fds.c VGMPlay/chips/okim6258.c
            VGMPlay/chips/okim6295.c VGMPlay/chips/Ootake_PSG.c
            VGMPlay/chips/panning.c VGMPlay/chips/pokey.c VGMPlay/chips/pwm.c
            VGMPlay/chips/qsound.c VGMPlay/chips/rf5c68.c
            VGMPlay/chips/saa1099.c VGMPlay/chips/segapcm.c
            VGMPlay/chips/scd_pcm.c VGMPlay/chips/scsp.c
            VGMPlay/chips/scspdsp.c VGMPlay/chips/sn76489.c
            VGMPlay/chips/sn76496.c VGMPlay/chips/sn764intf.c
            VGMPlay/chips/upd7759.c VGMPlay/chips/vsu.c
            VGMPlay/chips/ws_audio.c VGMPlay/chips/x1_010.c
            VGMPlay/chips/ym2151.c VGMPlay/chips/ym2413.c
            VGMPlay/chips/ym2612.c VGMPlay/chips/ymdeltat.c
            VGMPlay/chips/ymf262.c VGMPlay/chips/ymf271.c
            VGMPlay/chips/ymf278b.c VGMPlay/chips/ymz280b.c
            VGMPlay/chips/ay8910_opl.c VGMPlay/chips/sn76496_opl.c
            VGMPlay/chips/ym2413hd.c VGMPlay/chips/ym2413_opl.c
            """.split(),
            define_macros=define_macros,
            include_dirs=include_dirs,
            libraries=libraries,
        )],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
