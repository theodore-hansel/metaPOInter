#!/usr/bin/env python
from pointer import FitFFParameters as Fit

settings = {}
settings['mon1'] = 'methane'
settings['mon2'] = 'methane'
settings['drude_method'] = 'read'
settings['drude_read_file'] = 'input/edrudes.dat'
settings['constraint_files'] = ['optimized_params.constraints']
settings['constrained_atomtypes'] = ['C', 'H']

settings_files = ['default']


Fit(settings_files,**settings)

