[ 15.09.2023 ]=====================================================================================

		rkDumper.exe
		version 1.1.2.1 (Windows)
		(c) RedScorpio, Moscow, 2014-2023

	Утилита предназначена для снятия дампов с прошивок формата RKFW/RKAF и RKFP устройств 
        на SoC производства RockChip.

	Тестировалось на ОС:
	WinXP (32), WinVista (32), Win7 (32/64), win10 (64)

	Примечание: Возможности проверить на всех (и даже на многих) устройствах нет и, скорее всего,
	            никогда не будет, поэтому используете эту утилиту на свой страх и риск.

	Supported Rockchip's SoC 
		VID:PID		description		tested on
		=========	=========		=========
		0bb4:2910	MSC device (USB debug off)
		0bb4:0c02	MSC device (USB debug on)

		2207:0000	MSC device (USB debug off)
		2207:0010	MSC device (USB debug on)

		2207:350D	RK3562
		2207:350C	RK3528
		2207:350B	RK3588J/RK3588S		ITX-3588J
		2207:350A	RK3566/RK3568		x88 Pro
		2207:330D	RK3308/RK3326/RK3388/PX30
							Evoo EV-A-81-8-1
		2207:330E	RK3308B
		2207:330C	RK3399/PX6		CSA96
		2207:330A	RK3368/PX5		Artway X6/HCT MTCD (Car head unit) SOM
		2207:320C	RK3318/RK3328/PX4	A5X Plus mini
		2207:320B	RK3229			MXQ 4K
		2207:320A	RK3288			Jesurun T034
		2207:310D	RK3126			Proscan PLT9650G
		2207:310C	RK3128			CS918-rk3128
		2207:310B	RK3188/PX3		PIPO Max M9 Pro
		2207:301A	RK3036			Wecast E8
		2207:300B	RK3168			Starmobile Engage7+
		2207:300A	RK3066/PX2		UG802
		2207:292C	RK3026/RK3028		ONYX BOOX C67SML COLUMBUS/?
		2207:292A	RK2928			Lexibook Tablet Master 2
		2207:290A	RK2906			TeXeT TB-138
		2207:281A	RK2818			ChinaLeap M3

    Состав архива:
    1. rkDumper.exe		- утилита.
    2. rkDumper.exe.manifest	- манифест.
    3. ReadMe.txt		- этот файл.
    Дополнительные файлы (для возможности работы автообновления):
    4. updater.exe
    5. NLog.dll 
    6. first.inf (позже будет удален)

===================================================================================================

    Download:
    http://4pda.ru/forum/index.php?showtopic=614530 (rus)
    http://forum.xda-developers.com/general/rooting-roms/tool-rkdumper-utility-backup-firmware-t2915363 (eng)

===================================================================================================

History:
1.1.2.1 (15.09.2023)
	+ RK3562;
1.1.2.0 (10.08.2023)
	+ RK3528;
1.1.1.7 (11.04.2023)
	+ RK3588J;
1.1.1.6 (11.01.2023)
	+ RK3588J/RK3588S;
	~ minor improvements.
1.1.1.0 (28.07.2022)
	+ autoUpdate;
	~ minor improvements.
1.1.0.0 (28.06.2022)
        + version numbering changed;
	+ support of RK3566 added;
	+ RKFP firmware format support;
	~ minor improvements.
1.08 (08.08.2019)
	~ bug fixed.
1.07 (10.07.2019)
	+ support of RK3388 added;
	+ support of RK3036G added;
	+ drivers version&date;
	~ minor improvements.
1.06 (04.04.2018)
	+ /part key added;
	+ /nrst key added;
	+ USB version decoding;
	+ Low Speed mode detection;
	~ minor improvements.
1.05 (09.10.2017)
	+ /load key added;
	+ "idb" command added;
	+ support of RK3399 added;
	+ support of RK2818 added;
	+ "chip" command added;
	+ "bad" command added;
	+ "MASKROM mode" detection added;
	~ minor improvements.
1.04 (03.05.2017)
	+ support of RK3328 added;
	~ minor improvements.
1.03 (10.03.2017)
	+ support of RK3229 added;
	+ /last key added;
	+ RSCE file size correction added.
1.02 (24.02.2016)
	~ /user key logic changed;
	~ errors handling changed;
	+ parm mode added;
	+ /pfile key added.
1.01 (15.01.2016)
	+ support of RK2928 added;
	+ support of RK3126 added;
	+ support of RK3368 added;
	+ detection of MTP&PTP modes added;
	~ some algorithms improved.
1.00 (02.09.2015)
	! Release;
	+ /incl key added;
	+ /excl key added;
	~ some algorithms improved.
0.95 (05.08.2015)
	! pre-Release #5;
	+ support of RK3128 added;
	+ /user key added;
	+ ROM size/vendor/ID determinetion added ("info" command);
	~ bug of incorrect determination of disks in multi-CD systems fixed.
0.94 (12.01.2015)
	! pre-Release #4;
	+ support of RK3268 added;
	+ manifest file added;
	+ detection of device revision added;
	~ administrator's rights checking algorithm changed.
0.93 (27.11.2014)
	! pre-Release #3;
	+ support of RK3168 added;
	+ administrator's rights checking added.
0.92 (29.10.2014)
	! pre-Release #2;
	~ "4GB" bug fixed;
	+ support of "USB debug on" mode added;
	+ support of RK3026 added;
	+ support of RK2906 added;
	+ support of VID=0bb4 (HTC? Rockchip devices) added.
0.91 (23.10.2014)
	! pre-Release #1.
0.90 (21.10.2014)
	! pre-Release (for internal use).

===================================================================================================
