#!/usr/bin/env python
#
#
# Authors: Rahul ES <esrahulcool@gmail.comd>
# Web : http://brokenbulb.site40.net/blog
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of either or both of the following licenses:
#
# 1) the GNU Lesser General Public License version 3, as published by the
# Free Software Foundation; and/or
# 2) the GNU Lesser General Public License version 2.1, as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the applicable version of the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of both the GNU Lesser General Public
# License version 3 and version 2.1 along with this program.  If not, see
# <http://www.gnu.org/licenses/>
#

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
import re

#predefined brightness values
brightness = ['490' ,'978','1466','1954','2442','2930','3418','3906','4394','4882']
# create menu
menu = Gtk.Menu()

#update menu items to show the selected item
def updateMenu(selected):
  count = 1
  # loop though menu items and mark the currently selected item
  for item in menu.get_children():
    if count == selected:
      temp = '<%d>' % count
    else:
      temp = '  %d  ' % count
    item.set_label(temp)
    count = count + 1

# menu item response
def menuitem_response(w, buf):
  # get the currently selected brightness index, by extracting the number from string
  menuVal = re.findall(r'\d+',buf)
  j = int(menuVal[0])
  # open file and change the brightness value to selected  
  bFile = open("/sys/class/backlight/intel_backlight/brightness",'wb')
  bFile.write(brightness[j-1])
  bFile.close()
  # call function to update the menu, passing currently selected index
  updateMenu(j)
 
if __name__ == "__main__":
  ind = appindicator.Indicator.new (
                        "indicate-brightness",
                        "display-brightness",
                        appindicator.IndicatorCategory.APPLICATION_STATUS)
  ind.set_status (appindicator.IndicatorStatus.ACTIVE)
  ind.set_attention_icon ("display-brightness")
 
  #open file to get read current brightness value
  oFile = open("/sys/class/backlight/intel_backlight/brightness",'r')
  val = int(oFile.read())
  bVal = str(val)
  oFile.close()
 
 
  # create menu items
  for i in range(10):
    if str(brightness[i]) == bVal:
      buf = "<%d>" % (i+1)
    else:
      buf = "  %d  " % (i+1)
    menu_items = Gtk.MenuItem(buf)
 
    menu.append(menu_items)
 
    # connectmenu item up with a function
 
    menu_items.connect("activate", menuitem_response, buf)
 
    # show the items
    menu_items.show()
 
  ind.set_menu(menu)
 
  Gtk.main()