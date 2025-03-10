echo "This script will perform Task 3"
echo "Client scripts"
python3 Client.py --nagle --delack
sleep 1.5
python3 Client.py --nagle
sleep 1.5
python3 Client.py --delack
sleep 1.5
python3 Client.py
sleep 1.5
