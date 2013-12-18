---
layout: default
title: Networking Glossary
categories: glossary
---

**ARP** - Address Resolution Protocol.  How machines on a local network talk to each other to figure out which MAC address corresponds to a given IP address.

**bridge** - a machine connected to multiple networks that can blindly copies traffic between them.

**DHCP** - Dynamic Host Configuration Protocol.  The way a server assigns dynamic IP addresses to a machine.

**dynamic address** - an IP address that is assigned by a server and can be changed on the whim of that server

**gateway** - a machine on the local network that can route packets to the global internet

**hub** - a box that connects multiple machine together, where every machine sees all the traffic to all the other machines (vs switch)

**IP address** - a logical address assigned to a machine so that it can communicate

**MAC address** - Media Access Controller.  A physical (i.e. in hardware) network address associated with a network card.

**NAT** - network address translation.  A standard for letting multiple machines with private address to connect to the internet with a single public address.

**netmask** - a set of bits used to differentiate between machines on the global internet versus the local network.

**private address** - an IP address that cannot be used on the global internet.  A machine with a private address must go through a router with NAT to access the internet.

**router** - a machine connected to multiple networks that can intelligently send traffic from one network to the other.

**static address** - an IP address that does not change

**switch** - a box that connects multiple machines together.  Each machine will only sees its own traffic (and broadcast traffic).

To Do
=====
Ethernet - http://en.wikipedia.org/wiki/Ethernet
access point
router
crossover cable
VLAN
packet
broadcast
domain name
host name
DNS
dynamic DNS
registrar
firewall
LAN
reverse DNS
multi-homed

Tools
=====
dig
arp
traceroute/tracert
route
ifconfig/ipconfig
whois
