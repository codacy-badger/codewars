#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def ips_between(start: str, end: str) -> int:
	"""
    A function that receives two IPv4 addresses,
    and returns the number of addresses between
    them (including the first one, excluding the
    last one).

    All inputs will be valid IPv4 addresses in
    the form of strings. The last address will
    always be greater than the first one.
    :param start:
    :param end:
    :return:
    """

	ip_start = [int(a) for a in start.split('.')]
	ip_end = [int(b) for b in end.split('.')]
	ips = zip(ip_start, ip_end)
	ips_range = [0, 0, 0, 0]
	result = 1

	for ip_id, ip in enumerate(ips):
		if ip[0] == ip[1] != 0:
			ips_range[ip_id] = 0
		elif ip[1] == 0 and ip[0] != 0 and ips_range[ip_id - 1] > 0:
			ips_range[ip_id] = 256 - ip[0]
		elif ip[1] > ip[0]:
			ips_range[ip_id] = ip[1] - ip[0]
		elif ip[1] == ip[0] == 0 and ips_range[ip_id - 1] > 0:
			ips_range[ip_id] = 256

	print(ips_range)

	for i in ips_range:
		if i != 0:
			result *= i

	return result


