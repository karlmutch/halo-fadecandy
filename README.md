# Poke Halo - fadecandy server

## Description

Config and deployment for Fadecandy server (running on as Raspberry PI)

## Prerequisites
Trying to use Salt with a Raspberry PI is a fools errand. Therefore there will be a little bit of manual setup required:

#### 1.Install supervisor
##### 2. Create an empty folder in /etc called supervisord - this is because our velcro script assumes supervisor is installed here.
#### 3. Create a symlink to /etc/supervisor/supervisor.conf in this new folder
#### 4. Recreate the standard Poke folder structures:
/poke/software/
/poke/data/app/poke/halo/
/poke/data/conf/supervisord/

### 1. Checkout fadecandy repo

Checkout the repo from

https://github.com/pokelondon/fadecandy to the /poke/software/ folder on the pi (i.e. into a folder with path /poke/software/fadecandy/)

# Developers

 * Jamie Ingram
