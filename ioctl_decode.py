#!/usr/bin/env python3
import sys

def ioctl_decode(ioctl_code):
    access_names = [
        "FILE_ANY_ACCESS",
        "FILE_READ_ACCESS",
        "FILE_WRITE_ACCESS",
        "FILE_READ_ACCESS | FILE_WRITE_ACCESS",
    ]
    method_names = [
        "METHOD_BUFFERED",
        "METHOD_IN_DIRECT",
        "METHOD_OUT_DIRECT",
        "METHOD_NEITHER",
    ]
    device_name_unknown = "<UNKNOWN>"
    device_names = [
        device_name_unknown,  # 0x0000
        "FILE_DEVICE_BEEP",  # 0x0001
        "FILE_DEVICE_CD_ROM",  # 0x0002
        "FILE_DEVICE_CD_ROM_FILE_SYSTEM",  # 0x0003
        "FILE_DEVICE_CONTROLLER",  # 0x0004
        "FILE_DEVICE_DATALINK",  # 0x0005
        "FILE_DEVICE_DFS",  # 0x0006
        "FILE_DEVICE_DISK",  # 0x0007
        "FILE_DEVICE_DISK_FILE_SYSTEM",  # 0x0008
        "FILE_DEVICE_FILE_SYSTEM",  # 0x0009
        "FILE_DEVICE_INPORT_PORT",  # 0x000A
        "FILE_DEVICE_KEYBOARD",  # 0x000B
        "FILE_DEVICE_MAILSLOT",  # 0x000C
        "FILE_DEVICE_MIDI_IN",  # 0x000D
        "FILE_DEVICE_MIDI_OUT",  # 0x000E
        "FILE_DEVICE_MOUSE",  # 0x000F
        "FILE_DEVICE_MULTI_UNC_PROVIDER",  # 0x0010
        "FILE_DEVICE_NAMED_PIPE",  # 0x0011
        "FILE_DEVICE_NETWORK",  # 0x0012
        "FILE_DEVICE_NETWORK_BROWSER",  # 0x0013
        "FILE_DEVICE_NETWORK_FILE_SYSTEM",  # 0x0014
        "FILE_DEVICE_NULL",  # 0x0015
        "FILE_DEVICE_PARALLEL_PORT",  # 0x0016
        "FILE_DEVICE_PHYSICAL_NETCARD",  # 0x0017
        "FILE_DEVICE_PRINTER",  # 0x0018
        "FILE_DEVICE_SCANNER",  # 0x0019
        "FILE_DEVICE_SERIAL_MOUSE_PORT",  # 0x001A
        "FILE_DEVICE_SERIAL_PORT",  # 0x001B
        "FILE_DEVICE_SCREEN",  # 0x001C
        "FILE_DEVICE_SOUND",  # 0x001D
        "FILE_DEVICE_STREAMS",  # 0x001E
        "FILE_DEVICE_TAPE",  # 0x001F
        "FILE_DEVICE_TAPE_FILE_SYSTEM",  # 0x0020
        "FILE_DEVICE_TRANSPORT",  # 0x0021
        "FILE_DEVICE_UNKNOWN",  # 0x0022
        "FILE_DEVICE_VIDEO",  # 0x0023
        "FILE_DEVICE_VIRTUAL_DISK",  # 0x0024
        "FILE_DEVICE_WAVE_IN",  # 0x0025
        "FILE_DEVICE_WAVE_OUT",  # 0x0026
        "FILE_DEVICE_8042_PORT",  # 0x0027
        "FILE_DEVICE_NETWORK_REDIRECTOR",  # 0x0028
        "FILE_DEVICE_BATTERY",  # 0x0029
        "FILE_DEVICE_BUS_EXTENDER",  # 0x002A
        "FILE_DEVICE_MODEM",  # 0x002B
        "FILE_DEVICE_VDM",  # 0x002C
        "FILE_DEVICE_MASS_STORAGE",  # 0x002D
        "FILE_DEVICE_SMB",  # 0x002E
        "FILE_DEVICE_KS",  # 0x002F
        "FILE_DEVICE_CHANGER",  # 0x0030
        "FILE_DEVICE_SMARTCARD",  # 0x0031
        "FILE_DEVICE_ACPI",  # 0x0032
        "FILE_DEVICE_DVD",  # 0x0033
        "FILE_DEVICE_FULLSCREEN_VIDEO",  # 0x0034
        "FILE_DEVICE_DFS_FILE_SYSTEM",  # 0x0035
        "FILE_DEVICE_DFS_VOLUME",  # 0x0036
        "FILE_DEVICE_SERENUM",  # 0x0037
        "FILE_DEVICE_TERMSRV",  # 0x0038
        "FILE_DEVICE_KSEC",  # 0x0039
        "FILE_DEVICE_FIPS",  # 0x003A
        "FILE_DEVICE_INFINIBAND",  # 0x003B
        device_name_unknown,  # 0x003C
        device_name_unknown,  # 0x003D
        "FILE_DEVICE_VMBUS",  # 0x003E
        "FILE_DEVICE_CRYPT_PROVIDER",  # 0x003F
        "FILE_DEVICE_WPD",  # 0x0040
        "FILE_DEVICE_BLUETOOTH",  # 0x0041
        "FILE_DEVICE_MT_COMPOSITE",  # 0x0042
        "FILE_DEVICE_MT_TRANSPORT",  # 0x0043
        "FILE_DEVICE_BIOMETRIC",  # 0x0044
        "FILE_DEVICE_PMI",  # 0x0045
        "FILE_DEVICE_EHSTOR",  # 0x0046
        "FILE_DEVICE_DEVAPI",  # 0x0047
        "FILE_DEVICE_GPIO",  # 0x0048
        "FILE_DEVICE_USBEX",  # 0x0049
        "FILE_DEVICE_CONSOLE",  # 0x0050 (note: skip to 0x50 index)
    ]
    extra_names = [
        "FILE_DEVICE_NFP",  # 0x0051
        "FILE_DEVICE_SYSENV",  # 0x0052
        "FILE_DEVICE_VIRTUAL_BLOCK",  # 0x0053
        "FILE_DEVICE_POINT_OF_SERVICE",  # 0x0054
        "FILE_DEVICE_STORAGE_REPLICATION",  # 0x0055
        "FILE_DEVICE_TRUST_ENV",  # 0x0056
        "FILE_DEVICE_UCM",  # 0x0057
        "FILE_DEVICE_UCMTCPCI",  # 0x0058
        "FILE_DEVICE_PERSISTENT_MEMORY",  # 0x0059
        "FILE_DEVICE_NVDIMM",  # 0x005A
        "FILE_DEVICE_HOLOGRAPHIC",  # 0x005B
        "FILE_DEVICE_SDFXHCI",  # 0x005C
        "FILE_DEVICE_UCMUCSI",  # 0x005D
        "FILE_DEVICE_PRM",  # 0x005E
        "FILE_DEVICE_EVENT_COLLECTOR",  # 0x005F
        "FILE_DEVICE_USB4",  # 0x0060
        "FILE_DEVICE_SOUNDWIRE",  # 0x0061
    ]
    while len(device_names) < 0x50:
        device_names.append(device_name_unknown)
    device_names.extend(extra_names)
    device_names2 = [
        {"name": "MOUNTMGRCONTROLTYPE", "code": 0x0000006D},
    ]
    device = (ioctl_code >> 16) & 0xFFFF
    access = (ioctl_code >> 14) & 0x3
    function = (ioctl_code >> 2) & 0xFFF
    method = ioctl_code & 0x3

    if device < len(device_names):
        device_name = device_names[device]
    else:
        device_name = device_name_unknown
        for dev in device_names2:
            if device == dev["code"]:
                device_name = dev["name"]
                break

    print(f"ioctl_decode(0x{ioctl_code:08X})")
    print(f"Device   : {device_name} (0x{device:04X})")
    print(f"Function : 0x{function:X}")
    print(f"Method   : {method_names[method]} ({method})")
    print(f"Access   : {access_names[access]} ({access})")
    print("")

def parse_number(s):
    s = s.strip()
    try:
        if s.lower().startswith("0x"):
            return int(s, 16)
        return int(s, 10)
    except ValueError:
        raise

def main(argv):
    if len(argv) < 2:
        print("Usage: python3 ioctl_decode.py <ioctl_code1> [ioctl_code2 ...]")
        print("Example: python3 ioctl_decode.py 0x8007A85C 0x8007282C")
        return 1
    for token in argv[1:]:
        try:
            val = parse_number(token)
        except ValueError:
            print(f"Invalid number: {token}")
            continue
        val = val & 0xFFFFFFFF
        ioctl_decode(val)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
