"""
Created on 10-29-21 by Mojtaba Heydari  <mheydari@ur.rochester.edu>

"""


# Local imports
# None.

# Third party imports
# None.

# Python standard library imports
import setuptools
from setuptools import find_packages
import distutils.cmd


# Required packages
REQUIRED_PACKAGES = [
    'numpy<1.26',
    'cython',
    'librosa<0.11,>=0.10.0',
    'numba<0.59.0,>=0.58.0',
    'mido<1.4.0,>=1.3.2',
    'pytest',
    'pyaudio;platform_system!="Windows"',  # NOTE: Install PortAudio, e.g., `brew install portaudio` on macOS
    'torch<2.3,>=2.2.1',
    'matplotlib',
    'BeatNet<1.1.2,>=0.0.4',
    'madmom',  # NOTE: Install from source https://github.com/CPJKU/madmom
]


class MakeReqsCommand(distutils.cmd.Command):
  """A custom command to export requirements to a requirements.txt file."""

  description = 'Export requirements to a requirements.txt file.'
  user_options = []

  def initialize_options(self):
    """Set default values for options."""
    pass

  def finalize_options(self):
    """Post-process options."""
    pass

  def run(self):
    """Run command."""
    with open('./requirements.txt', 'w') as f:
        for req in REQUIRED_PACKAGES:
            f.write(req)
            f.write('\n')



setuptools.setup(
    cmdclass={
        'make_reqs': MakeReqsCommand
    },

    # Package details
    name="jump_reward_inference",
    version="0.0.8",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,

    # Metadata to display on PyPI
    author="Mojtaba Heydari",
    author_email="mheydari@ur.rochester.edu",
    description="A package for fast real-time music joint rhythmic parameters tracking including beats, downbeats, tempo and meter using the BeatNet AI, a super compact 1D state space and the jump back reward technique",
    keywords="Beat tracking, Downbeat tracking, meter detection, tempo tracking, 1D state space, jump reward technique, efficient state space, ",
    url="https://github.com/mjhydri/1D-StateSpace"


    # CLI - not developed yet
    #entry_points = {
    #    'console_scripts': ['beatnet=beatnet.cli:main']
    #}
)
