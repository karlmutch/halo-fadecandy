import os
from fabric.state import output

from velcro.decorators import pre_hooks, post_hooks
from velcro.service.supervisord import list_programs, start, stop, restart
from velcro.scm.git import deploy as _deploy

# Silence Output
output['running'] = False

# Project Details
env.client = 'poke'
env.project = 'halo'

env.local_path = os.path.abspath(os.path.dirname(__file__))

# Paths & Directories
env.root_path = '/poke/data/app/'
env.directories = {
    'logs': None, 'config': None,
}

# Users
env.user = 'poke'
env.sudo_user = 'root'

# Version Control
env.scm = 'git'

# Hosts to deploy too
env.hosts = [
    '10.193.15.59',
]

# Config path
env.config_path_pipeline = [
    'config',
]

# Supervisord Configs
env.supervisord_config_dir = '/poke/data/conf/supervisord/'
env.supervisord_configs = [
    'supervisord.conf',
]


@post_hooks(
    'velcro.scm.git.clean',
    'velcro.service.supervisord.symlink',
    'service.supervisord.reread',
)
def deploy(branch, **kwargs):
    _deploy(branch)
