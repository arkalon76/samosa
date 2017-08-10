import pytest
import samosa


@pytest.mark.parametrize("test_file,expected", [
    ('Ghost.In.The.Shell.2017.1080p.3D.BluRay.AVC.TrueHD.7.1.Atmos-FGT.mkv', 'tt1219827'),
    ('The.Princess.And.The.Frog.2009.1080p.BluRay.AVC.DTS-HD.MA.5.1-FGT.mkv', 'tt0780521'),
    ('Shot.Caller.2017.1080p.BluRay.REMUX.AVC.TrueHD.5.1-FGT.mkv', 'tt4633690'),
    ('Random.Bullshit.without.year.mkv', None),
    ('.git.filename', None)
])


def test_resolve_imdb_id_from_filename(test_file, expected):
    imdb_id = samosa.resolve_imdb_from_filename(test_file)
    assert imdb_id == expected


@pytest.fixture
def movielist():
    return ['Kimi.no.na.wa.aka.Your.Name.2016.JAPANESE.1080p.BluRay.REMUX.AVC.DTS-HD.MA.5.1-FGT.mkv',
            'Looney.Tunes.Volume.2.1936-1959.1080p.BluRay.REMUX.AVC.DD1.0-RARBG.mp4',
            'The.Princess.And.The.Frog.2009.1080p.BluRay.AVC.DTS-HD.MA.5.1-FGT.avi',
            'MyPresentation.ppt'
            ]


def test_find_only_mkv_files(movielist, tmpdir):
    for movie in movielist:
        f1 = tmpdir.join(movie)
        f1.write('MovieContent')

    file_list = samosa.find_all_media_files(extentions=['.mkv'],
                                            dir_to_search=str(tmpdir))
    assert len(file_list) is 1


def test_find_all_supported_files(movielist, tmpdir):
    for movie in movielist:
        f1 = tmpdir.join(movie)
        f1.write('MovieContent')

    file_list = samosa.find_all_media_files(dir_to_search=str(tmpdir))
    assert len(file_list) is 3
