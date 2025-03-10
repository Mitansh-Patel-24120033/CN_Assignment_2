# Run each Python program in the background (&)
echo "For test script replace: [server_ip], [server_port], [interface] with valid values"
(sleep 20 && timeout 100 sudo hping3 [server_ip] -S -p [server_port] --flood) &
(timeout 165 sudo tcpdump -i [interface] -n -w capture.pcap) &
sudo python3 Client.py
# Wait for all background processes to complete
wait

echo "All processes have finished."
