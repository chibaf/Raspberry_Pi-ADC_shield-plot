# Raspberry_Pi-ADC_shield-plot
Raspberry_Pi-ADC_shield-plot

## installation (1)

Shield: High-Precision AD/DA Board - Waveshare Wiki  

https://www.waveshare.com/wiki/High-Precision_AD/DA_Board

Raspberry Pi AD/DA Expansion

wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.75.tar.gz

   19  tar zxvf bcm2835-1.75.tar.gz 
   
   20  cd bcm2835-1.75/
   
   21  sudo ./configure && sudo make -j4 && sudo make check && sudo make install
   

 23  wget https://project-downloads.drogon.net/wiringpi-latest.deb
 
   24  sudo dpkg -i wiringpi-latest.deb
   
   25  gpio -v
  
wget https://github.com/joan2937/lg/archive/master.zip

 29  wget https://github.com/joan2937/lg/archive/master.zip
 
   30  unzip master.zip
   
   31  cd lg-master
   
   32  sudo make install
   
   33

  sudo apt-get install ttf-wqy-zenhei
  
   37  sudo apt-get install python3-pip
   
   38  sudo pip install RPi.GPIO
   
   39  sudo pip install RPi.GPIO --break-system-packages
   
   40  sudo pip install spidev
   
   41  sudo pip install spidev --break-system-packages

   
29  wget https://github.com/joan2937/lg/archive/master.zip

   30  unzip master.zip
   
   31  cd lg-master
   
   32  sudo make install
   
   34  sudo apt-get update
 
   35  cd
   
   36  sudo apt-get install ttf-wqy-zenhei
  
   37  sudo apt-get install python3-pip
  
   38  sudo pip install RPi.GPIO
 
   39  sudo pip install RPi.GPIO --break-system-packages

   40  sudo pip install spidev

   41  sudo pip install spidev --break-system-packages

   42  history

   43  sudo apt-get install p7zip-full

   44  wget https://files.waveshare.com/upload/5/5e/High-Precision-AD-DA-Board-Code.7z

   45  7z x High-Precision-AD-DA-Board-Code.7z -r -o./High-Precision-AD-DA-Board-Code

   46  cd High-Precision-AD-DA-Board-Code/RaspberryPI/
 
   47  cd ADS1256/
 
   48  ls
 
   49  cd bcm2835/
 
   50  ls
 
   51  make 

   52  ls

   53  ./ads1256_test 
  
   54  cd

   55  history

pi@RasPi5SSD:~ $ 

sudo pip3 install rpi.gpio --break-system-packages

## installation (2)

gpio - wiringPi giving "Unable to determine board revision from /proc/cpuinfo" error after kernel 6.1 update - Raspberry Pi Stack Exchange

https://raspberrypi.stackexchange.com/questions/145031/wiringpi-giving-unable-to-determine-board-revision-from-proc-cpuinfo-error-af

command:

sudo apt update; sudo apt install --reinstall libraspberrypi0 libraspberrypi-{bin,dev,doc} raspberrypi-bootloader raspberrypi-kernel
