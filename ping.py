import subprocess

class Ping:

    @staticmethod
    def ping(hostname):
        p = subprocess.Popen(
            'ping ' + hostname, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        pingStatus = 'ok'

        for line in p.stdout:
            output = line.rstrip().decode('UTF-8')

            if (output.endswith('unreachable')):
                pingStatus = 'unreachable'
                break
            elif (output.startswith('Ping request could not find host')):
                pingStatus = 'host_not_found'
                break
            if (output.startswith('Request timed out.')):
                pingStatus = 'timed_out'
                break

        return pingStatus
