from tasktrail.logic import *
import pprint

s = Services()
s.profile_handler.log_in("Profile 1", "password")
pprint.pprint(s.profile_handler.class_handler.get_assignments())