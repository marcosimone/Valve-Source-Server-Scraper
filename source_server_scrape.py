import socket
import time
import struct
import sys

if len(sys.argv) != 4:
    print "\nusage:\n\t%s <IP> <PORT> [ipr]\n" % sys.argv[0]
    print "ipr can be in any order:"
    print "\ti - print server info"
    print "\tp - print player info"
    print "\tr - print rules\n"
    exit()
IP=sys.argv[1]
PORT=int(sys.argv[2],0)
args=sys.argv[3]
#IP="74.201.57.61"
#PORT=27015
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP\

def str2hex(s):
    return " ".join("{:02x}".format(ord(c)) for c in s)

def query(query): # INFO, PLAYER, RULES
    if query is "INFO":
        data=""
        msg="\xff\xff\xff\xff\x54Source Engine Query\x00" #get server info
        sock.sendto(msg, (IP,PORT))
        data_tmp, server = sock.recvfrom(4096)
        data = data+data_tmp
        if data[0] == "\xfe":
            num_packets=ord(data[8])
            for x in range(1, num_packets):
                data_tmp, server = sock.recvfrom(4096)
                data = data+data_tmp

    elif query is "PLAYER":
        data=""
        msg="\xff\xff\xff\xff\x55\xff\xff\xff\xff\x00" #get server info
        sock.sendto(msg, (IP,PORT))
        challenge, server = sock.recvfrom(4096)
        msg=challenge.replace("\x41","\x55") + "\x00";
        sock.sendto(msg, (IP,PORT))
        data_tmp, server = sock.recvfrom(4096)
        data=data_tmp
        if data_tmp[0] == "\xfe":
            num_packets=ord(data_tmp[8])
            data_arr=['' for x in xrange(num_packets)]
            data_arr[0]=data_tmp[12:]
            for x in range(1, num_packets):
                data_tmp, server = sock.recvfrom(4096)
                data_arr[ord(data_tmp[9])] = data_tmp[12:]
            data="".join(data_arr)

    elif query is "RULES":
        data=""
        msg="\xff\xff\xff\xff\x56\xff\xff\xff\xff\x00" #get server info
        sock.sendto(msg, (IP,PORT))
        challenge, server = sock.recvfrom(4096)
        msg=challenge.replace("\x41","\x56") + "\x00";
        sock.sendto(msg, (IP,PORT))
        data_tmp, server = sock.recvfrom(4096)
        data=data_tmp
        if data_tmp[0] == "\xfe":
            num_packets=ord(data_tmp[8])
            data_arr=['' for x in xrange(num_packets)]
            data_arr[0]=data_tmp[12:]
            for x in range(1, num_packets):
                data_tmp, server = sock.recvfrom(4096)
                data_arr[ord(data_tmp[9])] = data_tmp[12:]
            data="".join(data_arr)
    return data

def formatINFO(data):
    info = {}
    headerless = data[5:]
    ba=bytearray(headerless)
    #protocol byte
    info["protocol"]=ord(ba[:1])
    ba=ba[1:]
    #name string
    null_index=ba.find(b'\x00')+1
    info["name"]=ba[:null_index]
    ba=ba[null_index:]
    #map string
    null_index=ba.find(b'\x00')+1
    info["map"]=ba[:null_index]
    ba=ba[null_index:]
    #folder string
    null_index=ba.find(b'\x00')+1
    info["folder"]=ba[:null_index]
    ba=ba[null_index:]
    #game string
    null_index=ba.find(b'\x00')+1
    info["game"]=ba[:null_index]
    ba=ba[null_index:]
    #id short
    info["id"]=struct.unpack('h', ba[:2])[0]
    ba=ba[2:]
    #players byte
    info["players"]=ord(ba[:1])
    ba=ba[1:]
    #max players byte
    info["max_players"]=ord(ba[:1])
    ba=ba[1:]
    #bots byte
    info["bots"]=ord(ba[:1])
    ba=ba[1:]
    #servertype byte
    info["servertype"]=ba[:1]
    ba=ba[1:]
    #env byte
    info["environment"]=ba[:1]
    ba=ba[1:]
    #visibility byte
    info["visibility"]=ord(ba[:1])
    ba=ba[1:]
    #vac byte
    info["vac"]=ord(ba[:1])
    ba=ba[1:]
    #version string
    null_index=ba.find(b'\x00')+1
    info["version"]=ba[:null_index]
    ba=ba[null_index:]
    #edf byte
    info["edf"]=ord(ba[:1])
    ba=ba[1:]
    if (info["edf"] & 0x80):
        info["port"]=struct.unpack('h', ba[:2])[0]
        ba=ba[2:]
    if (info["edf"] & 0x10):
        info["steamid"]=struct.unpack('i', ba[:4])[0]
        ba=ba[4+2:]
    if (info["edf"] & 0x40):
        info["spec_port"]=struct.unpack('h', ba[:2])[0]
        ba=ba[2:]
        null_index=ba.find(b'\x00')+1
        info["spec_name"]=ba[:null_index]
        ba=ba[null_index:]
    if (info["edf"] & 0x20):
        null_index=ba.find(b'\x00')+1
        info["keywords"]=ba[:null_index]
        ba=ba[null_index:]
    if (info["edf"] & 0x01):
        info["gameid_64"]=struct.unpack('i', ba[:4])[0]
        ba=ba[4:]
    return info

def formatPLAYER(data): #list of (name, score, duration [s])
    players=[]
    headerless = data[6:]
    num_players = ord(data[5]);
    ba=bytearray(headerless)
    for x in xrange(0,num_players):
        #chunk index byte
        index=ord(ba[:1])
        ba=ba[1:]
        #name string
        null_index=ba.find(b'\x00')+1
        name=ba[:null_index]
        ba=ba[null_index:]
        #score long
        score=struct.unpack('i', ba[:4])[0]
        ba=ba[4:]
        #duration float
        duration=struct.unpack('f', ba[:4])[0]
        ba=ba[4:]
        #print "name: %s\nscore: %d\nduration: %f\n" % (name, score, duration)
        players.append((name, score, duration))
    return players

def formatRULES(data):
    rules={}
    headerless = data[5:]
    ba=bytearray(headerless)
    num_rules = struct.unpack('h', ba[:2])[0]
    ba=ba[2:]
    print num_rules
    for x in xrange(0,num_rules):
        null_index=ba.find(b'\x00')+1
        key=ba[:null_index].decode()
        ba=ba[null_index:]
        null_index=ba.find(b'\x00')+1
        rules[key]=ba[:null_index]
        ba=ba[null_index:]
    return rules
def main():

    if "i" in args:
        print "\n\nSERVER INFO\n--------------------"
        info_raw_data = query("INFO")
        info = formatINFO(info_raw_data)
        for key in info:
            print "%s: %s" % (key, info[key])
        print "--------------------\n"
    if "p" in args:
        print "PLAYER INFO"
        player_raw_data = query("PLAYER")
        players = formatPLAYER(player_raw_data)
        for player in players:
            print "--------------------\nname: %s\nscore: %d\nduration: %f" % (player[0], player[1], player[2])
        print "--------------------"
    if "r" in args:
        print "\nRULES\n--------------------"
        rules_raw_data = query("RULES")
        rules=formatRULES(rules_raw_data)
        for key in rules:
            print "%s: %s" % (key, rules[key])

        print "--------------------\n"

    sock.close()




if __name__ == "__main__":
    main()
