from MCP230XX import MCP230XX
import time
MCP = MCP230XX('MCP23017', 0x20, '16bit')
MCP.set_mode(1, 'output')
while 1:
    MCP.output(1,1)
    time.sleep(1)
    MCP.output(1,0)
    time.sleep(1)
    

#link for data https://github.com/owainm713/MCP230XX-Python-Module
    
