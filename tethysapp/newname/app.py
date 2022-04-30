from tethys_sdk.base import TethysAppBase, url_map_maker


class Newname(TethysAppBase):
    """
    Tethys app class for  my First APP.
    """

    name = ' my First APP'
    index = 'newname:home'
    icon = 'newname/images/icon.gif'
    package = 'newname'
    root_url = 'newname'
    color = '#8e44ad'
    description = 'Description'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='newname',
                controller='newname.controllers.home'
            ),
        )

        return url_maps