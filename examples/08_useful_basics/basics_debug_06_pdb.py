
vlans = ["1", "2", "3", "test", "4", "5", "switchport allowed vlans add", "100"]


vlans_list = []
for vl in vlans:
    if vl.isdigit():
        new_vl = int(vl)
        print(f"{vl=} {new_vl=}")
        vlans_list.append(new_vl)

print(vlans_list)
