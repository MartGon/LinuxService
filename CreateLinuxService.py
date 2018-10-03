#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

if len(sys.argv) != 2:
	print 'Número de argumentos incorrecto. Sólo hace falta el path realtivo al archivo'
	quit()

execName = os.path.abspath(sys.argv[1])
serviceFileNameSplitted = os.path.relpath(execName, os.path.dirname(os.path.realpath(sys.argv[1]))).split(".")
workingDirectory = execName.replace(sys.argv[1], "")

if len(serviceFileNameSplitted) != 2:
	print 'El archivo no parece tener una terminación válida'
	quit()

print 'El path absoluto del ejectuable es', execName
print 'El working directory es', workingDirectory

servicePath = '/etc/systemd/system/'
serviceName = serviceFileNameSplitted[0] + '.service';

print 'El nombre del servicio es', serviceName

serviceFilePath = servicePath + serviceName

print 'El path del servicio es', serviceFilePath

serviceFile = open(serviceFilePath, "w")

serviceFile.write('[Unit] \nDescription=DroneService \nAfter=network.target')
serviceFile.write('\n[Service] \nExecStart=' + execName + '\nWorkingDirectory=' + workingDirectory)
serviceFile.write('\n[Install] \nWantedBy=multi-user.target \n')

serviceFile.close()

from subprocess import call

print 'Dando permisos de ejecución a', execName
call(["chmod", "+x", execName])

print 'Ejecutando las siguientes lineas'
print 'systemctl enable', serviceName
print 'systemctl daemon-reload'
print 'systemctl start', serviceName

call(["systemctl", "enable", serviceName])
call(["systemctl", "daemon-reload"])
call(["systemctl", "start", serviceName])
