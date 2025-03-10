# CN_Assignment_2
This is the repository containing the files for assignment(2) of Computer Networks(2025) at IIT Gandhinagar

## Team Overview

- **Mitansh Patel** (24120033)
- **Chinteshwar Dhakate** (24120024)


## Protocol Assignments

1. **Protocol 1**: BIC TCP
2. **Protocol 2**: HighSpeed TCP
3. **Protocol 3**: Yeah TCP (derived from team ID formula)
 **Congestion Mitigation**: Techniques to reduce network overload (e.g., QoS, traffic shaping). Includes bandwidth upgrades and traffic prioritization.  

 **Mininet**: Network emulator for creating virtual SDN environments. Simulates switches, hosts, and controllers for testing.  

## Implementation Structure

Three core components with associated tools:


| Component | Tools Used | Key Metrics |
| :-- | :-- | :-- |
| TCP Protocol Comparison | Mininet, iperf3 | Throughput, Window Size |
| SYN Flood Defense | Python, sysctl | Packet Loss, Connection Duration |
| Nagle's Algorithm | Custom Python scripts | Goodput, Network Latency |

## Repository Organization

```
├── Task1/                 # Congestion control comparison
│   ├── topology.py        # Mininet configuration
│   ├── iperf_config.sh    # TCP client-server setup
│   └── analysis.ipynb     # Jupyter metrics analysis
├── Task2/                 # SYN flood implementation
│   ├── syn_flood.py       # Attack script
│   ├── mitigation.sh      # Kernel hardening
│   └── packet_capture.sh  # tcpdump automation
├── Task3/                 # Nagle's algorithm testing
│   └── nagle_test.py      # Algorithm configuration
└── utils/
    ├── plot_generator.py       # Visualization tools
    └── connection_analyzer.py  # TCP analysis
```


## Setup Requirements

**OS:** Linux (Ubuntu/Debian recommended)
**Dependencies:**

```bash
sudo apt install mininet iperf3 wireshark tshark python3-pip
pip3 install matplotlib numpy pandas jupyter
```


## Task Execution

### Task 1: Protocol Comparison

1. Start Mininet topology:
```bash
sudo mn --custom Task1/topology.py --test pingall
```

2. Configure iperf3 server on H7:
```bash
iperf3 -s -p 5001
```

3. Run client tests:
```bash
python3 Task1/iperf_config.sh --option=a --congestion=<protocol>
```


### Task 2: SYN Flood Defense

**Attack Implementation:**

```bash
cd Task2
sudo sysctl -w net.ipv4.tcp_syncookies=0
sudo python3 syn_flood.py -t <server_ip> -p 80 --duration=100
```

**Mitigation:**
.  
```bash
sudo sysctl -w net.ipv4.tcp_syncookies=1
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=1024
```
 **Congestion Mitigation**: 
 Techniques to reduce network overload (e.g., QoS, traffic shaping). Includes bandwidth upgrades and traffic prioritization.  

### Task 3: Nagle's Algorithm
```bash
python3 Task3/nagle_test.py --nagle <0/1> --delay_ack <0/1>
```

| Configuration | Nagle | Delayed-ACK |
| :-- | :-- | :-- |
| 1 | 1 | 1 |
| 2 | 1 | 0 |
| 3 | 0 | 1 |
| 4 | 0 | 0 |
 **Nagle’s Algorithm**: Reduces small packets by buffering data until ACK received. Disabled via `TCP_NODELAY` for latency-sensitive apps
Test configurations:
 **Delayed-ACK**: Delays TCP acknowledgments by ~500ms to combine responses. Conflicts with Nagle’s, causing temporary deadlocks.  

## Analysis Metrics

- **Throughput:** iperf3 JSON reports
- **Packet Loss:** tcpdump statistics
- **Window Size:** TCP header analysis
- **Connection Duration:** tshark timestamps

 **SYN Flag**: Initiates TCP connections during 3-way handshake. Sent by clients to synchronize sequence numbers.  
 **FIN Flag**: Gracefully terminates TCP connections. Triggers 4-step closure process when no data remains. 
 **RESET,ACK (RST,ACK)**: Abruptly terminates a TCP connection while acknowledging prior data. Combines RST (forceful closure) with ACK (confirms received packets) 
 **FIN-ACK**: Gracefully closes one direction of a TCP connection while acknowledging data. Combines FIN (initiates closure) with ACK (confirms prior segment receipt) 
Note: RST,ACK is rare (resets typically don't require ACKs), while FIN-ACK is common during normal shutdowns

## Deliverables

- Time-series plots of network metrics
- Comparative protocol performance tables
- PCAP files for all experiments
- Kernel parameter logs (sysctl.conf)


## References

1. [Mininet Documentation](http://mininet.org/)
2. [Linux Kernel Parameters](https://www.kernel.org/doc/html/latest/networkir)
3. [iPerf3 Documentation](https://iperf.fr/)

