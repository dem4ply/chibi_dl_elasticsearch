from chibi_dl.site.nhentai import Episode as Episode_base
from chibi_dl_elasticsearch.models.nhentai import Manga


class Episode( Episode_base ):
    def to_es( self ):
        if not Manga.url_is_scaned( self.url ):
            model = Manga( **self.metadata )
            model.save()
