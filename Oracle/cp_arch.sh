cp /u01/app/oracle/oradata/XE/users.dbf         /u01/bkup/arch
cp /u01/app/oracle/oradata/XE/sysaux.dbf       /u01/bkup/arch
cp /u01/app/oracle/oradata/XE/undotbs1.dbf  /u01/bkup/arch
cp /u01/app/oracle/oradata/XE/system.dbf      /u01/bkup/arch
cp /u01/app/oracle/fast_recovery_area/XE/onlinelog/o1_mf_2_cx7h1sq6_.log   /u01/bkup/arch
cp /u01/app/oracle/fast_recovery_area/XE/onlinelog/o1_mf_1_cx7h1lwc_.log   /u01/bkup/arch
cp /u01/app/oracle/oradata/XE/control.dbf       /u01/bkup/arch

chown oracle:dba *.*
