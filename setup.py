# -*- coding: utf-8 -*-
from setuptools import setup
entry_points = (
    """
    [ckan.plugins]
    scryfall=ckanext.wms_viewer.plugin:WmsViewerPlugin
    """,
)
setup(
    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
