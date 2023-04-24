from pynse.constants import URLS
from pynse.request_utils import request_nse_csv


def get_all_indices():
    """Get all indices from NSE website.

    Returns:
        list: List of all indices.
    """
    index_df = request_nse_csv(URLS.NSE_URLS.INDICES_CSV)
    return index_df["INDEX \n"].tolist()


def get_all_indices_data():
    """Get all indices data from NSE website.

    Returns:
        DataFrame: Dataframe with all indices data.
    """
    index_df = request_nse_csv(URLS.NSE_URLS.INDICES_CSV)
    index_df.columns = index_df.columns.str.replace(" \n", "")
    return index_df