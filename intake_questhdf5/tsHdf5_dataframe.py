from .base import quest_hdf5_base
# from . import __version__


class tsHdf5Source_dataframe(quest_hdf5_base):
    """Reads an XY HDF5 table into a dataframe

    Parameters
    ----------
    path: str
        File to load.
    tablename: str
        Name of table to load.
    metadata:
        Arbitrary information to associate with this source.

    """
    name = 'quest_tsHdf5_dataframe'
    container = 'dataframe'
    #version = __version__
    version = '0.0.1'
    partition_access = False

    def __init__(self, path, tablename='dataframe', metadata=None):
        # store important kwargs
        self.path = path
        self.tablename = tablename
        super(tsHdf5Source_dataframe, self).__init__(metadata=metadata)

    def _get_partition(self, _):
        return self.get_dataframe(self.path, self.tablename)

    def _close(self):
        pass
