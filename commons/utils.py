import time


def append_str_to(append_to: str, *args, sep=", ", **kwargs):
    """Concatenate to a string.
    Args:
        append_to(str): The string to append to.
        args(list): list of string characters to concatenate.
        sep(str): Seperator to use between concatenated strings.
        kwargs(dict): Mapping of variables with intended string values.
    Returns:
        str, joined strings seperated
    """
    append_to = append_to or ""
    result_list = [append_to] + list(args) + list(kwargs.values())
    return f"{sep}".join(filter(len, result_list))

def return_complete_address(self):
    address = ""
    if self.address_line:
        address += self.address_line
    if self.street:
        if address:
            address += ", " + self.street
        else:
            address += self.street
    if self.city:
        if address:
            address += ", " + self.city
        else:
            address += self.city
    if self.state:
        if address:
            address += ", " + self.state
        else:
            address += self.state
    if self.postcode:
        if address:
            address += ", " + self.postcode
        else:
            address += self.postcode
    if self.country:
        if address:
            address += ", " + self.get_country_display()
        else:
            address += self.get_country_display()
    return address


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def convert_to_custom_timezone(custom_date, custom_timezone, to_utc=False):
    user_time_zone = pytz.timezone(custom_timezone)
    if to_utc:
        custom_date = user_time_zone.localize(custom_date.replace(tzinfo=None))
        user_time_zone = pytz.UTC
    return custom_date.astimezone(user_time_zone)

def img_url(self, filename):
    hash_ = int(time.time())
    return "%s/%s/%s" % ("profile_pics", hash_, filename)