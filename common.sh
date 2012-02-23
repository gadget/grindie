#
# Copyright 2010 Adam Dobos
#
# This file is part of Grindie.
#
# Grindie is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Grindie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Grindie.  If not, see <http://www.gnu.org/licenses/>.
#

#!/bin/sh

check_ret() {
  last_ret=$?
  if [ "0" -ne "$last_ret" ]
  then
    echo "Exit code: $last_ret"
    exit $last_ret
  fi
}

iterate_over_hosts() {
  callback=$1
  # iterate over unique hosts in settings/scenario.conf
  cat settings/scenario.conf |grep -v '#' |grep -v "^$" |cut -d" " -f1 |sort |uniq |while read host
  do
    $callback $host
  done
}
