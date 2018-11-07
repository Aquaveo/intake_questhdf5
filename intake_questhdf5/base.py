from intake.source.base import DataSource, Schema
import warnings
# from . import __version__

class quest_hdf5_base(DataSource):
    """Reads an HDF5 table

    Parameters
    ----------
    path: str
        File to load.
    tablename: str
        Name of table to load.
    metadata:
        Arbitrary information to associate with this source.

    """
    #version = __version__
    version = '0.0.1'
    container = 'dataframe'
    partition_access = False

    def setattr_on_dataframe(self, df, attr, value, warnings_filter='ignore'):
        with warnings.catch_warnings():
            warnings.simplefilter(warnings_filter)
            setattr(df, attr, value)

    def get_dataframe(self, path, tablename):
        import pandas as pd

        with pd.HDFStore(path) as h5store:
            dataframe = h5store.get(tablename)
            self.setattr_on_dataframe(dataframe, 'metadata', h5store.get_storer(tablename).attrs.metadata)
        return dataframe

    def _get_schema(self):
        import pandas as pd

        self._dtypes = {}
        with pd.HDFStore(self.path) as h5store:
            for key in h5store:
                try:
                    # column names of table store
                    self._dtypes = h5store.get_node('{}/table'.format(key)).description._v_types
                except AttributeError:
                    try:
                        # column names of fixed store
                        self._dtypes = list(h5store.get_node('{}/axis0'.format(key)).read().astype(str))
                    except AttributeError:
                        # e.g. a dataset created by h5py instead of pandas.
                        print('unknown node in HDF.')

        return Schema(
            datashape=None,
            dtype=self._dtypes,
            shape=(None, len(self._dtypes)),
            npartitions=1,  # This data is not partitioned, so there is only one partition
            extra_metadata={}
        )

    def _get_partition(self, _):
        return self.get_dataframe(self.path, self.tablename)

    def _close(self):
        pass
