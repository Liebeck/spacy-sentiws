export DOWNLOADURL='http://pcai056.informatik.uni-leipzig.de/downloads/etc/SentiWS/SentiWS_v2.0.zip'

wget -O sentiws.ZIP $DOWNLOADURL
mkdir -p data
unzip sentiws.ZIP -d data/sentiws/
rm data/sentiws/SentiWS.txt