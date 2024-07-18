"""
A plugin to connect to the scryfall api from CKAN.
"""

import logging
from ckan import plugins
from ckan.types import Any, Context, DataDict
from ckan.plugins import toolkit


class ScryfallPlugin(plugins.SingletonPlugin):
    """Class ScryfallPlugin implements IResourceView"""

    plugins.implements(plugins.IResourceView)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(self, *args, **kwargs)
        self.__log = logging.getLogger(__name__)

    # Add custom view renderings for different resource types.
    def info(self) -> dict[str, Any]:
        """Returns a dictionary with configuration options for the Scryfall Plugin."""
        scryfall_config = {
            "name": "scryfall",
            "title": toolkit._("Scryfall Viewer"),
            "default_title": toolkit._("Scryfall View"),
            "default_description": toolkit._(
                "This is a viewer to the Magic The Gathering Scryfall public API."
            ),
            "icon": "magic",
            "always_available": False,
            "iframed": True,
            "preview_enabled": False,
            "full_page_edit": False,
        }

        return scryfall_config

    def can_view(self, data_dict: DataDict) -> bool:
        """
        Returns whether the plugin can render a particular resource.

        The ``data_dict`` contains the following keys:

        :param resource: dict of the resource fields
        :param package: dict of the full parent dataset

        :returns: True if the plugin can render a particular resource, False
            otherwise
        :rtype: bool
        """

        def is_scryfall() -> bool:
            """Check if a data dictionary is in the scryfall format. And do input validation"""
            resource = None
            resource_format = ""
            try:
                if "resource" in data_dict.keys():
                    resource = data_dict["resource"]
                    if "format" in resource.keys():
                        resource_format = data_dict["resource"]
            except AttributeError as e:
                # Can throw if the wrong data type is sent in as data_dict.
                self.__log.exception(e)
                return False

            return resource_format == "scryfall"

        return is_scryfall()

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
        return {}

    def view_template(self, context: Context, data_dict: DataDict) -> str:
        """
        Returns a string representing the location of the template to be
        rendered when the view is displayed

        The path will be relative to the template directory you registered
        using the :py:func:`~ckan.plugins.toolkit.add_template_directory`
        on the :py:class:`~ckan.plugins.interfaces.IConfigurer.update_config`
        method, for instance ``views/my_view.html``.

        :param resource_view: dict of the resource view being rendered
        :param resource: dict of the parent resource fields
        :param package: dict of the full parent dataset

        :returns: the location of the view template.
        :rtype: string
        """
        return ""

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
