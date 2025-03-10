from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
import time
import argparse

def buildTOPO(option=None):
	net=Mininet(switch=OVSSwitch, link=TCLink)
	c0=net.addController('c0')
	# Add switches
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	s3 = net.addSwitch('s3')
	s4 = net.addSwitch('s4')

	# Add hosts
	h1 = net.addHost('h1')
	h2 = net.addHost('h2')
	h3 = net.addHost('h3')
	h4 = net.addHost('h4')
	h5 = net.addHost('h5')
	h6 = net.addHost('h6')
	h7 = net.addHost('h7')

	# Connect hosts to switches
	net.addLink(h1, s1)
	net.addLink(h2, s1)
	net.addLink(h3, s2)
	net.addLink(h4, s3)
	net.addLink(h5, s3)
	net.addLink(h6, s4)
	net.addLink(h7, s4)
	if option=='a' or option=='b':
		# Connect switches
		net.addLink(s1, s2)
		net.addLink(s2, s3)
		net.addLink(s3, s4)
	if option=='c' or option=='d1'or option=='d2':
		#Connect switches
		net.addLink(s1, s2, bw=100)
		if option=='c':
			net.addLink(s2, s3, bw=50)
		elif option=='d1':
			net.addLink(s2, s3, bw=50, loss=1)
		elif option=='d2':
			net.addLink(s2, s3, bw=50, loss=5)
		net.addLink(s3, s4, bw=100)
	
	net.start()
	#Testing Pings
	net.pingAll()

	#Working with CLI
	CLI(net)
	net.stop()

# Run the topology
if __name__ == '__main__':
	#op=input("Enter a choice: ")
	parser = argparse.ArgumentParser(description="Run Mininet topology experiments with configurable options.")
	parser.add_argument('--option', type=str, required=True, choices=['a', 'b', 'c', 'd1', 'd2'], help="Specify the experiment to run: a, b, c, d1 (link loss: S2-S3 at 1%), d2 (link loss: S2-S3 at 5%)")
	args = parser.parse_args()
	setLogLevel('info')
	buildTOPO(args.option)
	

