# TODO add MP4

tags_conversion = {
    "flac": {
        "album": {"ALBUM"},
        "albumsort": {"ALBUMSORT"},
        "title": {"TITLE"},
        "titlesort": {"TITLESORT"},
        "work": {"WORK"},
        "artist": {"ARTIST"},
        "artistsort": {"ARTISTSORT"},
        "albumartist": {"ALBUMARTIST"},
        "albumartistsort": {"ALBUMARTISTSORT"},
        "date": {"DATE"},
        "originaldate": {"ORIGINALDATE"},
        "originalyear": {"ORIGINALYEAR"},
        "composer": {"COMPOSER"},
        "composersort": {"COMPOSERSORT"},
        "lyricist": {"LYRICIST"},
        "writer": {"WRITER"},
        "conductor": {"CONDUCTOR"},
        "performer-instrument": {"PERFORMER"},
        "remixer": {"REMIXER"},
        "arranger": {"ARRANGER"},
        "engineer": {"ENGINEER"},
        "producer": {"PRODUCER"},
        "djmixer": {"DJMIXER"},
        "mixer": {"MIXER"},
        "label": {"LABEL"},
        "grouping": {"GROUPING"},
        "subtitle": {"SUBTITLE"},
        "discsubtitle": {"DISCSUBTITLE"},
        "tracknumber": {"TRACKNUMBER"},
        "totaltracks": {"TRACKTOTAL", "TOTALTRACKS"},
        "discnumber": {"DISCNUMBER"},
        "totaldiscs": {"DISCTOTAL", "TOTALDISCS"},
        "compilation": {"COMPILATION"},
        "comment-description": {"COMMENT"},
        "genre": {"GENRE"},
        "_rating": {"RATING:user@email"},
        "bpm": {"BPM"},
        "mood": {"MOOD"},
        "lyrics-description": {"LYRICS"},
        "media": {"MEDIA"},
        "catalognumber": {"CATALOGNUMBER"},
        # "show": set(),
        # "showsort": set(),
        # "podcast": set(),
        # "podcasturl": set(),
        "releasestatus": {"RELEASESTATUS"},
        "releasetype": {"RELEASETYPE"},
        "releasecountry": {"RELEASECOUNTRY"},
        "script": {"SCRIPT"},
        "language": {"LANGUAGE"},
        "copyright": {"COPYRIGHT"},
        "license": {"LICENSE"},
        "encodedby": {"ENCODEDBY"},
        "encodersettings": {"ENCODERSETTINGS"},
        "gapless": set(),
        "barcode": {"BARCODE"},
        "isrc": {"ISRC"},
        "asin": {"ASIN"},
        "musicbrainz_recordingid": {"MUSICBRAINZ_TRACKID"},
        "musicbrainz_trackid": {"MUSICBRAINZ_RELEASETRACKID"},
        "musicbrainz_albumid": {"MUSICBRAINZ_ALBUMID"},
        "musicbrainz_artistid": {"MUSICBRAINZ_ARTISTID"},
        "musicbrainz_albumartistid": {"MUSICBRAINZ_ALBUMARTISTID"},
        "musicbrainz_releasegroupid": {"MUSICBRAINZ_RELEASEGROUPID"},
        "musicbrainz_workid": {"MUSICBRAINZ_WORKID"},
        "musicbrainz_trmid": {"MUSICBRAINZ_TRMID"},
        "musicbrainz_discid": {"MUSICBRAINZ_DISCID"},
        "acoustid_id": {"ACOUSTID_ID"},
        "acoustid_fingerprint": {"ACOUSTID_FINGERPRINT"},
        "musicip_puid": {"MUSICIP_PUID"},
        "musicip_fingerprint": {"FINGERPRINT"},
        "website": {"WEBSITE"},
    },
    'mp3': {
        "album": {"TALB"},
        "albumsort": {"TSOA"},
        "title": {"TIT2"},
        "titlesort": {"TSOT"},
        "work": {"TOAL"},
        "artist": {"TPE1"},
        "artistsort": {"TSOP"},
        "albumartist": {"TPE2"},
        "albumartistsort": {"TSO2", "TXXX:ALBUMARTISTSORT"},
        "date": {"TDRC", "TYER", "TDAT"},
        "originaldate": {"TDOR"},
        "originalyear": {"TORY"},
        "composer": {"TCOM"},
        "composersort": {"TSOC", "TXXX:COMPOSERSORT"},
        "lyricist": {"TEXT"},
        "writer": {"TXXX:Writer"},
        "conductor": {"TPE3"},
        "performer-instrument": {"TMCL:instrument", "IPLS:instrument"},
        "remixer": {"TPE4"},
        "arranger": {"TMCL:arranger", "IPLS:arranger"},
        "engineer": {"TMCL:engineer", "IPLS:engineer"},
        "producer": {"TMCL:producer", "IPLS:producer"},
        "djmixer": {"TMCL:DJ-mix", "IPLS:DJ-mix"},
        "mixer": {"TMCL:mix", "IPLS:mix"},
        "label": {"TPUB"},
        "grouping": {"TIT1"},
        "subtitle": {"TIT3"},
        "discsubtitle": {"TSST"},
        "tracknumber": {"TRCK"},
        "totaltracks": {},
        "discnumber": {"TPOS"},
        "totaldiscs": {},
        "compilation": {"TCMP"},
        "comment-description": {"COMM:description"},
        "genre": {"TCON"},
        "_rating": {"POPM"},
        "bpm": {"TBPM"},
        "mood": {"TMOO"},
        "lyrics-description": {"USLT:description"},
        "media": {"TMED"},
        "catalognumber": {"TXXX:CATALOGNUMBER"},
        # "show": set(),
        # "showsort": set(),
        # "podcast": set(),
        # "podcasturl": set(),
        "releasestatus": {"TXXX:MusicBrainz Album Status"},
        "releasetype": {"TXXX:MusicBrainz Album Type"},
        "releasecountry": {"TXXX:MusicBrainz Album Release Country"},
        "script": {"TXXX:SCRIPT"},
        "language": {"TLAN"},
        "copyright": {"TCPO"},
        "license": {"WCOP", "TXXX:LICENSE"},
        "encodedby": {"TENC"},
        "encodersettings": {"TSSE"},
        "gapless": set(),
        "barcode": {"TXXX:BARCODE"},
        "isrc": {"TSRC"},
        "asin": {"TXXX:ASIN"},
        "musicbrainz_recordingid": {"UFID:http://musicbrainz.org"},
        "musicbrainz_trackid": {"TXXX:MusicBrainz Release Track Id"},
        "musicbrainz_albumid": {"TXXX:MusicBrainz Album Id"},
        "musicbrainz_artistid": {"TXXX:MusicBrainz Artist Id"},
        "musicbrainz_albumartistid": {"TXXX:MusicBrainz Album Artist Id"},
        "musicbrainz_releasegroupid": {"TXXX:MusicBrainz Release Group Id"},
        "musicbrainz_workid": {"TXXX:MusicBrainz Work Id"},
        "musicbrainz_trmid": {"TXXX:MusicBrainz TRM Id"},
        "musicbrainz_discid": {"TXXX:MusicBrainz Disc Id"},
        "acoustid_id": {"TXXX:Acoustid Id"},
        "acoustid_fingerprint": {"TXXX:Acoustid Fingerprint"},
        "musicip_puid": {"TXXX:MusicIP PUID"},
        "musicip_fingerprint": {"TXXX:MusicMagic Fingerprint"},
        "website": {"WOAR"},
    }
}

tags_names = {key for key in tags_conversion["flac"]}
