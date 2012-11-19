#
#    Copyright Phyushin 2012 Pi Baker (mac) V0.8
#  
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#!/usr/bin/python


import os;

class mac_baker:
    def __init__(self):
        title='';        
    def shell_call(self ,value):
        sts =os.system(value);
        
    def print_title(self):   
        title  ="""
 888888ba  oo     888888ba           dP                         
 88    `8b        88    `8b          88                         
a88aaaa8P' dP    a88aaaa8P' .d8888b. 88  .dP  .d8888b. 88d888b. 
 88        88     88   `8b. 88'  `88 88888"   88ooood8 88'  `88 
 88        88     88    .88 88.  .88 88  `8b. 88.  ... 88       
 dP        dP     88888888P `88888P8 dP   `YP `88888P' dP       
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
******************************************by Phyushin***********
     """ 
        print title;
    def baking(self):
        message = """
888888b.            888      d8b                   
888  "88b           888      Y8P                   
888  .88P           888                            
8888888K.   8888b.  888  888 888 88888b.   .d88b.  
888  "Y88b     "88b 888 .88P 888 888 "88b d88P"88b 
888    888 .d888888 888888K  888 888  888 888  888 
888   d88P 888  888 888 "88b 888 888  888 Y88b 888 
8888888P"  "Y888888 888  888 888 888  888  "Y88888 
                                               888 
                                          Y8b d88P 
                                           "Y88P
                        This Could Take A While...
                                           """
        print message;
b = mac_baker();
b.shell_call('clear');
b.print_title();
print('-------------------------------------');
print('do you need to unzip the file?');
un_zip = raw_input();
if (un_zip <> 'n'):
    print('Please enter the location of the zip');
    zip_loc = raw_input();
    print('-------------------------------------');
    print('ShaSum:');
    print('-------------------------------------');
    b.shell_call('shasum ' + zip_loc);
    print('Unzipping');
    b.shell_call('unzip '+ zip_loc);
b.shell_call('clear');
b.print_title;
print('-------------------------------------');
b.shell_call('ls');
print('-------------------------------------');
b.shell_call('df -h');
print('-------------------------------------');
print('Select SD card location(the /dev/ part isn'' needed):');
sd_card_location = '/dev/' + raw_input();
print('you entered: ') + sd_card_location + (' is this correct?');

choice = raw_input();
if choice ==('y'):
    print('enter SD location like this (/dev/r(disknumber) for '+ sd_card_location);
    sd_card = raw_input();
    print('unmounting '+sd_card_location);
    print('where is the img?');
    img_path = raw_input();
    b.shell_call('sudo diskutil unmount '+sd_card_location);
    b.shell_call('clear');
    b.baking();
    b.shell_call('sudo dd bs=1m if='+ img_path+' of=/dev/'+sd_card)
    b.shell_call('sudo diskutil eject '+ sd_card )


