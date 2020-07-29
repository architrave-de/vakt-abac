import vakt
from vakt.rules import CIDR, Eq, Any, And, Greater, Less, SubjectMatch
from vakt import Policy, ALLOW_ACCESS, DENY_ACCESS
from resources import USERS
from flask import abort, Response
import sys


adminFullAcces =  Policy(
    1,
    effect= ALLOW_ACCESS,
    subjects=[{'group':Eq('Admin')}],
    resources=[Any()],
    actions=[Any()],
    description= "User with this policy can perform any action any resource with any method"
)
ownerAccess =  Policy(
    2,
    effect=ALLOW_ACCESS,
    subjects=[Any()],
    resources=[{'owner_id': SubjectMatch('id')}],
    actions=[Eq('GET'), Eq('POST'), Eq('PUT')],
)

policies =[
   adminFullAcces,
   ownerAccess
]
storage = vakt.MemoryStorage()
for policy in policies:
    storage.add(policy)

def get_user(request):
    action = request.method
    token = request.headers.get('Authorization')
    user = None

    for u in USERS:
        if u['token'] == token:
            user = u
            break 
    print(user, file=sys.stderr)
    if user == None:
        unauthourized()
    return [ user, action ]

def auth(request, resource):
    """
    Compute user access
    """
    user, action = get_user(request)
    guard = vakt.Guard(storage, vakt.RulesChecker())
    #print(resource, file=sys.stderr)
    inq = vakt.Inquiry(
         action=action,
         resource=resource,
         subject=user,
     )
    print(inq, file=sys.stderr)
    allowed = guard.is_allowed(inq)
    print(allowed, file=sys.stderr)
    if allowed == False:
        unauthourized()

def unauthourized():
    abort(Response('Unauthourized', 401))