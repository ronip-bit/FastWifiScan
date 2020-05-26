# FastWifiScan
Un escáner de red de alta velocidad.

# Velocidad:

https://subefotos.com/ver/?83488be39496f8e3e7351b97b02e0a95o.png

Actualmente tiene una velocidad en distribuciónes Linux superior a la de nmap, es cierto que en Windows puede reducir su velocidad pero aún así compite con nmap.

# Características positivas:

1. El escáner no gasta muchos recursos del sistema.
2. Mucho más silencioso que otros como nmap.
3. Muy veloz y versátil.
4. Funciona en varios SO.
5. El script funciona en múltiples hilos.
6. Es open source.

# Características negativas:

1. Si la conexión a internet es lenta podría no detectar algunos dispositivos.
2. No trae interfaz gráfica.

# Uso:

FastWifiScaner.py [GATEWAY] [HILOS RECOMENDADO 256] [TIEMPO DE TIMEOUT EN SEGUNDOS RECOMENDADO 0.5]

Ejemplo:

python3 FastWifiScaner.py 192.168.1. 256 0.5

# Probado en:

Parrot OS
Ubuntu 18.04
Windows 10
Termux


