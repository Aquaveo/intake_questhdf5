from .base import quest_hdf5_base
import json
# from . import __version__


class XYHdf5Source(quest_hdf5_base):
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
    name = 'quest_xyHdf5'
    container = 'dataframe'
    #version = __version__
    version = '0.0.1'
    partition_access = False
    tablename = 'dataframe'

    def __init__(self, path, fmt=None, metadata=None):
        # store important kwargs
        self.path = path
        self.fmt = fmt

        if self.fmt is None or self.fmt.lower() == 'dataframe':
            self.container = 'dataframe'
        elif self.fmt.lower() == 'dict':
            self.container = 'dict'
        elif self.fmt.lower() == 'json':
            self.container = 'dict'
        else:
            raise NotImplementedError('format %s not recognized' % self.fmt)

        super(XYHdf5Source, self).__init__(metadata=metadata)

    def _get_partition(self, _):
        dataframe = self.get_dataframe(self.path, self.tablename)

        if self.fmt is None or self.fmt.lower() == 'dataframe':
            return dataframe

        # # convert index to datetime in case it is a PeriodIndex
        # dataframe.index = dataframe.index.to_datetime()
        jstr = json.loads(dataframe.to_json())
        d = dict()
        d['data'] = {k: sorted(v.items()) for k, v in jstr.items()}
        d['metadata'] = dataframe.metadata

        if self.fmt.lower() == 'dict':
            return d

        if self.fmt.lower() == 'json':
            return json.dumps(d)

        raise NotImplementedError('format %s not recognized' % self.fmt)

    def _close(self):
        pass
