from os import listdir
from os.path import isfile, join
__all__ = [f[:-3] for f in listdir("./responses") if isfile(join("./responses", f)) and f[-3:] == ".py" and f[:2] !=  "__" and f[:-3] != "BaseResponse"]
