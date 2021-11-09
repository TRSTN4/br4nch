# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.builder.header import build_header
from br4nch.utility.unpacker import unpack_paint_clear
from br4nch.utility.librarian import paint_branch
from br4nch.utility.painter import painter


def build_branch(branch, colors=True):
    if colors:
        paint_clear = unpack_paint_clear(branch)
        branch_paint = paint_clear
    else:
        paint_clear = ""
        branch_paint = ""

    if paint_branch[branch] and colors:
        branch_paint = painter(paint_branch[branch], branch)
    else:
        branch_paint = ""

    build_header(branch, branch_paint, colors)
