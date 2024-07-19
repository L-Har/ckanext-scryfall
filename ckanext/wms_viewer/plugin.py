"""
A plugin to connect to the a mapserver api from CKAN.
"""

from urllib.parse import urlparse
import logging
from ckan import plugins
from ckan.types import Any, Context, DataDict
from ckan.plugins import toolkit


class WmsViewerPlugin(plugins.SingletonPlugin):
    """Class WmsViewerPlugin implements IResourceView"""

    plugins.implements(plugins.IResourceView)
    plugins.implements(plugins.IConfigurer)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(self, *args, **kwargs)
        self.__log = logging.getLogger(__name__)

    def update_config(self, config):
        # Add extension templates directory
        toolkit.add_template_directory(config, "templates")

    def update_config_schema(self, schema):
        return schema

    def info(self) -> dict[str, Any]:
        """Returns a dictionary with configuration options for the WmsViewer Plugin."""
        wms_viewer_config = {
            "name": "wms_viewer",
            "title": "WMS " + toolkit._("Viewer"),
            "default_title": "Wms " + toolkit._("View"),
            "default_description": toolkit._(
                "This is a viewer to for mapserver wms files."
            ),
            "icon": "magic",
            "always_available": False,
            "iframed": True,
            "preview_enabled": False,
            "full_page_edit": False,
        }

        return wms_viewer_config

    def can_view(self, data_dict: DataDict) -> bool:
        """
        Returns whether the plugin can render Wms View.
        """

        def is_wms() -> bool:
            """Check if a data dictionary is in the Wms format. And do input validation"""
            resource = None
            resource_format = ""
            try:
                if "resource" in data_dict.keys():
                    resource = data_dict["resource"]
                    if "format" in resource.keys():
                        resource_format = data_dict["resource"]["format"]
            except AttributeError as e:
                # Can throw if the wrong data type is sent in as data_dict.
                self.__log.exception(e)
                return False

            return resource_format == "WMS"

        return is_wms()

    def setup_template_variables(
        self, context: Context, data_dict: DataDict
    ) -> dict[str, Any]:
        """
        Adds variables to be passed to the template being rendered.

        This should return a new dict instead of updating the input
        ``data_dict``.

        The ``data_dict`` contains the following keys:

        :param resource_view: dict of the resource view being rendered
        :param resource: dict of the parent resource fields
        :param package: dict of the full parent dataset

        :returns: a dictionary with the extra variables to pass
        :rtype: dict
        """
        wms_api_link: str = ""

        def check_is_valid() -> bool:
            """Check if a data dictionary has a valid wms_viewer url."""
            resource = None
            url: str = ""
            # Validate the data structure.
            if "resource" in data_dict.keys():
                resource = data_dict["resource"]
                if "url" in resource.keys():
                    url = data_dict["resource"]["url"]

            if url == "":
                raise toolkit.ValidationError(
                    "The url is empty. This resource cannot be viewed."
                )

            # Now Validate url is a valid wms_viewer url.

            # We no longer need url as a string so convert to a dict
            # and reuse the useful variable name "url"
            url: dict = urlparse(url)
            hostname: str = ""
            if hasattr(url, "hostname"):
                hostname = url.hostname
                if hostname == "mapserver.tnris.org":
                    wms_api_link = hostname
                else:
                    raise toolkit.ValidationError("Hostname is not mapserver.tnris.org")

            else:
                raise toolkit.ValidationError("There is no hostname found")

            # If we get this far and wms_api_link is not an empty string the data needs to be valid.
            return wms_api_link != ""

        try:
            if not check_is_valid():
                raise toolkit.ValidationError(
                    "There was a problem validating the url for the wms view"
                )
        except toolkit.ValidationError as e:
            self.__log.exception(str(e))

        return {}

    def view_template(self, context: Context, data_dict: DataDict) -> str:
        """
        Returns a string representing the location of the template to be
        rendered when the view is displayed

        :param resource_view: dict of the resource view being rendered
        :param resource: dict of the parent resource fields
        :param package: dict of the full parent dataset

        :returns: the location of the wms view template.
        :rtype: string
        """

        return "views/wms_template.html"

    def form_template(self, context: Context, data_dict: DataDict) -> str:
        """
        Returns a string representing the location of the template to be
        rendered when the edit view form is displayed

        The path will be relative to the template directory you registered
        using the :py:func:`~ckan.plugins.toolkit.add_template_directory`
        on the :py:class:`~ckan.plugins.interfaces.IConfigurer.update_config`
        method, for instance ``views/my_view_form.html``.

        :param resource_view: dict of the resource view being rendered
        :param resource: dict of the parent resource fields
        :param package: dict of the full parent dataset

        :returns: the location of the edit view form template.
        :rtype: string
        """
        return ""
