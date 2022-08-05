# DIP Switch converter
## Using Tkinter to convert a DMX address to a DIP Switch configuration, with event lighting equipment in mind.

DMX512 (Digital Multiplex 512) is used in lighting control, where a lighting universe contains 512 individually controllable channels. An "intelligent" RGB fixture may require 3 channels of data, so a set of such lights may be addressed at DMZ 001, 004, 007 etc. Many fixtures now have LCD panels for adjusting modes and DMX addressing, while older equipment (lights, hazers) come with DIP Switches. Back in the day when I freelanced as a lighting technician, a DIP switch calculator was often needed during load ins. Except when that one guy was working. He knew these configurations by heart. A true mad lad.

This program converts a DMX address(0-512) to the corresponding DIP Switch configuration with ten switches, with the tenth generally being used as a test channel(512).
The not so secret math behind the switches is decimal - binary, and the combination of 9 switches in ON(1)/OFF(0) positions add up to the value of the DMX address.
```
Switch - Value
switch 1 – 1
switch 2 – 2
switch 3 – 4
switch 4 – 8
switch 5 – 16
switch 6 – 32
switch 7 – 64
switch 8 – 128
switch 9 – 256
```
