import re

def clean_to_int(x):
    if isinstance(x, bytes):
        return int(x.decode())
    if isinstance(x, str):
        # Match negative and positive numbers inside possible b'' or quotes
        match = re.match(r"b?'?\"?(-?\d+)'?\"?", x)
        if match:
            return int(match.group(1))
        # If not matching, try direct conversion
        try:
            return int(x)
        except ValueError:
            return None  # or np.nan if you want to handle missing values
    return int(x)

# Apply cleaning only to columns that should be int
cols = ['sfh', 'popupwidnow', 'sslfinal_state', 'request_url', 'url_of_anchor',
        'web_traffic', 'url_length', 'age_of_domain', 'having_ip_address', 'result']

df[cols] = df[cols].applymap(clean_to_int)
df = df.astype('int64')
df.info()