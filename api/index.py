import sys
import os

# Add the project root to the python search path to import backend modules
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from backend.app import app

class PrefixMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        path_info = environ.get('PATH_INFO', '')
        
        # Strip '/_/backend' prefix if present
        if path_info.startswith('/_/backend'):
            environ['PATH_INFO'] = path_info[len('/_/backend'):] or '/'
        # Strip '/api' prefix if present
        elif path_info.startswith('/api'):
            environ['PATH_INFO'] = path_info[len('/api'):] or '/'
            
        return self.app(environ, start_response)

# Apply the middleware so Flask routes match without prefixes
app.wsgi_app = PrefixMiddleware(app.wsgi_app)
