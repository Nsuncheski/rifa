def iter_store_excluded(cron_dict, store_excluded, report):
    """_summary_
    Args:
        country (dict): Dictionary that comes from cron.
        store_excluded (list): List of dictionaries with excluded locales that comes from Parameter store.
        report (string): Report type.

    Returns:
        exclusionList: Excluded locales or empty string.
    """
    for se in store_excluded[report]:
        if se['country'] == cron_dict['country']:
            exclusionList = se["store"]
            return exclusionList
        else:
            exclusionList = [""]
            
    return exclusionList

store_excluded = {"fc": [{"country": "AR", "division": "SLA", "store": "'SA2', 'PBJ', 'PPZ', 'SSZ', 'PIL'"}, {"country": "BR", "division": "BRA", "store": "'SSO'"}], "dt": [{"country": "BR", "division": "BRA", "store": "'AVA','CRI','FRM','PAC','SSO'"}], "mfy": [{"country": "BR", "division": "BRA", "store": "'SSO'"}]}

cron_dict = {
  "countries": [{
    "country": "AR",
    "exclusionFC": ["SA2", "PBJ", "PPZ"]
  }, {
    "country": "CL"
  }, {
    "country": "EC"
  }, {
    "country": "PE"
  }, {
    "country": "UY"
  }, {
    "country": "AW"
  }, {
    "country": "CO"
  }, {
    "country": "CW"
  }, {
    "country": "SV"
  }, {
    "country": "VE"
  }]
}
import json

# cron_dict = json.loads(cron_dict)
# store_excluded = json.loads(store_excluded)

h = iter_store_excluded({
    "country": "BR"
  }, store_excluded, 'fc')
print(h)