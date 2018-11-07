import json
from .base import quest_hdf5_base
# from . import __version__


class XYHdf5Source_dict(quest_hdf5_base):
    """Reads an XY HDF5 table into a dictionary

    Parameters
    ----------
    path: str
        File to load.
    tablename: str
        Name of table to load.
    metadata:
        Arbitrary information to associate with this source.

    """
    name = 'quest_xyHdf5_dict'
    container = 'dict'
    # version = __version__
    version = '0.0.1'
    partition_access = False

    def __init__(self, path, tablename='dataframe', metadata=None):
        # store important kwargs
        self.path = path
        self.tablename = tablename
        super(XYHdf5Source_dict, self).__init__(metadata=metadata)

    def _get_partition(self, _):
        dataframe = self.get_dataframe(self.path, self.tablename)

        # # convert index to datetime in case it is a PeriodIndex
        # dataframe.index = dataframe.index.to_datetime()
        jstr = json.loads(dataframe.to_json())
        d = dict()
        d['data'] = {k: sorted(v.items()) for k, v in jstr.items()}
        d['metadata'] = dataframe.metadata

        return d

    def _close(self):
        pass
