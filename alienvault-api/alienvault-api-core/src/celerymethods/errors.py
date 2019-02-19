# This is a list of potential error codes and their corresponding explanation.
# VERY IMPORTANT: If you ever modify this list, you must include the same modifications in web configuration as well

SYSTEM_UPDATE_ERROR_STRINGS = {
    "0": ("0", "System successfully updated"),
    "1": ("300001", "Update requested with unknown parameters"),
    "2": ("300002", "No /etc/ossim/ossim_setup.conf file was found"),
    "3": ("300003", "No profiles in /etc/ossim/ossim_setup.conf were found"),
    "4": ("300004", "Could not resynchronize package index files. Please try again in a few minutes"),
    "5": ("300005", "apt-get update failed"),
    "6": ("300006", "Error while removing software inventory"),
    "7": ("300007", "The update process is unavailable for this machine. Are you trying to update a trial installation?"),
    "8": ("300008", "Error rewriting sources list while executing apt-get update"),
    "9": ("300009", "Error while removing libio-socket-inet6-perl"),
    "10": ("300010", "Error while installing alienvault-license"),
    "11": ("300011", "Error while installing alienvault-professional"),
    "12": ("300012", "Error stopping monit"),
    "13": ("300013", "Error removing suricata and alienvault-dummy-sensor when trying to remove libhtp1"),
    "14": ("300014", "Error reinstalling suricata and alienvault-dummy-sensor after libhtp1 was removed"),
    "15": ("300015", "Error removing php5-suhosin"),
    "16": ("300016", "Error setting linux-image to 'On Hold' state"),
    "17": ("300017", "Error installing libmysqlclient16"),
    "18": ("300018", "Error: unknown libmysqlclient16 version"),
    "19": ("300019", "Error setting libmysqlclient16 to 'On Hold'"),
    "20": ("300020", "Error unsetting apache2 from 'On Hold' state"),
    "21": ("300021", "Error reinstalling daq"),
    "22": ("300022", "Error looking for perconadb password"),
    "23": ("300023", "Error while doing buildload preseed conf"),
    "24": ("300024", "Error in debconf selections while reconfiguring dash"),
    "25": ("300025", "Error installing dash"),
    "26": ("300026", "Error installing mailbsdx"),
    "27": ("300027", "Error while downloading packages prior to a dist-upgrade operation"),
    "28": ("300028", "Error during a dist-upgrade operation"),
    "29": ("300029", "Error while updating igb-pfring"),
    "30": ("300030", "Error while uninstalling squid2"),
    "31": ("300031", "Error while autoremoving unnecessary packages"),
    "32": ("300032", "Error while purging files/packages not needed any more"),
    "33": ("300033", "Update still not available for this platform"),
    "34": ("300034", "Error: repository check detected a problem"),
    "40": ("300040", "Error: Update script not found in USB device"),
    "50": ("300050", "Error: There is an update instance running. Aborting update"),
    "51": ("300051", "Error: Invalid signature for upgrade file (AV3)"),
    "52": ("300052", "Error: Signature unavailable for upgrade file (AV3)"),
    "53": ("300053", "Error: Invalid key. Are you trying to use an AV3 key?"),
    "54": ("300054", "Error: Please enter a valid AV key"),
    "55": ("300055", "Error: Invalid signature for upgrade file (AV4)"),
    "56": ("300056", "Error: Signature unavailable for upgrade file (AV4)"),
    "57": ("300057", "Error: Invalid signature for upgrade file (feed)"),
    "58": ("300058", "Error: Signature unavailable for upgrade file (feed)"),
    "59": ("300059", "Error: System running in HA Mode. Aborting update"),
    "60": ("300060", "Error: Cannot download upgrade file (AV5)"),
    "61": ("300061", "Error: Invalid signature for upgrade file (AV5)"),
    "62": ("300062", "Error: Signature unavailable for upgrade file (AV5)"),
    "63": ("300063", "Error: Cannot download upgrade file (feed)"),
    "64": ("300064", "Error: Cannot install package from feed update"),
    "70": ("300070", "Not enough free disk space to install the latest updates."),
    "90": ("300090", "An existing task running"),
    "91": ("300091", "Something wrong happened while running the alienvault update"),
    "92": ("300092", "Something wrong happened while retrieving the alienvault-update log file"),
    "93": ("300093", "Something wrong happened while retrieving the alienvault-update return code"),
    "99": ("300099", "An error occurred running alienvault-update")
}