import subprocess

class Ping:

    @staticmethod
    def ping(hostname):
        p = subprocess.Popen(
            'ping ' + hostname, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        pingStatus = 'Ok'

        for line in p.stdout:
            output = line.rstrip().decode('UTF-8')

            if (output.endswith('unreachable')):
                pingStatus = 'Unreachable'
                break
            elif (output.startswith('Ping request could not find host')):
                pingStatus = 'Host not found'
                break
            if (output.startswith('Request timed out.')):
                pingStatus = 'Timed out'
                break

        return pingStatus

    @staticmethod
    def pingList(remoteMachines):

        resultList = []

        for machine in remoteMachines:

            resultList.append(Ping.ping(machine[1]))

        return resultList
