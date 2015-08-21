
import re
import struct
import codecs


data = b'\x00\xbf\x05@acesover\x00\x00\x00\x00\x00\x80\xe6\xb2\x03\x01\x00\x10\x01\xc0\xa8\x01Bc\xaa\xf3\x84 q q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9f\xc8\xf2o\xfa\xf2\xc8\x9f\xc8\x00\x01\x19\x00\\\xff\xff\xff\x00\xa4\x04\x00\x01\xf9\xff\x81Twelve Gage\x00\x00\x00\x00\x00O!\xe7\x04\x01\x00\x10\x01\xc0\xa8\x00\x03D\xcb\xc2\xa8 q q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00)\r\xdb"\x9a\xdb\r)\x10h\x06\x05E\x0A\x96\x00\x00\x000\xc8\x00@\x02\xdc{@cghaskins933\x00\x00\x00\x00\x00\x8d\xe5\r\x0f\x01\x00\x10\x01\xc0\xa8\x00:A\x81\xba\x99 q q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc6P\xc8\xb1\xe9\xc8P\xc6\x98\xc8\x00\x0cE\x00S\xff\xff\xff\x84\x03\x00\x10\x03\xef\x1e\x18Rozak\x00\x00\x00\x00\x00\xc4Q\xa5\x03\x01\x00\x10\x01\xc0\xa8\x02\xf5k\xdb \x97 q q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa8\xdc\xc9#Y\xc9\xdc\xa8)\xf0\x05\x01E\x05\xa9\x00\x00\x002\x08\x00\xcc\x04\xb7\x07\x88Vapor\x00\x00\x00\x00\x00\xfapD\x05\x01\x00\x10\x01\xc0\xa8\x19\t\xc8\xaf\xae\xf5 q q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\xaa\x13\x99\x9b\x13\xaa(\xe4\x02\x0bE\x0AL\x00\x00\x00i\x84\x04\x00\x05\xf3k\x81^1E^2x^3t^4d^5a^6r^7k^8m^1a^5n\x00\x00\x00\x00\x00\x9c?S\x0c\x01\x00\x10\x01\xc0\xa8\x00\x03E\xcf\xa4\xe6 q q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xed2\x9a\xab\xd8\x9a2\xed\xa2\x14\x00\x02E\x02\x8a\x00\x00\x0039\x02@\x06\xfcQ\xc0~~\x00\x00\x00\x00\x00\xf1\x8f\x17\r\x01\x00\x10\x01\x0A\x00\x00d\xc8g\xa0\xc6 q q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x007\xf5x\x1cHx\xf57d\x94\x07\x0AE\x00\x7f\x00\x00\x00\x04\x05\x00\x10\x07\xff\x1e8ComradeEcho\x00\x00\x00\x00\x00\xce\xfe\x8d\x04\x01\x00\x10\x01\xc0\xa8\x01d\xa7\x8e+? q q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x93\x03\x8e;\xf6\x8e\x03\x93\x15\x00\x00\x00E\t=\x00\x00\x00\xe4\x0f\x00D\x08\x0f\x04\x90Evaristo\x00\x00\x00\x00\x00}G\xcd\x07\x01\x00\x10\x01\xc0\xa8\x00\x07\xba\xd1\xb9\xed q1q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00q\xb6\x16r\xce\x16\xb6q8\x04\x0f\x16\x00\xa8\xff\xff\xff\x88\x08\x04\x00\tS\x0b\x81endless12345\x00\x00\x00\x00\x00\xdb\x1e\xef\x02\x01\x00\x10\x01\xc0\xa8\x00\x12\xdb\xfaB? q q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd3\xf8-&7-\xf8\xd3\x14\x80\x07\x06\x03\x00E\x00\x00\x00\x00\x00\x00@\x0A\xf4\x00@Storm Hunter\x00\x00\x00\x00\x00\x169y\x0c\x01\x00\x10\x01\xc0\xa8\x00d2H\\\x94 q$q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00,L\xcaE\xd4\xcaL,\t,\x01\x0cE\x01\x93\xff\xff\xffB\x03\x00\x00'



def sanityCheck(packet):
	if packet[10] >= 0:
		if packet[11] >= 0:
			if 0 <= packet[12] <= 69:
				if 0 <= packet[13] <= 11:
					return True

	return False

global offset
offset =82
print()

def main():
	global offset
	for each in range(0,10):
		result = re.search(b'.+?\x00{24}......................',data[offset:] , re.DOTALL)
		a = result.group()
		length = len(a)
		nameLength = length - 75
		unpackedPacket = struct.unpack('<b3s%ds5xqIIhh24xIIxhbbbq'%nameLength, a)
		if sanityCheck(unpackedPacket):
			print("long")
			print(unpackedPacket)
			offset = offset + length
		else:
			result = re.search(b'.+?\x00{24}.....................', data[offset:], re.DOTALL)
			a = result.group()
			length = len(a)
			nameLength = length - 74
			unpackedPacket = struct.unpack('<b3s%ds5xqIIhh24xIIhbbbq'%nameLength, a)
			if sanityCheck(unpackedPacket):
				print("short")
				print(unpackedPacket)
				offset = offset + length
						





main()