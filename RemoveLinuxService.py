#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

if len(sys.argv) != 2:
	print 'Número de argumentos incorrecto. Sólo hace el nombre del servicio (<Nombre del ejecutable sin terminacion>.service)'
	quit()

servicePath = '/etc/systemd/system/'
serviceName = sys.argv[1];
serviceFilePath = servicePath + serviceName

print 'El path del servicio es', serviceFilePath

print 'Deshabilitando servicio'

from subprocess import call
call(["systemctl", "disable", serviceName])

print 'Eliminando el .service'

os.remove(serviceFilePath)

print 'Relaod de daemons'

call(["systemctl", "daemon-reload"])
