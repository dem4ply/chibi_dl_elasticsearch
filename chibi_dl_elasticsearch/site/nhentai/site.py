from chibi_dl.site.nhentai import Nhentai as Nhentai_base
from .episodes import Episode


class Nhentai( Nhentai_base ):
    @property
    def episode_class( self ):
        return Episode
