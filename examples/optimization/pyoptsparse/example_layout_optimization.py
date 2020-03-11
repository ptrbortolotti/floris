# Copyright 2020 NREL

# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import numpy as np
import matplotlib.pyplot as plt
import os

import floris.tools as wfct
import floris.tools.optimization.pyoptsparse as opt

# Initialize the FLORIS interface fi
file_dir = os.path.dirname(os.path.abspath(__file__))
fi = wfct.floris_interface.FlorisInterface(
    os.path.join(file_dir, '../../example_input.json')
)

boundaries = [[0., 0.], [0., 1000.], [1000., 1000.], [1000., 0.]]

# wd = np.arange(0., 360., 60.)
wd = [270]
np.random.seed(1)
ws = 8.0 + np.random.randn(len(wd))*0.5
freq = np.abs(np.sort(np.random.randn(len(wd))))
freq = freq/freq.sum()

model = opt.layout.Layout(fi, boundaries, wdir=wd,
                                          wspd=ws,
                                          wfreq=freq)

tmp = opt.optimization.Optimization(model=model, solver='SLSQP')

sol = tmp.optimize()

print(sol)

model.plot_layout_opt_results(sol)
plt.show()