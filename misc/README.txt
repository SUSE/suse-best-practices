#
#  ggf folgende Zeile einzufügen in /etc/docker/daemon.json
#  "storage-driver": "devicemapper",
#  * bei systemctl status docker kam eine Fehlermeldung etwa:
#  could not use snapshotter devmapper in metadata plugin error="devmapper not configured 
#  * beim ausführen von daps2docker.sh kam die Fehlermeldung:
#  docker: Error response from daemon: stat /var/lib/docker/btrfs/subvolumes/c9ed033237bac69124c58ba7aad83a3758a66de85fa681b35f8d29b2cdb40375: 
#  no such file or directory.  
#                                                                                                                                            
