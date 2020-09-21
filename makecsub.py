#!/usr/bin/env python
##
# Copyright 2009-2020 Ghent University
#
# This file is part of csub,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Flemish Research Foundation (http://www.fwo.be/en),
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/csub
#
# csub is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 2 of
# the License, or (at your option) any later version.
#
# csub is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with csub. If not, see <http://www.gnu.org/licenses/>.
#
#
# make csub from adding the base.sh and epilogue.sh script to csub.py

import os
import re

with open('epilogue.sh', 'r') as fh:
    epi = fh.read()

with open('base.sh', 'r') as fh:
    base = fh.read()

with open('csub.py', 'r') as fh:
    csub = fh.read()

regepi = re.compile(r"^EPILOGUE\s*=.*", re.M)
regbase = re.compile(r"^BASE\s*=.*", re.M)

csub = regepi.sub('EPILOGUE="""' + epi + "\n" + '"""', csub)
csub = regbase.sub('BASE="""' + base + "\n" + '"""', csub)

with open('csub', 'w') as fh:
    fh.write(csub)
os.chmod('csub', 0o755)
