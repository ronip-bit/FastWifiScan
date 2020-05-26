# FastWifiScan
Un escáner de red Wi-Fi de alta velocidad.

 Velocidad:


<a href="https://imgbb.com/"><img src="https://i.ibb.co/VD4JwqF/Fast-Wifi-Scan.png" alt="Fast-Wifi-Scan" border="0"></a>

Actualmente tiene una velocidad en distribuciónes Linux superior a la de nmap, es cierto que en Windows puede reducir su velocidad pero aún así compite con nmap.

Características positivas:

1. El escáner no gasta muchos recursos del sistema.
2. Mucho más silencioso que otros como nmap.
3. Muy veloz y versátil.
4. Funciona en varios SO.
5. El script funciona en múltiples hilos.
6. Es open source.

Características negativas:

1. Si la conexión a internet es lenta podría no detectar algunos dispositivos.
2. No trae interfaz gráfica.

Uso:

FastWifiScaner.py [GATEWAY] [HILOS RECOMENDADO 256] [TIEMPO DE TIMEOUT EN SEGUNDOS RECOMENDADO 0.5]

Ejemplo:

python3 FastWifiScaner.py 192.168.1. 256 0.5

Probado en:

Parrot OS
Ubuntu 18.04
Windows 10
Termux


