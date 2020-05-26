from os import name as os_name
from sys import argv
from threading import Thread
from subprocess import run, PIPE
from time import time
from re import search
from re import compile as re_compile
autores="dan884075 and ronip"
print("""\n WIFI SCAN 1.0""")
TTL_OS = {128: "windows", 32: "Windows 95", 64: "linux", 255: "Solaris 2"} #TTL de cada sistema operativo

#Comandos para el ping en cada SO
#Hacen el ping con un paquete En la última posición se pondrá la ip a probar
LINUX_PING = "timeout {} ping -c 1 x"
WINDOWS_PING = "ping -w {} -n 1 x"


LINUX_TTL_RE = re_compile("ttl=[0-9]{1,3}")
WINDOWS_TTL_RE = re_compile("TTL=[0-9]{1,3}")

class ThreadScanner(Thread):
        """Hilo que comprueba que las ip en el rango indicado sean accesibles"""

        def __init__(self, start, end, baseIp, timeout, command, correctPing, getTTL):
                """start: Inicio del rango de ip
                end: Fin del rango de ip, no se incluye este valor
                baseIp: Ip base a la que se añadirán los números en el rango indicado
                timeout: Tiempo máximo de cada ping
                command: Comando para ejecutar el ping
                correctPing: Función que devuelve si el ping es correcto al pasarle la salida de consola
                getTTL: Función que devueve el ttl del ping, al pasarle la salida de consola"""

                if not (callable(correctPing) and callable(getTTL)):
                        raise ValueError("correctPing o getTTL no es una función")

                super().__init__()

                self.startNum = start
                self.endNum = end
                self.baseIp = baseIp

                self.command = command.format(timeout).split(" ")
                self.correctPing = correctPing
                self.getTTL = getTTL
                self.nIpFound = 0

        def run(self):
                for a in range(self.startNum, self.endNum):
                        ip = self.baseIp + str(a)
                        self.command[-1] = ip

                        comando = run(self.command, stdout=PIPE, stderr=PIPE).stdout.decode(errors="ignore")

                        if self.correctPing(comando):
                                ttl = self.getTTL(comando)
                                print("\n" + ip + " ACTIVA < " + (TTL_OS[ttl] if ttl in TTL_OS else "SO no reconocido") + " >")
                                self.nIpFound += 1


getLinuxThread = lambda *params: ThreadScanner(*params, LINUX_PING, lambda x: "1 received" in x, lambda data: int(search(LINUX_TTL_RE, data).group()[4:]))
getWindowsThread = lambda *params: ThreadScanner(*params, WINDOWS_PING, lambda x: "(0% perdidos)" in x, lambda data: int(search(WINDOWS_TTL_RE, data).group()[4:]))


def scan(ip, nThreads, timeout, scanner):
        if nThreads <= 0 or nThreads > 256:
                raise ValueError("Máximo número de hilos 256")

        threads = []
        nElemsThread = 256 // nThreads
        curNum = 0

        for i in range(nThreads):
                threads.append(scanner(curNum, curNum + nElemsThread if i != nThreads - 1 else 256, ip, timeout))
                threads[i].start()
                curNum += nElemsThread

        nIpFound = 0
        for thread in threads:
                thread.join()
                nIpFound += thread.nIpFound

        print("\n---------------------------------------------------------------")
        print("\nEscaneo correcto 256 ip escaneadas: " + str(nIpFound) + " activas.")
        print("\n---------------------------------------------------------------")


def main():
        try:
                if os_name == "nt":
                        scanner = getWindowsThread

                elif os_name == "posix":
                        scanner = getLinuxThread

                else:
                        print("SO no soportado")
                        exit(-1)

                if argv[1] == "-h":
                        print("""

FastWifiscanner.py [GATEWAY] [HILOS RECOMENDADO 256] [TIEMPO DE TIMEOUT EN SEGUNDOS RECOMENDADO 0.5]

EJEMPLO:

FastWifiscanner.py 192.168.1. 256 0.5
                        """)

                elif len(argv) == 3:
                        scan(argv[1], int(argv[2]), 1, scanner)

                elif len(argv) == 4:
                        scan(argv[1], int(argv[2]), float(argv[3]), scanner)

                else:
                        print("Parámetros inválidos")
        except:
                                        print("""

FastWifiScaner.py [GATEWAY] [HILOS RECOMENDADO 256] [TIEMPO DE TIMEOUT EN SEGUNDOS RECOMENDADO 0.5]
EJEMPLO:
FastWifiScaner.py 192.168.1. 256 0.5
                        """)

if __name__ == '__main__':
        t0 = time()
        main()
        print(f"Time: {time() - t0}")
