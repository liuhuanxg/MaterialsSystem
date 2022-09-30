import json

data = {"version": 2, "data": [{
                                   "tp_qemu_disk": "{\"reset_conn_info\": {\"hcbs_client\": \"S<sl\", \"hcbs_agent\": \"S<sl\", \"iscsid_1\": \"S<Ls\", \"spdk\": \"R\", \"iscsid\": \"S<s\", \"host\": \"11.131.200.117\", \"client_cpu\": 0, \"reset_conn_num\": -1, \"time\": \"2022-09-21 10:18:43\", \"is_have_spdk_compute\": \"common_have_spdk\", \"spdk_is_ztcp\": 1}, \"cfs_flag\": null, \"qemu_disk_config_and_iostat\": {\"/dev/a1e78108\": [{\"wld_status\": 0, \"await\": 100, \"wcnt\": 9, \"disk_num\": 17, \"wband\": 439, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 8799, \"avgqu\": 0, \"size\": \"260G\", \"wld_uuid\": \"a1e78108-73c1-45e1-ad7b-9c9abb293650\", \"rcnt\": 0, \"uuid\": \"a1e78108-73c1-45e1-ad7b-9c9abb293650\", \"rband\": 0, \"devname\": \"a1e78108\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 100, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/98efaa53\": [{\"wld_status\": 0, \"await\": 166, \"wcnt\": 119, \"disk_num\": 17, \"wband\": 1799, \"host_ip\": \"11.131.200.117\", \"util\": 20, \"svctm\": 175, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 3000, \"avgqu\": 0, \"size\": \"50G\", \"wld_uuid\": \"98efaa53-41ce-4691-b65c-327f720121c8\", \"rcnt\": 0, \"uuid\": \"98efaa53-41ce-4691-b65c-327f720121c8\", \"rband\": 0, \"devname\": \"98efaa53\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 166, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/8a36da70\": [{\"wld_status\": 0, \"await\": 50, \"wcnt\": 19, \"disk_num\": 17, \"wband\": 79, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 800, \"avgqu\": 0, \"size\": \"1400G\", \"wld_uuid\": \"8a36da70-c03b-4662-9344-db4d6a2575b3\", \"rcnt\": 0, \"uuid\": \"8a36da70-c03b-4662-9344-db4d6a2575b3\", \"rband\": 0, \"devname\": \"8a36da70\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 50, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/355e9af3\": [{\"wld_status\": 0, \"await\": 50, \"wcnt\": 19, \"disk_num\": 17, \"wband\": 79, \"host_ip\": \"11.131.200.117\", \"util\": 480, \"svctm\": 24050, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 800, \"avgqu\": 0, \"size\": \"1400G\", \"wld_uuid\": \"355e9af3-c8e9-4714-aae7-c4e3b8014fc9\", \"rcnt\": 0, \"uuid\": \"355e9af3-c8e9-4714-aae7-c4e3b8014fc9\", \"rband\": 0, \"devname\": \"355e9af3\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 50, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/08190d65\": [{\"wld_status\": 0, \"await\": 50, \"wcnt\": 19, \"disk_num\": 17, \"wband\": 79, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 800, \"avgqu\": 0, \"size\": \"1400G\", \"wld_uuid\": \"08190d65-85e7-44a0-af5a-78d131f810e4\", \"rcnt\": 0, \"uuid\": \"08190d65-85e7-44a0-af5a-78d131f810e4\", \"rband\": 0, \"devname\": \"08190d65\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 50, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/8879dda1\": [{\"wld_status\": 0, \"await\": 50, \"wcnt\": 19, \"disk_num\": 17, \"wband\": 79, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 800, \"avgqu\": 0, \"size\": \"1400G\", \"wld_uuid\": \"8879dda1-1678-4345-9360-c7bb24157bd3\", \"rcnt\": 0, \"uuid\": \"8879dda1-1678-4345-9360-c7bb24157bd3\", \"rband\": 0, \"devname\": \"8879dda1\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 50, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/3581794b\": [{\"wld_status\": 0, \"await\": 177, \"wcnt\": 219, \"disk_num\": 17, \"wband\": 1559, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 1418, \"avgqu\": 0, \"size\": \"50G\", \"wld_uuid\": \"3581794b-01f2-4c00-b470-32b0c5e616c4\", \"rcnt\": 0, \"uuid\": \"3581794b-01f2-4c00-b470-32b0c5e616c4\", \"rband\": 0, \"devname\": \"3581794b\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 177, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/fbff6806\": [{\"wld_status\": 0, \"await\": 185, \"wcnt\": 69, \"disk_num\": 17, \"wband\": 1079, \"host_ip\": \"11.131.200.117\", \"util\": 20, \"svctm\": 300, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 3085, \"avgqu\": 0, \"size\": \"50G\", \"wld_uuid\": \"fbff6806-c0fc-4594-b888-b7dc3b5198ba\", \"rcnt\": 0, \"uuid\": \"fbff6806-c0fc-4594-b888-b7dc3b5198ba\", \"rband\": 0, \"devname\": \"fbff6806\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 185, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/c8c0a33d\": [{\"wld_status\": 0, \"await\": 50, \"wcnt\": 19, \"disk_num\": 17, \"wband\": 79, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 800, \"avgqu\": 0, \"size\": \"1400G\", \"wld_uuid\": \"c8c0a33d-c500-4063-86ec-0d88cab74649\", \"rcnt\": 0, \"uuid\": \"c8c0a33d-c500-4063-86ec-0d88cab74649\", \"rband\": 0, \"devname\": \"c8c0a33d\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 50, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/0ac541a9\": [{\"wld_status\": 0, \"await\": 50, \"wcnt\": 19, \"disk_num\": 17, \"wband\": 79, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 800, \"avgqu\": 0, \"size\": \"1400G\", \"wld_uuid\": \"0ac541a9-7df2-472d-a355-2eeb99289e35\", \"rcnt\": 0, \"uuid\": \"0ac541a9-7df2-472d-a355-2eeb99289e35\", \"rband\": 0, \"devname\": \"0ac541a9\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 50, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/fbc4c560\": [{\"wld_status\": 0, \"await\": 50, \"wcnt\": 19, \"disk_num\": 17, \"wband\": 79, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 800, \"avgqu\": 0, \"size\": \"1400G\", \"wld_uuid\": \"fbc4c560-94ce-48c4-8749-12012cbc1e03\", \"rcnt\": 0, \"uuid\": \"fbc4c560-94ce-48c4-8749-12012cbc1e03\", \"rband\": 0, \"devname\": \"fbc4c560\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 50, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/66f6c902\": [{\"wld_status\": 0, \"await\": 0, \"wcnt\": 19, \"disk_num\": 17, \"wband\": 79, \"host_ip\": \"11.131.200.117\", \"util\": 12, \"svctm\": 650, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 800, \"avgqu\": 0, \"size\": \"1400G\", \"wld_uuid\": \"66f6c902-8d41-4a74-a428-4b3df0571090\", \"rcnt\": 0, \"uuid\": \"66f6c902-8d41-4a74-a428-4b3df0571090\", \"rband\": 0, \"devname\": \"66f6c902\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 0, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/a1b3f975\": [{\"wld_status\": 0, \"await\": 90, \"wcnt\": 219, \"disk_num\": 17, \"wband\": 2679, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 2436, \"avgqu\": 0, \"size\": \"100G\", \"wld_uuid\": \"a1b3f975-a563-4914-a204-7d2fc56ad503\", \"rcnt\": 0, \"uuid\": \"a1b3f975-a563-4914-a204-7d2fc56ad503\", \"rband\": 0, \"devname\": \"a1b3f975\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 90, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/446c30da\": [{\"wld_status\": 0, \"await\": 54, \"wcnt\": 5049, \"disk_num\": 17, \"wband\": 30396, \"host_ip\": \"11.131.200.117\", \"util\": 191, \"svctm\": 38, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 1203, \"avgqu\": 2, \"size\": \"500G\", \"wld_uuid\": \"446c30da-5980-4ce1-ade2-c9881143fe87\", \"rcnt\": 0, \"uuid\": \"446c30da-5980-4ce1-ade2-c9881143fe87\", \"rband\": 0, \"devname\": \"446c30da\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 54, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/b9380ef6\": [{\"wld_status\": 0, \"await\": 122, \"wcnt\": 679, \"disk_num\": 17, \"wband\": 4399, \"host_ip\": \"11.131.200.117\", \"util\": 20, \"svctm\": 30, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 1294, \"avgqu\": 1, \"size\": \"50G\", \"wld_uuid\": \"b9380ef6-2715-4947-9c02-1d431f1678fb\", \"rcnt\": 0, \"uuid\": \"b9380ef6-2715-4947-9c02-1d431f1678fb\", \"rband\": 0, \"devname\": \"b9380ef6\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 122, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/ea3488e4\": [{\"wld_status\": 0, \"await\": 58, \"wcnt\": 1209, \"disk_num\": 17, \"wband\": 28757, \"host_ip\": \"11.131.200.117\", \"util\": 83, \"svctm\": 69, \"proxy_ip\": \"0.0.0.0\", \"wld_change_ts\": 1663726723, \"avgrq\": 4753, \"avgqu\": 0, \"size\": \"1000G\", \"wld_uuid\": \"ea3488e4-b08c-4b18-9d83-7b4e1c12e185\", \"rcnt\": 0, \"uuid\": \"ea3488e4-b08c-4b18-9d83-7b4e1c12e185\", \"rband\": 0, \"devname\": \"ea3488e4\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 58, \"is_base\": 0, \"type\": \"spdk\", \"rrqm\": 0}]}, \"qemu_disk_iostat_sec\": {\"/dev/fbff6806\": [{\"await\": 400, \"wcnt\": 200, \"wband\": 1600, \"util\": 210, \"svctm\": 1050, \"avgrq\": 1600, \"avgqu\": 1, \"rcnt\": 0, \"uuid\": \"fbff6806-c0fc-4594-b888-b7dc3b5198ba\", \"rband\": 0, \"devname\": \"/dev/fbff6806\", \"wrqm\": 0, \"time\": \"2022-09-21 10:18:37\", \"type\": \"spdk\", \"rrqm\": 0}], \"/dev/355e9af3\": [{\"await\": 50, \"wcnt\": 200, \"wband\": 800, \"util\": 490, \"svctm\": 2450, \"avgrq\": 800, \"avgqu\": 0, \"rcnt\": 0, \"uuid\": \"355e9af3-c8e9-4714-aae7-c4e3b8014fc9\", \"rband\": 0, \"devname\": \"/dev/355e9af3\", \"wrqm\": 0, \"time\": \"2022-09-21 10:18:41\", \"type\": \"spdk\", \"rrqm\": 0}]}, \"disk_without_config_and_iostat\": {\"/dev/sdv\": [{\"wld_status\": 0, \"await\": 0, \"wcnt\": 0, \"disk_num\": 17, \"wband\": 0, \"host_ip\": \"11.131.200.117\", \"util\": 0, \"svctm\": 0, \"proxy_ip\": \"127.0.0.1\", \"is_check\": 0, \"wld_change_ts\": 1663726723, \"avgrq\": 0, \"avgqu\": 0, \"is_base\": 0, \"wld_uuid\": \"f64a6b53-bf83-417b-9e88-ab4aebec7eeb\", \"rcnt\": 0, \"uuid\": \"f64a6b53-bf83-417b-9e88-ab4aebec7eeb\", \"vm_offline\": \"\", \"rband\": 0, \"devname\": \"sdv\", \"wrqm\": 0, \"rawait\": 0, \"time\": \"2022-09-21 10:18:43\", \"wawait\": 0, \"type\": \"cbs_wcf\", \"rrqm\": 0}]}, \"qemu_vm_list\": []}"}],
        "host_ip": "11.131.200.117", "key": "report_cbs_log"}

for d in data["data"][0:1]:

    values = d["tp_qemu_disk"]
    values = json.loads(values)
    qemu_disk_iostat_sec = values["qemu_disk_iostat_sec"]
    qemu_disk_config_and_iostat = values["qemu_disk_config_and_iostat"]

    for _k, v in qemu_disk_iostat_sec.items():
        for _v in v:
            if _v["uuid"] == "355e9af3-c8e9-4714-aae7-c4e3b8014fc9":
                print("秒级io", _v)
                break
    for _k, v in qemu_disk_config_and_iostat.items():
        for _v in v:
            if _v["uuid"] == "355e9af3-c8e9-4714-aae7-c4e3b8014fc9":
                print("10s级io", _v)
                break


host_ips = """
11.130.40.244
30.105.174.94
30.126.234.186
11.130.47.22
11.130.40.229
30.126.235.211
30.105.174.149
11.130.47.4
30.105.171.20
30.123.206.61
30.126.233.242
30.126.237.19
30.126.236.11
30.105.43.217
30.126.236.6
30.126.235.234
30.126.236.34
30.105.201.98
11.130.47.122
11.130.46.230
11.130.41.22
30.100.72.156
30.126.237.53
30.126.233.239
11.130.41.186
30.126.236.21
30.118.208.33
11.130.40.236
30.126.237.22
30.126.237.47
11.127.108.229
30.126.233.248
30.106.72.114
30.106.77.237
"""

for host_ip in host_ips.split("\n"):
    print(json.dumps(host_ip)+",")