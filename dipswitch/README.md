# DIP Switch converter
## Using Tkinter to convert a DMX address to a DIP Switch configuration, with event lighting equipment in mind.

DMX512 (Digital Multiplex 512) is used in lighting control, where a lighting universe contains 512 individually controllable channels. An "intelligent" RGB fixture may require 3 channels of data, so a set of such lights may be addressed at DMZ 001, 004, 007 etc. Many fixtures now have LCD panels for adjusting modes and DMX addressing, while older equipment (lights, hazers) come with DIP Switches. Back in the day when I freelanced as a lighting technician, a DIP switch calculator was often needed during load ins. Except when that one guy was working. He knew these configurations by heart. A true mad lad.

This program converts a DMX address(0-512) to the corresponding DIP Switch configuration with ten switches, with the tenth generally being used as a test channel(512).
The not so secret math behind the switches is decimal - binary, and the combination of 9 switches in ON(1)/OFF(0) positions add up to the value of the DMX address.
```
Switch - Value
Switch 1 – 1
Switch 2 – 2
Switch 3 – 4
Switch 4 – 8
Switch 5 – 16
Switch 6 – 32
Switch 7 – 64
Switch 8 – 128
Switch 9 – 256
Switch 10 - 512 
```
Switches 1-9 each update the address and binary number, and toggling Switch 10 (for testing purposes) resets the values of switches 1-9 to 0.

### GUIs are cute
Toggling the switches (that are secretly scales with the range of 0-1) also changes the binary code and DMX address, which is not a priority of a DMX-switch converter, but it's still nice to know its there, like that box of hot cocoa powder you keep shelved for rainy days but never use.

### QA is trying to break things, then struggling to remember how you broke it.

Entry validation catches DMX addresses that are negative or > 512, and rounds floats down to the nearest integer.
