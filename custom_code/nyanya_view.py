from main.models import Language, Profile, Language,SERVICE_TYPE, EDUCATION_DEGREE_LIST, PROFILE_STATUS_LIST

SERVICE_TYPE = [SERVICE_TYPE[x][0] for x in range(0,len(SERVICE_TYPE))]
EDUCATION_DEGREE_LIST = [EDUCATION_DEGREE_LIST[x][0] for x in range(0,len(EDUCATION_DEGREE_LIST))]
PROFILE_STATUS_LIST  = [PROFILE_STATUS_LIST[x][0] for x in range(0,len(PROFILE_STATUS_LIST))]

def get_extra_args(args):
	args['service_types'] = SERVICE_TYPE
	args['degrees'] =  EDUCATION_DEGREE_LIST
	args['statuses'] = PROFILE_STATUS_LIST
	args['languages'] = Language.objects.all()
	return args

