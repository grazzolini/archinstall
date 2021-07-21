# A desktop environment using "bspwm"

import archinstall

is_top_level_profile = False

__packages__ = [
    "bspwm",
    "sxhkd",
	"xdo",
	"rxvt-unicode",
	"lightdm-gtk-greeter",
	"lightdm",
]

def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	# bswpm requires a functioning Xorg installation.
	profile = archinstall.Profile(None, 'xorg')
	with profile.load_instructions(namespace='xorg.py') as imported:
		if hasattr(imported, '_prep_function'):
			return imported._prep_function()
		else:
			print('Deprecated (??): xorg profile has no _prep_function() anymore')

# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("bspwm", "/somewhere/bspwm.py")
# or through conventional import bspwm
if __name__ == "bspwm":
	# Install dependency profiles
	archinstall.storage['installation_session'].install_profile('xorg')

	# Install packages for bspwm
	archinstall.storage['installation_session'].add_additional_packages(__packages__)

	# Enable Light Display Manager
	archinstall.storage['installation_session'].enable_service('lightdm')
