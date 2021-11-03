import time


def connection_wait():
    """wait until connection count matches target count"""
    settings_dict = read_settings()
    settings_dict.update({"connection_count": str(int(settings_dict["connection_count"]) + 1)})
    write_settings(settings_dict)
    cont = True
    while cont:
        settings_dict = read_settings()
        if get_conn_count(settings_dict) == get_targ_conn(settings_dict):
            cont = False
        else:
            time.sleep(time_sync())


def time_sync(window=5):
    """return the number of seconds until the next multiple of 5"""
    current_time = int(time.time())
    difference = current_time % window
    return window - difference


def setting_startup():
    """set connections to 0 while perservering other settings"""
    settings_dict = read_settings()
    settings_dict.update({"connection_count": "0"})
    write_settings(settings_dict)


def read_settings():
    """return dict with settings from file"""
    file = open("test_settings.txt", "r")
    settings = file.readlines()
    output = {}
    for row in settings:
        row = row.strip()
        parsed_row = row.split("=")
        output.update({parsed_row[0]: parsed_row[1]})
    file.close()
    return output


def write_settings(settings_dict):
    """write settings dict to file"""
    file = open("test_settings.txt", "w")
    keys = list(settings_dict.keys())
    for key in keys:
        file.write(key + "=" + settings_dict[key] + "\n")
    file.close()


def get_conn_count(settings_dict):
    return settings_dict["connection_count"]


def get_targ_conn(settings_dict):
    return settings_dict["target_connection"]
