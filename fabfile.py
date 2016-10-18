import os
from fabric.api import env, run
from fabric.state import output

from velcro.env import bootstrap as _bootstrap
from velcro.decorators import pre_hooks, post_hooks
from velcro.target import live, stage
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
    'logs': None, 'config': None, 'src': None,
}

# Users
env.user = 'poke'
env.sudo_user = 'root'

# Version Control
env.scm = 'git'

# Hosts to deploy too
env.hosts = [
    'pokehalo',
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
    'velcro.service.supervisord.symlink',
)
def bootstrap():
    _bootstrap()


@post_hooks(
    'velcro.scm.git.clean',
    'velcro.service.supervisord.symlink',
    'service.supervisord.reread',
)
def deploy(branch, **kwargs):
    _deploy(branch)
