#data1 = str(sys.argv[1])
#data2 = str(sys.argv[2])
#data3 = str(sys.argv[3])
#data4 = str(sys.argv[4])
#if(MAX_dbg==1):print ( data1 )
#if(MAX_dbg==1):print ( data2 )
#if(MAX_dbg==1):print ( data3 )
#if(MAX_dbg==1):print ( data4 )


import time
import MAXIOT
import MEDIATOR
import commands
import fifo
SYS_dbg = 1

try:
	print "\n\n\n"
	if(SYS_dbg==1):print "###################################"
	if(SYS_dbg==1):print "... SYS : SYSTEM START !!!"
	if(SYS_dbg==1):print "###################################"
	fifo.init()
	########################
	MEDIATOR.START()
	time.sleep(0.2)
	########################
	MAXIOT.reconnect		   =  1
	#MAXIOT.Server_IP          = "10.0.0.13"
	MAXIOT.Server_IP          =  commands.getoutput("hostname -I")
	MAXIOT.Server_PORT        =  3004
	MAXIOT.DEVICE_NAME        = "9002"
	MAXIOT.DEVICE_DESCRIPTION = "LCD ILI9341"
	MAXIOT.START()
	########################
	while 1:
		time.sleep(0.001)
		####################################################
		
		if(MAXIOT.reconnect==1):
			if(MAXIOT.CLIENT_STATUS==0):
				time.sleep(1)
				print "... MAX : [#      ]"
				time.sleep(1)
				print "... MAX : [##     ]"
				time.sleep(1)
				print "... MAX : [###    ]"
				time.sleep(1)
				print "... MAX : [####   ]"	
				time.sleep(1)
				print "... MAX : [#####  ]"
				time.sleep(1)
				print "... MAX : [###### ]"
				time.sleep(1)
				print "... MAX : [#######]"
				print "###################################"
				print "... MAX : RECONNECTING !!!"
				MAXIOT.START()
	
		####################################################
		
#		while(fifo.Len()):
#			d = fifo.Get()
#			print "... LCD : " + str(d)
#			MEDIATOR.Text(d)

		####################################################	

finally:
	if(SYS_dbg==1):print "###################################"
	if(SYS_dbg==1):print "... MAX : SYSTEM STOP !!!"
	if(SYS_dbg==1):print "###################################"
	MAXIOT.CLIENT_STATUS     = 0
	MAXIOT.PING_STATUS       = 0
	MEDIATOR.USER_STATUS     = 0
	MEDIATOR.MEM_USER_STATUS = 0
















