# A system with "xorg" installed

import os
import archinstall

is_top_level_profile = True

__packages__ = [
	'dkms',
	'xorg-server',
	'xorg-xinit',
	'nvidia-dkms',
	'xorg-server',
	*archinstall.lib.hardware.__packages__,
]


def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	__builtins__['_gfx_driver_packages'] = archinstall.select_driver()

	# TODO: Add language section and/or merge it with the locale selected
	#       earlier in for instance guided.py installer.

	return True


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("xorg", "/somewhere/xorg.py")
# or through conventional import xorg
if __name__ == 'xorg':
	try:
		if "nvidia" in _gfx_driver_packages:
			if (
				"linux-zen" in installation.base_packages
				or "linux-lts" in installation.base_packages
			):
				installation.add_additional_packages(
					"dkms"
				)  # I've had kernel regen fail if it wasn't installed before nvidia-dkms
				installation.add_additional_packages("xorg-server xorg-xinit nvidia-dkms")
			else:
				installation.add_additional_packages(
					f"xorg-server xorg-xinit {' '.join(_gfx_driver_packages)}"
				)
		else:
			installation.add_additional_packages(
				f"xorg-server xorg-xinit {' '.join(_gfx_driver_packages)}"
			)
	except:
		installation.add_additional_packages(
			f"xorg-server xorg-xinit"
		)  # Prep didn't run, so there's no driver to install

	# with open(f'{installation.mountpoint}/etc/X11/xinit/xinitrc', 'a') as X11:
	# 	X11.write('setxkbmap se\n')

	# with open(f'{installation.mountpoint}/etc/vconsole.conf', 'a') as vconsole:
	# 	vconsole.write('KEYMAP={keyboard_layout}\n'.format(**arguments))
	# 	vconsole.write('FONT=lat9w-16\n')

	# awesome = archinstall.Application(installation, 'awesome')
	# awesome.install()
