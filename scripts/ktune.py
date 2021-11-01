import subprocess


def cc(algo="reno", readback=True):
    terminal = "sysctl -w net.ipv4.tcp_congestion_control=" + algo
    proc=subprocess.Popen(terminal, shell=True,
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if readback:
        print(proc.stdout.readline().strip())


def rmem(minv=4096, maxv=6291456, startv=131072, readback=True):
    terminal = "sysctl -w net.ipv4.tcp_rmem=\"" + str(minv) + " " + str(startv) + " " + str(maxv)+"\""
    proc = subprocess.Popen(terminal, shell=True,
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if readback:
        print(proc.stdout.readline().strip())

def wmem(minv=4096, maxv=4194304, startv=16384, readback=True):
    terminal = "sysctl -w net.ipv4.tcp_wmem=\"" + str(minv) + " " + str(startv) + " " + str(maxv)+"\""
    proc = subprocess.Popen(terminal, shell=True,
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if readback:
        print(proc.stdout.readline().strip())


def win_scale(binary):
    param = None
    if binary:
        param=1
    else:
        param=0
    terminal = "sysctl -w net.ipv4.tcp_window_scaling=" + str(param)
    subprocess.Popen(terminal, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
