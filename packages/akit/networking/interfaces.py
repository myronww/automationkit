
import fcntl
import socket
import struct

import netifaces

from akit.compat import bytes_cast


def get_ip_address(ifname):

    ifname = bytes_cast(ifname)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sfd = s.fileno()
    ifname_packed = struct.pack('256s', ifname[:15])
    iface = socket.inet_ntoa(
        fcntl.ioctl(sfd,
        0x8915,  # SIOCGIFADDR
        ifname_packed)[20:24])

    return iface

def get_correspondance_interface(ref_ip, ref_port, addr_family=socket.AF_INET):
    """
        Utilizes the TCP stack to make a connection to a remote computer and utilizes
        gets the network interface that was used to connect to the remote computer.
        This network interface is the network interface that is likely to be visible
        to the remote computer and thus could be used to establish services that will
        be visible to the remote computer.

        :param ref_ip: An IP address of a computer that is on the subnet that you wish
                       to find the correspondance ip address for and that is hosting a
                       service that will accept a TCP connection from a client.
        :type ref_ip: str
        :param ref_port: The port number of a service on a computer that will accept a
                         TCP connection so we can determine a path to the computer.
        :type ref_port: int
        :param addr_family: The socket address family to utilize when making a remote
                            connection to a host socket.AF_INET or socket.AF_INET6.
                            The address family used will determine the type of IP address
                            returned from this function.
        :type addr_family: int

        :returns: The correspondance interface and IPAddress that can be used to setup a
                  service that is visible to the reference IP address.
        :rtype: (str, str)
    """

    corr_iface = None

    corr_ip = get_correspondance_ip_address(ref_ip, ref_port, addr_family=addr_family)

    iface_name_list = [ iface for iface in netifaces.interfaces() ]
    for iface in iface_name_list:
        if_address_table = netifaces.ifaddresses(iface)
        if addr_family in if_address_table:
            faddr_list = if_address_table[addr_family]
            for faddr in faddr_list:
                if 'addr' in faddr:
                    ipaddr = faddr['addr']
                    if ipaddr == corr_ip:
                        corr_iface = iface
                        break
        if corr_iface is not None:
            break

    return corr_iface, corr_ip

def get_correspondance_ip_address(ref_ip, ref_port, addr_family=socket.AF_INET):
    """
        Utilizes the TCP stack to make a connection to a remote computer and utilizes
        gets the socket address of the socket that connected to the remote computer.
        This socket address is the address of the socket that is likely to be visible
        to the remote computer and thus could be used to establish services that will
        be visible to the remote computer.

        :param ref_ip: An IP address of a computer that is on the subnet that you wish
                       to find the correspondance ip address for and that is hosting a
                       service that will accept a TCP connection from a client.
        :type ref_ip: str
        :param ref_port: The port number of a service on a computer that will accept a
                         TCP connection so we can determine a path to the computer.
        :type ref_port: int
        :param addr_family: The socket address family to utilize when making a remote
                            connection to a host socket.AF_INET or socket.AF_INET6.
                            The address family used will determine the type of IP address
                            returned from this function.
        :type addr_family: int

        :returns: The correspondance IP address that can be used to setup a service that
                  is visible to the reference IP address.
        :rtype: str
    """
    corr_ip = None

    sock = socket.socket(addr_family, socket.SOCK_STREAM)
    try:
        sock.settimeout(10)
        sock.connect((ref_ip, ref_port))
        corr_ip, _ = sock.getsockname()
    except Exception as xcpt:
        # If an exception occurs, just return None
        pass
    finally:
        sock.close()

    return corr_ip
