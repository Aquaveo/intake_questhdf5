from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

# from .xyHdf5_dataframe import XYHdf5Source_dataframe
# from .xyHdf5_dict import XYHdf5Source_dict
# from .xyHdf5_json import XYHdf5Source_json
#
# from .timeseries_hdf5_dataframe import tsHdf5Source_dataframe
# from .timeseries_hdf5_dict import tsHdf5Source_dict
# from .timeseries_hdf5_json import tsHdf5Source_json

from .xyHdf5 import XYHdf5Source
from .timeseries_hdf5 import tsHdf5Source