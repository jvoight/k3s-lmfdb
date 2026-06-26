#!/usr/bin/env -S sage -python

import argparse
from genus import write_all_of_sig_between_genera_basic

parser = argparse.ArgumentParser("run_all", description="Run the whole pipeline for generating lattice data")
parser.add_argument("-n", "--rank-limit", type=int, default=32, description="Upper bound on rank")
parser.add_argument("-d", "--disc-ratio-limit", type=int, default=32768, description="Enumerate genera of discriminant up to d/n")
parser.add_argument("-k", "--nok3", action="store_true", description="By default, we also enumerate genera of discriminant up to d/(22-n) for nminus=1 or 2.  This option turns that off")
parser.add_argument("--enum-masslimit", type=int, default=1000, description="If the mass of a genus is larger than this threshold, don't even try to enumerate lattices within")
parser.add_argument("--enum-timelimit", type=int, default=300, description="Maximum number of seconds to spend on enumerating a genus") # TODO: calibrate this based on how much time we want to spend
parser.add_argument("--enum-sizelimit", type=int, default=1000, description="For genera with class number larger than this, do not store individual lattices within the genus")

args = parser.parse_args()

