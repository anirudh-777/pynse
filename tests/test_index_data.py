from pynse.indices import get_all_indices, get_all_indices_data


def test_get_all_indices():
    all_indices = get_all_indices()
    assert all_indices is not None
    assert len(all_indices) > 0
    assert "NIFTY 50" in all_indices
    assert "NIFTY NEXT 50" in all_indices
    assert "NIFTY MIDCAP 50" in all_indices
    assert "NIFTY MIDCAP 100" in all_indices


def test_get_all_indices_data():
    index_df = get_all_indices_data()
    assert index_df is not None
    assert index_df.shape[0] > 0
    assert "INDEX" in index_df.columns
    assert "CURRENT" in index_df.columns
    assert "NIFTY 50" in index_df["INDEX"].tolist()
    assert "NIFTY NEXT 50" in index_df["INDEX"].tolist()
