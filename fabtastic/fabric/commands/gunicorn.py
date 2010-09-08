from fabric.api import *
from fabtastic.fabric.util import _current_host_has_role

def reload_gunicorn():
    """
    Reloads gunicorn. This must be done to re-compile the code after a new
    revision has been checked out.
    """
    if _current_host_has_role('webapp_servers'):
        print("=== RESTARTING GUNICORN WEBAPP NODE ===")
        run('killall gunicorn')