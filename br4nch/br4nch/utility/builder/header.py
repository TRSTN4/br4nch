# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.builder.layer import configure
from br4nch.utility.unpacker import unpack_paint_builder
from br4nch.utility.unpacker import unpack_paint_clear
from br4nch.utility.librarian import branches, output, paint_header
from br4nch.utility.painter import painter


def build_header(branch, paint_branch, colors):
    if colors:
        paint_clear = unpack_paint_clear(branch)
        header_paint = paint_clear
    else:
        paint_clear = ""
        header_paint = ""

    if branches[branch]:
        header = list(branches[branch].keys())[0]

        if paint_header[branch] and colors:
            header_paint = painter(paint_header[branch], branch)
        else:
            header_paint = ""

        output[branch].append(paint_clear + header_paint + header + paint_clear + paint_branch + paint_clear)

        configure(branch, paint_branch, colors)
