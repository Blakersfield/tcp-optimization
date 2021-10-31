import subprocess


def cc(algo):
    terminal = "sysctl net.ipv4.tcp_congestion_control = " + algo
    subprocess.Popen(terminal, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def rmem(minv, maxv, startv):
    terminal = "sysctl net.ipv4.tcp_rmem = " + str(minv) + " " + str(startv) + " " + str(maxv)
    subprocess.Popen(terminal, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def wmem(minv, maxv, startv):
    terminal = "sysctl net.ipv4.tcp_wmem = " + str(minv) + " " + str(startv) + " " + str(maxv)
    subprocess.Popen(terminal, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def win_scale(binary):
    param = None
    if binary:
        param=1
    else:
        param=0
    terminal = "sysctl net.ipv4.tcp_window_scaling = " + str(param)
    subprocess.Popen(terminal, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)