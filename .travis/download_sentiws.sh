export DOWNLOADURL='http://pcai056.informatik.uni-leipzig.de/downloads/etc/SentiWS/SentiWS_v1.8c.zip'

wget -O sentiws.ZIP $DOWNLOADURL
mkdir -p data
unzip sentiws.ZIP -d data/sentiws/
rm data/sentiws/SentiWS.txt
rm -r data/sentiws/__MACOSX