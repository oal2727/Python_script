import paramiko
import os
from getpass import getpass
import sys

#working with protocol ssh 


#ruta=""

 

directorio1=os.getcwd()
print("****************************")
print("Trabajo con el directorio %s" %directorio1)
print("Servicio FTP with python")




def ssh(comand):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(host,port,user,pas)
    entrada,salida,error=ssh.exec_command(comand)
    output=salida.readlines()
    print('\n'.join(output).lstrip("\n"))

def set():
	ssh = paramiko.SSHClient()
	archivo=input("Ingrse el archivo que desea almecenar al servidor : ")
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	ssh.connect(host,port,user,pas)
	sftp_client=ssh.open_sftp()
	if(os.path.isfile(archivo)):
		ruta =input("Ingrese la ruta del archivo donde se almacenara: ")
		try:
			sftp_client.put(archivo, ruta)
			print("->>>>>>Almacenanando archivo en el servidor en la ruta : %s" %ruta )
		except:
			print("Fallo al almacenar en la ruta %s" %ruta)
	else:
		print("El archivo %s no existe " %archivo )
		print("Verifique bien el archivo para poder almacenar al servidor")
	sftp_client.close()
	ssh.close()

def get():
	ssh = paramiko.SSHClient()
	ruta=input("Ingrse la ruta del archivo o archivo que desea obtener: ")
	archivo =input("Ingrese el archivo que desea obtener: ")
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	ssh.connect(host,port,user,pas)
	sftp_client=ssh.open_sftp()
	try:

		sftp_client.get(ruta , archivo)
		print("->>>>>>>>Copiando el archivo  %s " %archivo)
		if(os.path.isfile(archivo)):
			print("****Archivo encontrado**********")
			print("\n")
		else:
			print("No encuentra el archivo obtenido")
	except:
		print("Fallo al intentar copiar el archivo %s " %archivo )
	sftp_client.close()
	ssh.close()
def delete():
	ssh = paramiko.SSHClient()
	archivo=input("Ingrese el archivo que desea eliminar ")
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	ssh.connect(host,port,user,pas)
	sftp_client=ssh.open_sftp()
	try:
		sftp_client.remove(archivo)
		print("-------->>>>>Eliminado correctamente")
		print("\n")
	except:
		print("No existe el archivo %s en el servidor " %archivo)
	sftp_client.close()
	ssh.close()




def conexion():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	try:
		ssh.connect(host,port,user,pas)
		print("BIENVENIDO ---> %s" %user)
		print("\n")
	except:
		print("Error de conexion no coinciden los datos ingresados")
		sys.exit()


try:
	host=input("Input a host: ")
	port=int(input("Input a port: "))
	user=input("Input a user: ")
	pas=getpass("Input password: ")
	conexion()
	print("Programa de Obtener archivo , almacenar archivo o borrar archivo")
	v=int(input("Ingrese las veces que realizara los trabajos: "))
	for i in range(v):
		op=int(input("Elija la opcion que desea realizar \n1.Put file on server"
														"\n2.Get file on server "
														"\n3.Delete file on server"
														"\n4.View files "
														"\n5.Cerrar Programa "
														"\nIngrese la opcion: "))
		print('\n')
		if(op == 1):
			print("Ruta del directorio actual: ")
			ssh('pwd')
			set()
		elif(op == 2):
			print("Ruta actual del directorio servidor : ")
			ssh('pwd')
			print("Mostrar ficheros del servidor : ")
			ssh('ls')
			get()
		elif(op == 3):
			delete()
		elif(op == 4):
			ssh('ls')
		elif(op == 5):
			print("->>>>>>>>>Hasta luego--")
			sys.exit()
		else:
			print("No existe la opcion ingresada")
except ValueError:
	print("Deebe ingresra bien los datos")


