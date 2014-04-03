#!/usr/bin/env python
from __future__ import with_statement
from fabric.api import *
from fabric.api import local, settings, abort, run, cd, env
from fabric.contrib.console import confirm
from contextlib import contextmanager as _contextmanager
import os


# glogal env
env.warn_only = True
env.supervisor = '/etc/supervisor/conf.d'
env.nginx = '/etc/nginx/sites-enabled'


"""
Definition instances
"""
def dev_strobelpr_ch():
    env.site_id = 'strobel-pr.ch'
    env.hosts = ['78.46.180.50']
    env.git_url = 'http://stash.netzbarkeit.ch/scm/DJANGOCMS/strobel-pr.git'
    env.git_branch = 'master'
    env.path = '/var/www/strobel-pr.ch'
    env.storage = '/storage/django_data/strobel-pr.ch'
    env.user = 'root'
    env.directory = '/srv/strobel-pr.ch/'
    env.activate = 'source /srv/strobel-pr.ch/bin/activate'


def live_strobelpr_ch():
    env.site_id = 'strobel-pr.ch'
    env.hosts = ['78.46.180.48']
    env.git_url = 'http://stash.netzbarkeit.ch/scm/DJANGOCMS/strobel-pr.git'
    env.git_branch = 'master'
    env.path = '/var/www/strobel-pr.ch'
    env.storage = '/storage/django_data/strobel-pr.ch'
    env.user = 'root'
    env.directory = '/srv/strobel-pr.ch/'
    env.activate = 'source /srv/strobel-pr.ch/bin/activate'


@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield 


def deploy():

    try:
        run('mkdir -p %s' % env.path)
    except Exception, e:
        print 'path exists: %s' % env.path
        pass
    
    
    """
    """
    with cd(env.path):  
        
        """
        remove old config
        """
        try:
            run('rm -r config')
        except Exception, e:
            pass
        
        """
        create directory to save the local_config (settings / sqlite3.db)
        """
        try:
            run('mkdir -p config')
        except Exception, e:
            pass
        
        try:
            run('cp src/website/local_settings.py config/')  
        except Exception, e:
            pass
        
        try:
            run('cp src/website/*.db config/')  
        except Exception, e:
            pass
        
        """
        recreate src directory
        """    
        try:
            run('rm -Rf src')
        except Exception, e:
            pass
        
        run('mkdir src')

        
    with cd(env.path + '/src'):
        
        """
        aquire code from repository and move files
        """
        run('git init')
        run('git remote add -t %s -f origin %s' % (env.git_branch, env.git_url))
        run('git checkout %s' % (env.git_branch))
        
    with cd(env.path): 

        """
        copy back the local_settings
        """
        try:
            run('cp config/local_settings.py src/website/')
        except Exception, e:
            pass
        
        try:
            run('cp config/*.db src/website/')
        except Exception, e:
            pass
    
    with virtualenv():
        run('pip freeze')
        run('pip install -r %s/src/website/requirements/requirements.txt' % env.path)
        
    with cd(env.path):
        """
        migrations
        """
        try:
            run('python %s/src/website/manage.py migrate' % env.path)
        except Exception, e:
            pass

        """
        creating files folders
        """
        try:
            run('mkdir -p %s/media' % env.storage)
            run('mkdir -p %s/static' % env.storage)
            #run('mkdir -p %s/site-static' % env.storage)
        except Exception, e:
            pass
            
        """
        linking storage directories
        """
        try:
            run('ln -s %s/media %s/src/website/media' % (env.storage, env.path))
            run('ln -s %s/static %s/src/website/static' % (env.storage, env.path))
            #run('ln -s %s/site-static %s/src/website/site-static' % (env.storage, env.path))
        except Exception, e:
            pass
        
        """
        linking config files
        """
        try:
            run('rm %s/%s.conf' % (env.supervisor, env.site_id))
            run('ln -s %s/src/conf/%s.supervised.conf %s/%s.conf' % (env.path, env.site_id, env.supervisor, env.site_id))
        except Exception, e:
            pass
        
        try:
            run('rm %s/%s' % (env.nginx, env.site_id))
            run('ln -s %s/src/conf/%s.nginx.conf %s/%s' % (env.path, env.site_id, env.nginx, env.site_id))
        except Exception, e:
            pass
        
        """
        (re)start gunicorn worker
        """
        try:
            run('supervisorctl reread')
        except Exception, e:
            pass
        
        try:
            run('supervisorctl restart %s' % env.site_id)
            run('supervisorctl status')
        except Exception, e:
            pass
        
