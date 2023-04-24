from pynse.pynse import get_nse_advances_declines


def test_get_nse_advances_declines():
    adv_dec = get_nse_advances_declines()
    assert adv_dec is not None
    assert adv_dec["advances"] is not None
    assert adv_dec["declines"] is not None
    assert adv_dec["unchanged"] is not None
    assert adv_dec["total"] is not None
    assert adv_dec["datetime"] is not None
