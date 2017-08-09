import pytest
import samosa


# @pytest.mark.parametrize("test_file", [
#     ('Kimi.no.na.wa.aka.Your.Name.2016.JAPANESE.1080p.BluRay.REMUX.AVC.DTS-HD.MA.5.1-FGT.mkv'),
#     ('Looney.Tunes.Volume.2.1936-1959.1080p.BluRay.REMUX.AVC.DD1.0-RARBG.mkv'),
#     ('The.Princess.And.The.Frog.2009.1080p.BluRay.AVC.DTS-HD.MA.5.1-FGT.avi'),
# ])

def test_find_only_mkv_files():
    file_list = samosa.find_all_media_files()
    assert len(file_list) is 2
