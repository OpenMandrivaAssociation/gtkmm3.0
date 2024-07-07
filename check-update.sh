#!/bin/sh
curl -s https://download.gnome.org/sources/gtkmm/3.24/ |grep LATEST |sed -e 's,.*LATEST-IS-,,;s,<.*,,'
