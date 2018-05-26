#!/bin/sh


die () {
  echo "*** dist_one_proofs/run.sh: $*" 1>&2
  exit 1
}

[ $# =  1 ] || die "argument missing"


msg () {
  echo "[dist_one_proofs/run.sh] $*"
}

run () {
  msg "$*"
  $* || exit 1
}

benchmark=$1
vertex="$1.vtx"
edge="$1.edge"
singular="$1.singular"
pythonlog="$1python.log"
pythonerr="$1python.err"
singularlog="$1singular.log"
singularerr="$1singular.err"

msg "benchmark      $benchmark"
msg "vertex         $vertex"
msg "edge           $edge"
msg "singular       $singular"
msg "pythonlog      $pythonlog"
msg "pythonerr      $pythonerr"
msg "singularlog    $singularlog"
msg "singularerr    $singularerr"

msg "running python to rewrite: '$pythonlog' and '$pythonerr'"
python check_dist_one.py $vertex $edge 1>$pythonlog 2>$pythonerr
msg "encoding done."

msg "running singular: '$singularlog' and '$singularerr'"
Singular $singular 1>$singularlog 2>$singularerr
msg "proof checking done."
