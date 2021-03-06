#!/usr/bin/env python3
import logging
from errno import ENOENT, EIO
from stat import S_IFDIR, S_IFLNK, S_IFREG
from sys import argv, exit
from time import time
import subprocess
from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
from fuse_3ds.romfs import *
class RomFS(RomFSBase):
    def __init__(self,fname,mount):
        f=open(fname,"rb")
        super(RomFS, self).__init__(f, mount)

if len(argv) != 3:
    print("usage: {name} <ROMFS> <mountpoint>".format(name=argv[0]))
    exit(1)
logging.basicConfig(level=logging.WARNING)
fuse = FUSE(RomFS(argv[1], argv[2]),argv[2], foreground=False)
